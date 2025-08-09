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
REQUEST_TIMEOUT = config.REQUEST_TIMEOUT


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


if __name__ == "__main__":
    print("Testing Chub.ai API endpoints...")
    print(f"Base URL: {BASE_URL}")
    
    try:
        test_chat_completion_endpoint()
        print("✅ Chat completions endpoint working")
    except Exception as e:
        print(f"❌ Chat completions endpoint failed: {e}")
    
    try:
        test_image_generation_endpoint()
        print("✅ Image generation endpoint working")
    except Exception as e:
        print(f"❌ Image generation endpoint failed: {e}")
    
    print("Endpoint testing complete!")
