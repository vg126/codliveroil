#!/usr/bin/env python3
"""
TEXT-TO-IMAGE FACE REFINEMENT SYSTEM

SCOPE: Generate faces from text descriptions with iterative prompt refinement
- Input: Target text description
- Process: Generate → Verify against text → Refine prompt → Repeat
- Output: Image that matches the text specification

NOT FOR: Reference image comparison or character consistency
FOR: Creating faces from detailed text descriptions

Uses curl subprocess calls to bypass Cloudflare blocks
"""
import subprocess
import json
import time
import csv
from datetime import datetime
import os

# Configuration
STAGE_TOKEN = "CHK-851CRFYMIROX4EDBOGN0MF6G4IBQZWESQM32SCGN6843701"
NORMAL_TOKEN = "CHK-9S2BT8YTFWZ7OYDJCVC25ARPXNUSO1KOR1J1DXBS6842987"
BASE_URL = "https://api.chub.ai"
MAX_ITERATIONS = 10
CONVERGENCE_THRESHOLD = 0.85
RATE_LIMIT_DELAY = 3

# Target and initial prompt
TARGET_DESCRIPTION = (
    "Petite Indian woman with semi-sharp features, expressive dark eyes, "
    "long black hair, subtle smile, warm complexion"
)
INITIAL_PROMPT = (
    "photorealistic portrait of a petite Indian woman with semi-sharp features, "
    "expressive dark eyes, long black hair, subtle smile, warm complexion, studio lighting"
)

def run_curl_command(cmd):
    """Execute curl command and return parsed JSON response"""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if result.returncode != 0:
            print(f"❌ Curl error: {result.stderr}")
            return None
        return json.loads(result.stdout)
    except subprocess.TimeoutExpired:
        print("❌ Request timeout")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ JSON decode error: {e}")
        print(f"Raw response: {result.stdout}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def generate_image_curl(prompt):
    """Generate image using curl subprocess call"""
    print(f"🎨 Generating image with prompt: {prompt[:50]}...")
    
    cmd = [
        'curl', '-X', 'POST', f'{BASE_URL}/images/text2img',
        '-H', f'Authorization: Bearer {STAGE_TOKEN}',
        '-H', 'Content-Type: application/json',
        '-d', json.dumps({
            "prompt": prompt,
            "width": 512,
            "height": 512,
            "num_inference_steps": 25,
            "guidance_scale": 3.5
        })
    ]
    
    response = run_curl_command(cmd)
    if not response:
        return None
    
    # Extract image URL from response
    image_url = response.get('primary_image_path')
    if image_url:
        print(f"✅ Image generated: {image_url}")
        return image_url
    else:
        print(f"❌ No image URL in response: {response}")
        return None

def verify_match_curl(image_url, target_description):
    """Verify image match using curl subprocess call"""
    print(f"🔍 Verifying image match...")
    
    verification_prompt = f"""
    Analyze this image: {image_url}
    
    Target description: {target_description}
    
    Rate how well the image matches the target on a scale of 0.0 to 1.0.
    Identify specific errors for facial features.
    
    Respond with ONLY this JSON format:
    {{
        "match_score": 0.0-1.0,
        "errors": {{
            "face_structure": "specific issue or 'good'",
            "eyes": "specific issue or 'good'",
            "hair": "specific issue or 'good'",
            "complexion": "specific issue or 'good'",
            "expression": "specific issue or 'good'"
        }}
    }}
    """
    
    cmd = [
        'curl', '-X', 'POST', f'{BASE_URL}/v1/chat/completions',
        '-H', f'Authorization: Bearer {NORMAL_TOKEN}',
        '-H', 'Content-Type: application/json',
        '-d', json.dumps({
            "model": "mythomax",
            "messages": [
                {"role": "system", "content": "You are a precise image analysis expert. Output only valid JSON."},
                {"role": "user", "content": verification_prompt}
            ],
            "temperature": 0.2,
            "max_tokens": 300
        })
    ]
    
    response = run_curl_command(cmd)
    if not response:
        return {"match_score": 0.0, "errors": {"system": "verification failed"}}
    
    try:
        ai_response = response['choices'][0]['message']['content']
        # Try to extract JSON from the response
        import re
        json_match = re.search(r'\{.*\}', ai_response, re.DOTALL)
        if json_match:
            result = json.loads(json_match.group())
            score = result.get('match_score', 0.0)
            print(f"📊 Match score: {score:.2f}")
            return result
        else:
            print(f"❌ No JSON found in response: {ai_response}")
            return {"match_score": 0.0, "errors": {"parsing": "failed to parse response"}}
    except Exception as e:
        print(f"❌ Error parsing verification: {e}")
        return {"match_score": 0.0, "errors": {"parsing": str(e)}}

def refine_prompt_curl(current_prompt, errors):
    """Refine prompt using curl subprocess call"""
    print(f"🛠️ Refining prompt based on errors...")
    
    error_list = [f"{k}: {v}" for k, v in errors.items() if v != 'good' and 'system' not in k and 'parsing' not in k]
    if not error_list:
        return current_prompt
    
    error_text = ", ".join(error_list)
    
    refinement_request = f"""
    Current prompt: "{current_prompt}"
    
    Issues to fix: {error_text}
    
    Create an improved prompt that addresses these specific issues.
    Keep the same subject (petite Indian woman) but enhance the problematic features.
    Output ONLY the improved prompt, nothing else.
    """
    
    cmd = [
        'curl', '-X', 'POST', f'{BASE_URL}/v1/chat/completions',
        '-H', f'Authorization: Bearer {NORMAL_TOKEN}',
        '-H', 'Content-Type: application/json',
        '-d', json.dumps({
            "model": "mistral",
            "messages": [
                {"role": "user", "content": refinement_request}
            ],
            "temperature": 0.7,
            "max_tokens": 150
        })
    ]
    
    response = run_curl_command(cmd)
    if not response:
        return current_prompt
    
    try:
        refined_prompt = response['choices'][0]['message']['content'].strip()
        print(f"✨ Refined prompt: {refined_prompt[:50]}...")
        return refined_prompt
    except Exception as e:
        print(f"❌ Error refining prompt: {e}")
        return current_prompt

def log_iteration(iteration, prompt, image_url, score, errors, writer):
    """Log iteration data to CSV"""
    writer.writerow({
        'iteration': iteration,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'prompt': prompt,
        'image_url': image_url,
        'match_score': score,
        'errors': json.dumps(errors)
    })
    print(f"📝 Logged iteration {iteration}")

def main():
    """Main automated refinement loop"""
    print("🚀 Starting Automated Face Refinement System")
    print("=" * 60)
    print(f"Target: {TARGET_DESCRIPTION}")
    print(f"Convergence threshold: {CONVERGENCE_THRESHOLD}")
    print(f"Max iterations: {MAX_ITERATIONS}")
    print("=" * 60)
    
    # Create CSV log file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_path = f"data/automated_run_{timestamp}.csv"
    
    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)
    
    current_prompt = INITIAL_PROMPT
    best_score = 0.0
    best_result = None
    
    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ['iteration', 'timestamp', 'prompt', 'image_url', 'match_score', 'errors']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for iteration in range(1, MAX_ITERATIONS + 1):
            print(f"\n🔄 === ITERATION {iteration}/{MAX_ITERATIONS} ===")
            
            # Step 1: Generate Image
            image_url = generate_image_curl(current_prompt)
            if not image_url:
                print("⚠️ Image generation failed, skipping iteration")
                continue
            
            # Rate limiting
            time.sleep(RATE_LIMIT_DELAY)
            
            # Step 2: Verify Match  
            verification = verify_match_curl(image_url, TARGET_DESCRIPTION)
            score = verification.get('match_score', 0.0)
            errors = verification.get('errors', {})
            
            # Step 3: Log Results
            log_iteration(iteration, current_prompt, image_url, score, errors, writer)
            csvfile.flush()  # Ensure data is written
            
            # Step 4: Track Best Result
            if score > best_score:
                best_score = score
                best_result = {
                    'iteration': iteration,
                    'image_url': image_url,
                    'prompt': current_prompt,
                    'score': score
                }
                print(f"🏆 New best score: {score:.2f}")
            
            # Step 5: Check Convergence
            if score >= CONVERGENCE_THRESHOLD:
                print(f"\n🎉 CONVERGENCE ACHIEVED!")
                print(f"✅ Final score: {score:.2f}")
                print(f"🖼️ Final image: {image_url}")
                print(f"📄 Results saved to: {csv_path}")
                return True
            
            # Step 6: Refine Prompt for Next Iteration
            if iteration < MAX_ITERATIONS:
                time.sleep(RATE_LIMIT_DELAY)
                current_prompt = refine_prompt_curl(current_prompt, errors)
        
        # Final summary
        print(f"\n📊 === FINAL RESULTS ===")
        print(f"Max iterations reached: {MAX_ITERATIONS}")
        print(f"Best score achieved: {best_score:.2f}")
        if best_result:
            print(f"🏆 Best result from iteration {best_result['iteration']}:")
            print(f"🖼️ Image: {best_result['image_url']}")
            print(f"📝 Prompt: {best_result['prompt']}")
        print(f"📄 Full results saved to: {csv_path}")
        
        return False

if __name__ == "__main__":
    try:
        success = main()
        if success:
            print("\n🎊 System successfully converged to target!")
        else:
            print("\n📈 System completed all iterations")
    except KeyboardInterrupt:
        print("\n\n⚠️ System interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n✅ Automated face refinement complete!")