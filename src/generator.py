"""Image generation module."""
import os
import sys
import time
import requests

# Add the project root to Python path for config import
project_root = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, project_root)

import config

BASE_URL = config.BASE_URL
HEADERS = {"Authorization": f"Bearer {config.STAGE_TOKEN}"}

POLLING_INTERVAL = config.POLLING_INTERVAL
MAX_POLL_ATTEMPTS = int(config.POLL_TIMEOUT / config.POLLING_INTERVAL)  # Calculate attempts from total timeout
REQUEST_TIMEOUT = config.REQUEST_TIMEOUT


def generate_face(prompt: str, reference_url: str | None = None) -> str | None:
    """Generate an image URL for the given prompt.

    If ``reference_url`` is provided the img2img endpoint is used. The
    function polls the ``/check`` endpoint until the generation is
    completed and returns the resulting image URL or ``None`` on failure.
    """
    endpoint = f"{BASE_URL}/images/text2img"
    payload: dict[str, object] = {"prompt": prompt}

    if reference_url:
        endpoint = f"{BASE_URL}/images/img2img"
        payload["parent_image"] = reference_url

    try:
        response = requests.post(
            endpoint, headers=HEADERS, json=payload, timeout=REQUEST_TIMEOUT
        )
        response.raise_for_status()
    except requests.RequestException as exc:
        print(f"Generation request failed: {exc}")
        return None

    data = response.json()
    generation_uuid = data.get("generation_uuid")
    if not generation_uuid:
        return None

    # poll for completion
    for attempt in range(1, MAX_POLL_ATTEMPTS + 1):
        print(f"Polling attempt {attempt}/{MAX_POLL_ATTEMPTS}...")
        try:
            check = requests.post(
                f"{BASE_URL}/check",
                headers=HEADERS,
                json={"generation_uuid": generation_uuid},
                timeout=REQUEST_TIMEOUT,
            )
            check.raise_for_status()
            result = check.json()
        except requests.RequestException as exc:
            print(f"Check request failed: {exc}")
            result = {}

        status = result.get("status") or result.get("state")
        if status == "completed":
            url = result.get("image_url") or result.get("url")
            if not url and isinstance(result.get("images"), list):
                images = result["images"]
                if images:
                    first = images[0]
                    url = first.get("url") if isinstance(first, dict) else first
            return url
        if status in {"failed", "error"}:
            return None
        time.sleep(POLLING_INTERVAL + attempt * 2)
    return None
