"""Main orchestration loop for the face refinement system."""
from __future__ import annotations

import csv
import json
import os
import sys
import time
from datetime import datetime

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, project_root)

# Import config first
import config

# Import local modules
from src.generator import generate_face
from src.verifier import verify_match
from src.refiner import refine_prompt

TARGET_DESCRIPTION = (
    "Professional man with sharp jawline, bright blue eyes, short brown hair,"
    " slight smile, clean shaven."
)
INITIAL_PROMPT = (
    "photorealistic portrait of a professional man with sharp angular jawline,"
    " bright blue eyes, short brown hair, subtle smile, clean shaven face, studio lighting"
)
THRESHOLD = config.CONVERGENCE_THRESHOLD
MAX_ITERATIONS = config.MAX_ITERATIONS


def main() -> None:
    prompt = INITIAL_PROMPT
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_path = os.path.join("data", f"run_{timestamp}.csv")

    with open(csv_path, "w", newline="") as csvfile:
        fieldnames = ["iteration", "prompt", "image_url", "match_score", "errors"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for iteration in range(1, MAX_ITERATIONS + 1):
            print(f"Iteration {iteration}: generating image...")
            image_url = generate_face(prompt)
            if not image_url:
                print("Image generation failed. Stopping.")
                break

            result = verify_match(image_url, TARGET_DESCRIPTION)
            match_score = result.get("match_score", 0.0)
            errors = result.get("errors", {})

            writer.writerow(
                {
                    "iteration": iteration,
                    "prompt": prompt,
                    "image_url": image_url,
                    "match_score": match_score,
                    "errors": json.dumps(errors),
                }
            )
            csvfile.flush()

            print(f"Score: {match_score:.2f}")
            if match_score >= THRESHOLD:
                print("Target achieved!" )
                break

            prompt = refine_prompt(prompt, errors)
            print(f"Refined prompt: {prompt}")
            time.sleep(2)  # rate limiting

    print(f"Results saved to {csv_path}")


if __name__ == "__main__":
    main()
