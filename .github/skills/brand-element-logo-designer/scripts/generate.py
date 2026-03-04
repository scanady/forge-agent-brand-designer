#!/usr/bin/env python3
"""Thin CLI tool: send a prompt to Gemini image generation and save the result."""

import argparse
import base64
import sys
import time
from pathlib import Path

from dotenv import load_dotenv
import os

from google import genai
from google.genai import types

SKILL_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(SKILL_ROOT / ".env")

MODEL_ID = "gemini-2.0-flash-exp-image-generation"
MAX_RETRIES = 3
BASE_DELAY_S = 2.0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate an image from a text prompt using Gemini."
    )
    parser.add_argument(
        "--prompt", required=True, help="The full text prompt for image generation"
    )
    parser.add_argument(
        "--output", required=True, help="Output file path (e.g. /path/to/logo.png)"
    )
    return parser.parse_args()


def generate_image(api_key: str, prompt: str) -> bytes:
    """Call Gemini image generation with retry logic. Returns raw image bytes."""
    client = genai.Client(api_key=api_key)
    last_error: Exception | None = None

    for attempt in range(MAX_RETRIES):
        if attempt > 0:
            delay = BASE_DELAY_S * (2 ** (attempt - 1))
            print(f"  Retry {attempt}/{MAX_RETRIES - 1} after {delay:.0f}s...")
            time.sleep(delay)

        try:
            response = client.models.generate_content(
                model=MODEL_ID,
                contents=types.Content(
                    role="user",
                    parts=[types.Part(text=prompt)],
                ),
                config=types.GenerateContentConfig(
                    response_modalities=["image", "text"],
                ),
            )

            if not response.candidates:
                raise RuntimeError("No candidates in response")

            candidate = response.candidates[0]
            if not candidate.content or not candidate.content.parts:
                raise RuntimeError("No content parts in response candidate")

            for part in candidate.content.parts:
                if part.inline_data and part.inline_data.data:
                    image_data = part.inline_data.data
                    if isinstance(image_data, str):
                        return base64.b64decode(image_data)
                    return bytes(image_data)

            raise RuntimeError(
                "No image data found in response. The model may have returned text only."
            )

        except Exception as err:
            last_error = err
            msg = str(err).lower()
            if any(kw in msg for kw in ("rate", "429", "quota")):
                print("  Rate limited, will retry...")
                continue
            if any(kw in msg for kw in ("500", "503", "internal")):
                print("  Server error, will retry...")
                continue
            raise

    raise RuntimeError(
        f"Failed after {MAX_RETRIES} attempts. Last error: {last_error}"
    )


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

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"Generating image...")
    print(f"  Output: {output_path}")
    print(f"  Prompt length: {len(args.prompt)} chars")

    try:
        image_data = generate_image(api_key, args.prompt)
        output_path.write_bytes(image_data)
        size_kb = len(image_data) / 1024
        print(f"  Done ({size_kb:.1f} KB)")
    except Exception as err:
        print(f"  FAILED: {err}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
