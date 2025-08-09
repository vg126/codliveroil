import os
import sys
import time
import requests

# ensure project root on path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import config

BASE_URL = config.BASE_URL
HEADERS = {"Authorization": f"Bearer {config.STAGE_TOKEN}"}
REQUEST_TIMEOUT = 30


def test_image_generation_endpoint():
    start = time.time()
    response = requests.post(
        f"{BASE_URL}/images/text2img",
        headers=HEADERS,
        json={"prompt": "test face", "width": 512, "height": 512},
        timeout=REQUEST_TIMEOUT,
    )
    duration = time.time() - start
    assert response.status_code == 200
    data = response.json()
    assert "generation_uuid" in data
    print(f"/images/text2img responded in {duration:.2f}s")


def test_chat_completion_endpoint():
    start = time.time()
    response = requests.post(
        f"{BASE_URL}/v1/chat/completions",
        headers=HEADERS,
        json={
            "model": "mistral",
            "messages": [{"role": "user", "content": "Say hello"}],
        },
        timeout=REQUEST_TIMEOUT,
    )
    duration = time.time() - start
    assert response.status_code == 200
    data = response.json()
    assert "choices" in data
    print(f"/v1/chat/completions responded in {duration:.2f}s")
