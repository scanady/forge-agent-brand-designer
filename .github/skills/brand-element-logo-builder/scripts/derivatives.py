#!/usr/bin/env python3
"""Derivative asset operations: resize, compose, and fit using Pillow."""

import argparse
import io
import re
import sys
import zipfile
from pathlib import Path
from urllib.error import URLError
from urllib.request import urlopen

from PIL import Image, ImageChops, ImageDraw, ImageFont


def _hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    h = hex_color.lstrip("#")
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


def _remove_bg(img: Image.Image, tolerance: int = 30) -> Image.Image:
    """Make the dominant corner color transparent."""
    img = img.convert("RGBA")
    w, h = img.size

    corners = [
        img.getpixel((1, 1))[:3],
        img.getpixel((w - 2, 1))[:3],
        img.getpixel((1, h - 2))[:3],
        img.getpixel((w - 2, h - 2))[:3],
    ]
    bg = max(set(corners), key=corners.count)

    r, g, b, a = img.split()
    bg_r = Image.new("L", img.size, bg[0])
    bg_g = Image.new("L", img.size, bg[1])
    bg_b = Image.new("L", img.size, bg[2])

    dr = ImageChops.difference(r, bg_r)
    dg = ImageChops.difference(g, bg_g)
    db = ImageChops.difference(b, bg_b)

    mr = dr.point(lambda p: 255 if p <= tolerance else 0)
    mg = dg.point(lambda p: 255 if p <= tolerance else 0)
    mb = db.point(lambda p: 255 if p <= tolerance else 0)

    bg_mask = ImageChops.multiply(ImageChops.multiply(mr, mg), mb)
    alpha = bg_mask.point(lambda p: 0 if p == 255 else 255)

    img.putalpha(alpha)
    return img


def _resolve_font(font_name: str, brand_dir: str, size: int = 40) -> ImageFont.FreeTypeFont:
    """Resolve font: check brand-folder/fonts/ first, try Google Fonts fallback."""
    fonts_dir = Path(brand_dir) / "fonts"

    if fonts_dir.exists():
        name_lower = font_name.lower().replace(" ", "")
        for font_file in sorted(fonts_dir.glob("*.[ot]tf")):
            if name_lower in font_file.stem.lower().replace(" ", "").replace("-", ""):
                return ImageFont.truetype(str(font_file), size)
        for font_file in sorted(fonts_dir.glob("*.[ot]tf")):
            for word in font_name.lower().split():
                if len(word) > 2 and word in font_file.stem.lower():
                    return ImageFont.truetype(str(font_file), size)

    font_path = _download_google_font(font_name, fonts_dir)
    if font_path:
        return ImageFont.truetype(str(font_path), size)

    raise FileNotFoundError(
        f'Could not find font "{font_name}".\n'
        f"  Place a .ttf or .otf file in: {fonts_dir}/\n"
        f"  Or ensure the font name matches a Google Fonts family."
    )


def _download_google_font(family: str, fonts_dir: Path) -> Path | None:
    """Download a font family from Google Fonts and cache to fonts_dir."""
    url = f"https://fonts.google.com/download?family={family.replace(' ', '+')}"
    print(f"  Downloading font '{family}' from Google Fonts...")

    try:
        with urlopen(url, timeout=15) as resp:  # noqa: S310
            if resp.status != 200:
                return None
            data = resp.read()
    except (URLError, OSError):
        return None

    fonts_dir.mkdir(parents=True, exist_ok=True)

    try:
        with zipfile.ZipFile(io.BytesIO(data)) as zf:
            ttf_files = [n for n in zf.namelist() if n.lower().endswith(".ttf")]
            if not ttf_files:
                return None

            chosen = None
            for pattern in (r"bold", r"regular"):
                for name in ttf_files:
                    if re.search(pattern, name, re.IGNORECASE):
                        chosen = name
                        break
                if chosen:
                    break
            if not chosen:
                chosen = ttf_files[0]

            font_data = zf.read(chosen)
            out_path = fonts_dir / Path(chosen).name
            out_path.write_bytes(font_data)
            print(f"  Cached font: {out_path}")
            return out_path
    except zipfile.BadZipFile:
        return None


# ── Subcommands ──────────────────────────────────────────────


def cmd_resize(args: argparse.Namespace) -> None:
    """Exact LANCZOS resize."""
    img = Image.open(args.input).convert("RGBA")
    if args.remove_bg:
        img = _remove_bg(img)
    resized = img.resize((args.width, args.height), Image.Resampling.LANCZOS)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    resized.save(args.output, "PNG")
    size_kb = Path(args.output).stat().st_size / 1024
    print(f"  Done: {args.output} ({size_kb:.1f} KB)")


def cmd_compose(args: argparse.Namespace) -> None:
    """Place image centered on a solid-color canvas, optionally with text."""
    img = Image.open(args.input).convert("RGBA")
    img = _remove_bg(img)

    canvas = Image.new("RGBA", (args.width, args.height), _hex_to_rgb(args.bg_color) + (255,))
    padding = int(min(args.width, args.height) * args.padding)
    max_w = args.width - (padding * 2)
    max_h = args.height - (padding * 2)

    # Reserve space for text if provided
    text_height = 0
    font = None
    if args.text:
        font = _resolve_font(args.font_name, args.brand_dir, size=32)
        draw_temp = ImageDraw.Draw(canvas)
        bbox = draw_temp.textbbox((0, 0), args.text, font=font)
        text_height = bbox[3] - bbox[1] + int(args.height * 0.08)
        max_h -= text_height

    ratio = min(max_w / img.width, max_h / img.height)
    new_w = int(img.width * ratio)
    new_h = int(img.height * ratio)
    resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)

    x = (args.width - new_w) // 2
    y = padding + (max_h - new_h) // 2
    canvas.paste(resized, (x, y), resized)

    if args.text and font:
        draw = ImageDraw.Draw(canvas)
        bbox = draw.textbbox((0, 0), args.text, font=font)
        tw = bbox[2] - bbox[0]
        tx = (args.width - tw) // 2
        ty = padding + max_h + int(args.height * 0.04)
        draw.text((tx, ty), args.text, fill=(255, 255, 255, 255), font=font)

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    canvas.save(args.output, "PNG")
    size_kb = Path(args.output).stat().st_size / 1024
    print(f"  Done: {args.output} ({size_kb:.1f} KB)")


def cmd_fit(args: argparse.Namespace) -> None:
    """Fit image within bounds maintaining aspect ratio, transparent padding."""
    img = Image.open(args.input).convert("RGBA")
    if args.remove_bg:
        img = _remove_bg(img)

    ratio = min(args.width / img.width, args.height / img.height)
    new_w = int(img.width * ratio)
    new_h = int(img.height * ratio)

    canvas = Image.new("RGBA", (args.width, args.height), (0, 0, 0, 0))
    resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    x = (args.width - new_w) // 2
    y = (args.height - new_h) // 2
    canvas.paste(resized, (x, y), resized)

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    canvas.save(args.output, "PNG")
    size_kb = Path(args.output).stat().st_size / 1024
    print(f"  Done: {args.output} ({size_kb:.1f} KB)")


def main() -> None:
    parser = argparse.ArgumentParser(description="Derivative asset image operations.")
    sub = parser.add_subparsers(dest="command", required=True)

    # resize
    p_resize = sub.add_parser("resize", help="Exact LANCZOS resize")
    p_resize.add_argument("--input", required=True, help="Source image path")
    p_resize.add_argument("--output", required=True, help="Output PNG path")
    p_resize.add_argument("--width", required=True, type=int, help="Target width")
    p_resize.add_argument("--height", required=True, type=int, help="Target height")
    p_resize.add_argument("--remove-bg", action="store_true", help="Remove background before resizing")

    # compose
    p_compose = sub.add_parser("compose", help="Place image on solid-color canvas")
    p_compose.add_argument("--input", required=True, help="Source image path")
    p_compose.add_argument("--output", required=True, help="Output PNG path")
    p_compose.add_argument("--width", required=True, type=int, help="Canvas width")
    p_compose.add_argument("--height", required=True, type=int, help="Canvas height")
    p_compose.add_argument("--bg-color", required=True, help="Background hex color (e.g., #2E5BFF)")
    p_compose.add_argument("--padding", type=float, default=0.15, help="Padding as fraction of canvas (default: 0.15)")
    p_compose.add_argument("--text", help="Optional text to render below the image")
    p_compose.add_argument("--font-name", help="Font family name (required with --text)")
    p_compose.add_argument("--brand-dir", help="Brand folder path for font resolution (required with --text)")

    # fit
    p_fit = sub.add_parser("fit", help="Fit image within bounds with transparent padding")
    p_fit.add_argument("--input", required=True, help="Source image path")
    p_fit.add_argument("--output", required=True, help="Output PNG path")
    p_fit.add_argument("--width", required=True, type=int, help="Target width")
    p_fit.add_argument("--height", required=True, type=int, help="Target height")
    p_fit.add_argument("--remove-bg", action="store_true", help="Remove background before fitting")

    args = parser.parse_args()

    if hasattr(args, "text") and args.text:
        if not args.font_name:
            parser.error("--font-name is required when --text is specified")
        if not args.brand_dir:
            parser.error("--brand-dir is required when --text is specified")

    {"resize": cmd_resize, "compose": cmd_compose, "fit": cmd_fit}[args.command](args)


if __name__ == "__main__":
    main()
