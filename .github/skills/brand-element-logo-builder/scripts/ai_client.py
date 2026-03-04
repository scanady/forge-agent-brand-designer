import base64
import time
from dataclasses import dataclass

from google import genai
from google.genai import types


@dataclass
class ReferenceImage:
    data: bytes
    mime_type: str

MODEL_ID = "gemini-3.1-flash-image-preview"
MAX_RETRIES = 3
BASE_DELAY_S = 2.0


def generate_image(
    api_key: str,
    prompt: str,
    reference_images: list[ReferenceImage] | None = None,
) -> bytes:
    client = genai.Client(api_key=api_key)

    last_error: Exception | None = None

    for attempt in range(MAX_RETRIES):
        if attempt > 0:
            delay = BASE_DELAY_S * (2 ** (attempt - 1))
            print(f"  Retry {attempt}/{MAX_RETRIES - 1} after {delay:.0f}s...")
            time.sleep(delay)

        try:
            parts: list[types.Part] = []

            if reference_images:
                for ref in reference_images:
                    parts.append(
                        types.Part(
                            inline_data=types.Blob(
                                data=base64.b64encode(ref.data).decode(),
                                mime_type=ref.mime_type,
                            )
                        )
                    )

            parts.append(types.Part(text=prompt))

            response = client.models.generate_content(
                model=MODEL_ID,
                contents=types.Content(role="user", parts=parts),
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
