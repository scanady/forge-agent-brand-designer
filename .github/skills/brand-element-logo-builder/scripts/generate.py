#!/usr/bin/env python3
"""Generate a single logo image using Google AI Studio (Gemini)."""

import argparse
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

SKILL_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(SKILL_ROOT / ".env")

from ai_client import generate_image, ReferenceImage


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a single brand logo image via Gemini."
    )
    prompt_group = parser.add_mutually_exclusive_group(required=True)
    prompt_group.add_argument("--prompt", help="Generation prompt text")
    prompt_group.add_argument(
        "--prompt-file", help="Path to a text file containing the prompt"
    )
    parser.add_argument("--output", required=True, help="Output PNG file path")
    parser.add_argument(
        "--ref", nargs="*", help="Reference image file paths"
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    api_key = os.environ.get("GOOGLE_AI_STUDIO_API_KEY")
    if not api_key:
        print(
            "Error: GOOGLE_AI_STUDIO_API_KEY not set.\n"
            "Copy .env.example to .env and add your API key.",
            file=sys.stderr,
        )
        sys.exit(1)

    if args.prompt_file:
        prompt = Path(args.prompt_file).read_text(encoding="utf-8").strip()
    else:
        prompt = args.prompt

    refs: list[ReferenceImage] | None = None
    if args.ref:
        refs = []
        for ref_path in args.ref:
            p = Path(ref_path)
            if not p.exists():
                print(f"Reference image not found: {ref_path}", file=sys.stderr)
                sys.exit(1)
            refs.append(ReferenceImage(data=p.read_bytes(), mime_type="image/png"))

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)

    print(f"Generating: {output.name}")
    if refs:
        print(f"  References: {len(refs)} image(s)")

    try:
        image_data = generate_image(api_key, prompt, refs)
        output.write_bytes(image_data)
        print(f"  Done ({len(image_data) / 1024:.1f} KB)")
    except Exception as err:
        print(f"  FAILED: {err}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
