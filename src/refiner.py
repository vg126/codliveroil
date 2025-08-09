"""Prompt refinement module."""
import os
import sys
import json
import requests

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import config

BASE_URL = config.BASE_URL
HEADERS = {"Authorization": f"Bearer {config.STAGE_TOKEN}"}

REQUEST_TIMEOUT = 30


def refine_prompt(current_prompt: str, errors: dict) -> str:
    """Return an improved prompt based on mismatch errors."""
    instruction = (
        "You refine prompts for an image generation model focused on human faces."
        " Given the current prompt and a dictionary of errors describing missing or"
        " incorrect facial features, return an improved prompt."
    )
    user_content = (
        f"Current prompt: {current_prompt}\nErrors: {json.dumps(errors)}\n"
        "Return only the improved prompt."
    )
    payload = {
        "model": "mistral",
        "messages": [
            {"role": "system", "content": instruction},
            {"role": "user", "content": user_content},
        ],
    }
    try:
        response = requests.post(
            f"{BASE_URL}/v1/chat/completions",
            headers=HEADERS,
            json=payload,
            timeout=REQUEST_TIMEOUT,
        )
        response.raise_for_status()
    except requests.RequestException as exc:
        print(f"Refinement request failed: {exc}")
        return current_prompt

    return (
        response.json()
        .get("choices", [{}])[0]
        .get("message", {})
        .get("content", current_prompt)
        .strip()
    )
