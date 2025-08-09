"""Image verification module."""
import os
import sys
import json
import requests

# Add the project root to Python path for config import
project_root = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, project_root)

import config

BASE_URL = config.BASE_URL
HEADERS = {"Authorization": f"Bearer {config.NORMAL_TOKEN}"}

REQUEST_TIMEOUT = config.REQUEST_TIMEOUT


def verify_match(image_url: str, target_description: str) -> dict:
    """Return match score and errors for the image against a description."""
    # Prepare OpenAI-style payload
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": (
                        "You are a vision model that evaluates how well an image matches a"
                        " target description. Respond strictly as JSON with keys 'match_score'"
                        " (0-1 float) and 'errors' (dict). Target description: "
                        f"{target_description}"
                    ),
                },
                {"type": "image_url", "image_url": {"url": image_url}},
            ],
        }
    ]
    payload = {"model": "mistral", "messages": messages}

    try:
        response = requests.post(
            f"{BASE_URL}/v1/chat/completions",
            headers=HEADERS,
            json=payload,
            timeout=REQUEST_TIMEOUT,
        )
        response.raise_for_status()
    except requests.RequestException as exc:
        return {"match_score": 0.0, "errors": {"api": f"verification failed: {exc}"}}

    content = (
        response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
    )
    try:
        data = json.loads(content)
    except Exception:
        data = {"match_score": 0.0, "errors": {"parse": "invalid JSON"}}
    return data
