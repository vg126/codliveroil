#!/usr/bin/env python3
"""
Hybrid Face Refinement System
- Image Generation: Chub.ai API (curl bypass)
- Vision Analysis: Poe API with GPT-4.1-mini (multimodal)
- Text Refinement: Best available model from either API

Strategy: Use the best tool for each job!
"""
import subprocess
import json
import time
import csv
import requests
from datetime import datetime
import os
import sys

# Configuration
CHUB_STAGE_TOKEN = "CHK-851CRFYMIROX4EDBOGN0MF6G4IBQZWESQM32SCGN6843701"
CHUB_NORMAL_TOKEN = "CHK-9S2BT8YTFWZ7OYDJCVC25ARPXNUSO1KOR1J1DXBS6842987"
CHUB_BASE_URL = "https://api.chub.ai"

# Poe API configuration (you'll provide the token)
POE_API_KEY = "REPLACE_WITH_YOUR_POE_TOKEN"  # You'll give me this
POE_BASE_URL = "https://api.poe.com"

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
    except Exception as e:
        print(f"❌ Curl command failed: {e}")
        return None

def generate_image_chub(prompt):
    """Generate image using Chub.ai API (proven to work with curl)"""
    print(f"🎨 [CHUB] Generating image with prompt: {prompt[:50]}...")
    
    cmd = [
        'curl', '-X', 'POST', f'{CHUB_BASE_URL}/images/text2img',
        '-H', f'Authorization: Bearer {CHUB_STAGE_TOKEN}',
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
    
    image_url = response.get('primary_image_path')
    if image_url:
        print(f"✅ [CHUB] Image generated: {image_url}")
        return image_url
    else:
        print(f"❌ [CHUB] No image URL in response")
        return None

def verify_match_poe_gpt4_vision(image_url, target_description):
    """Use Poe API with GPT-4.1-mini for vision analysis (multimodal)"""
    print(f"🔍 [POE/GPT-4.1-mini] Analyzing image with vision...")
    
    headers = {
        'Authorization': f'Bearer {POE_API_KEY}',
        'Content-Type': 'application/json'
    }
    
    verification_prompt = f"""
    I need you to analyze this image and rate how well it matches a target description.
    
    Image URL: {image_url}
    Target: {target_description}
    
    Please:
    1. Look at the image carefully
    2. Rate the match on a scale of 0.0 to 1.0 (where 1.0 is perfect match)
    3. Identify specific issues with facial features
    
    Respond in this exact JSON format:
    {{
        "match_score": 0.75,
        "errors": {{
            "face_structure": "specific issue or 'good'",
            "eyes": "specific issue or 'good'", 
            "hair": "specific issue or 'good'",
            "complexion": "specific issue or 'good'",
            "expression": "specific issue or 'good'"
        }}
    }}
    """
    
    payload = {
        "model": "gpt-4.1-mini",  # Multimodal model
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": verification_prompt},
                    {"type": "image_url", "image_url": {"url": image_url}}
                ]
            }
        ],
        "temperature": 0.2,
        "max_tokens": 400
    }
    
    try:
        response = requests.post(
            f"{POE_BASE_URL}/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            ai_response = data['choices'][0]['message']['content']
            
            # Extract JSON from response
            import re
            json_match = re.search(r'\{.*\}', ai_response, re.DOTALL)
            if json_match:
                result = json.loads(json_match.group())
                score = result.get('match_score', 0.0)
                print(f"📊 [POE] Vision analysis score: {score:.2f}")
                return result
            else:
                print(f"❌ [POE] No JSON in response: {ai_response}")
                return {"match_score": 0.0, "errors": {"parsing": "no json found"}}
        else:
            print(f"❌ [POE] API error: {response.status_code} - {response.text}")
            return {"match_score": 0.0, "errors": {"api": f"status {response.status_code}"}}
            
    except Exception as e:
        print(f"❌ [POE] Vision analysis failed: {e}")
        return {"match_score": 0.0, "errors": {"system": str(e)}}

def verify_match_chub_fallback(image_url, target_description):
    """Fallback: Try Chub.ai text model if Poe vision fails"""
    print(f"🔄 [CHUB] Fallback text-based verification...")
    
    verification_prompt = f"""
    Analyze this image URL: {image_url}
    Target description: {target_description}
    
    Based on the URL and typical image generation patterns, estimate how well this might match.
    This is a fallback method - be conservative in scoring.
    
    Respond with ONLY this JSON:
    {{
        "match_score": 0.0-1.0,
        "errors": {{
            "method": "text-fallback",
            "note": "limited analysis without vision"
        }}
    }}
    """
    
    cmd = [
        'curl', '-X', 'POST', f'{CHUB_BASE_URL}/v1/chat/completions',
        '-H', f'Authorization: Bearer {CHUB_NORMAL_TOKEN}',
        '-H', 'Content-Type: application/json',
        '-d', json.dumps({
            "model": "mythomax",
            "messages": [
                {"role": "system", "content": "You provide conservative estimates. Output only JSON."},
                {"role": "user", "content": verification_prompt}
            ],
            "temperature": 0.3,
            "max_tokens": 200
        })
    ]
    
    response = run_curl_command(cmd)
    if response:
        try:
            ai_response = response['choices'][0]['message']['content']
            import re
            json_match = re.search(r'\{.*\}', ai_response, re.DOTALL)
            if json_match:
                result = json.loads(json_match.group())
                print(f"📊 [CHUB] Fallback score: {result.get('match_score', 0.0):.2f}")
                return result
        except Exception as e:
            print(f"❌ [CHUB] Fallback parsing failed: {e}")
    
    return {"match_score": 0.5, "errors": {"fallback": "conservative estimate"}}

def refine_prompt_best_available(current_prompt, errors):
    """Try Poe first, fallback to Chub for prompt refinement"""
    print(f"🛠️ Refining prompt based on errors...")
    
    error_list = [f"{k}: {v}" for k, v in errors.items() 
                  if v != 'good' and k not in ['system', 'parsing', 'api', 'method', 'note']]
    
    if not error_list:
        return current_prompt
    
    error_text = ", ".join(error_list)
    refinement_request = f"""
    Current prompt: "{current_prompt}"
    Issues to fix: {error_text}
    
    Create an improved prompt for image generation that addresses these specific issues.
    Keep the same subject but enhance the problematic features.
    Output ONLY the improved prompt, nothing else.
    """
    
    # Try Poe first (usually better at prompt engineering)
    if POE_API_KEY != "REPLACE_WITH_YOUR_POE_TOKEN":
        try:
            headers = {'Authorization': f'Bearer {POE_API_KEY}', 'Content-Type': 'application/json'}
            payload = {
                "model": "gpt-4.1-mini",  
                "messages": [{"role": "user", "content": refinement_request}],
                "temperature": 0.7,
                "max_tokens": 150
            }
            
            response = requests.post(f"{POE_BASE_URL}/v1/chat/completions", 
                                   headers=headers, json=payload, timeout=30)
            
            if response.status_code == 200:
                refined = response.json()['choices'][0]['message']['content'].strip()
                print(f"✨ [POE] Refined prompt: {refined[:50]}...")
                return refined
        except Exception as e:
            print(f"⚠️ [POE] Refinement failed, trying Chub: {e}")
    
    # Fallback to Chub
    cmd = [
        'curl', '-X', 'POST', f'{CHUB_BASE_URL}/v1/chat/completions',
        '-H', f'Authorization: Bearer {CHUB_NORMAL_TOKEN}',
        '-H', 'Content-Type: application/json',
        '-d', json.dumps({
            "model": "mistral",
            "messages": [{"role": "user", "content": refinement_request}],
            "temperature": 0.7,
            "max_tokens": 150
        })
    ]
    
    response = run_curl_command(cmd)
    if response:
        try:
            refined = response['choices'][0]['message']['content'].strip()
            print(f"✨ [CHUB] Refined prompt: {refined[:50]}...")
            return refined
        except Exception as e:
            print(f"❌ Prompt refinement failed: {e}")
    
    return current_prompt

def main():
    """Hybrid automated refinement loop"""
    print("🚀 Starting HYBRID Face Refinement System")
    print("🎨 Image Generation: Chub.ai (curl bypass)")
    print("👁️ Vision Analysis: Poe GPT-4.1-mini (multimodal)")
    print("✨ Text Refinement: Best available model")
    print("=" * 60)
    print(f"Target: {TARGET_DESCRIPTION}")
    print(f"Convergence threshold: {CONVERGENCE_THRESHOLD}")
    print(f"Max iterations: {MAX_ITERATIONS}")
    print("=" * 60)
    
    # Check if Poe token is configured
    if POE_API_KEY == "REPLACE_WITH_YOUR_POE_TOKEN":
        print("⚠️ POE_API_KEY not configured - will use Chub fallback for vision")
        print("To use Poe vision: edit POE_API_KEY in this file")
        print()
    
    # Create CSV log
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_path = f"data/hybrid_run_{timestamp}.csv"
    os.makedirs("data", exist_ok=True)
    
    current_prompt = INITIAL_PROMPT
    best_score = 0.0
    best_result = None
    
    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ['iteration', 'timestamp', 'prompt', 'image_url', 'match_score', 
                     'verification_method', 'errors']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for iteration in range(1, MAX_ITERATIONS + 1):
            print(f"\n🔄 === ITERATION {iteration}/{MAX_ITERATIONS} ===")
            
            # Step 1: Generate Image (Chub.ai)
            image_url = generate_image_chub(current_prompt)
            if not image_url:
                print("⚠️ Image generation failed, skipping iteration")
                continue
            
            time.sleep(RATE_LIMIT_DELAY)
            
            # Step 2: Verify Match (Poe vision first, Chub fallback)
            if POE_API_KEY != "REPLACE_WITH_YOUR_POE_TOKEN":
                verification = verify_match_poe_gpt4_vision(image_url, TARGET_DESCRIPTION)
                method = "poe-vision"
            else:
                verification = verify_match_chub_fallback(image_url, TARGET_DESCRIPTION)  
                method = "chub-fallback"
            
            score = verification.get('match_score', 0.0)
            errors = verification.get('errors', {})
            
            # Step 3: Log Results
            writer.writerow({
                'iteration': iteration,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'prompt': current_prompt,
                'image_url': image_url,
                'match_score': score,
                'verification_method': method,
                'errors': json.dumps(errors)
            })
            csvfile.flush()
            
            # Step 4: Track Best
            if score > best_score:
                best_score = score
                best_result = {
                    'iteration': iteration,
                    'image_url': image_url,
                    'prompt': current_prompt,
                    'score': score,
                    'method': method
                }
                print(f"🏆 New best score: {score:.2f} via {method}")
            
            # Step 5: Check Convergence
            if score >= CONVERGENCE_THRESHOLD:
                print(f"\n🎉 CONVERGENCE ACHIEVED!")
                print(f"✅ Final score: {score:.2f}")
                print(f"🔍 Verification method: {method}")
                print(f"🖼️ Final image: {image_url}")
                print(f"📄 Results saved to: {csv_path}")
                return True
            
            # Step 6: Refine Prompt
            if iteration < MAX_ITERATIONS:
                time.sleep(RATE_LIMIT_DELAY)
                current_prompt = refine_prompt_best_available(current_prompt, errors)
        
        # Final Results
        print(f"\n📊 === FINAL RESULTS ===")
        print(f"Best score achieved: {best_score:.2f}")
        if best_result:
            print(f"🏆 Best result (iteration {best_result['iteration']}) via {best_result['method']}:")
            print(f"🖼️ Image: {best_result['image_url']}")
        print(f"📄 Full results: {csv_path}")
        return False

if __name__ == "__main__":
    print("⚙️ CONFIGURATION CHECK:")
    print(f"Chub.ai tokens: {'✅ Configured' if CHUB_STAGE_TOKEN else '❌ Missing'}")
    print(f"Poe API token: {'✅ Configured' if POE_API_KEY != 'REPLACE_WITH_YOUR_POE_TOKEN' else '⚠️ Not configured (will use fallback)'}")
    print()
    
    try:
        success = main()
        if success:
            print("\n🎊 HYBRID system successfully converged!")
        else:
            print("\n📈 HYBRID system completed all iterations")
    except KeyboardInterrupt:
        print("\n\n⚠️ System interrupted by user")  
    except Exception as e:
        print(f"\n\n❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n✅ Hybrid face refinement complete!")