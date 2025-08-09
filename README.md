# Face Generation Refinement System

## 🎯 Mission
Build and execute an iterative face generation system that refines prompts until convergence.

## 🔑 Setup
1. Clone this repository
2. Create `config.py` with your Chub.ai tokens:
```python
STAGE_TOKEN = "YOUR_STAGE_TOKEN_HERE"
NORMAL_TOKEN = "YOUR_NORMAL_TOKEN_HERE"
```
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python src/main.py`

## 🏗️ Architecture
Three-module system with iterative refinement:
- **Generator**: Creates faces from prompts (text2img/img2img)
- **Verifier**: Scores match quality (0-1 scale)
- **Refiner**: Improves prompts based on errors

## 📊 Target Metrics
- Convergence threshold: 0.85
- Max iterations: 10
- Success: 3+ iterations showing score improvement

## 🚀 Execution Instructions for GPT Codex
1. First run `tests/test_endpoints.py` to verify API access
2. Execute main loop with: `python src/main.py`
3. Monitor real-time output
4. Check `data/` folder for CSV results

## 📋 API Reference
- **Image Generation**: See `Chub Imagine API swagger.md`
- **Text Completions**: See `Chub Open AI Spec completions.md`
- **Base URL**: `https://api.chub.ai`

## 🎯 Target Face for Testing
"Professional man with sharp jawline, bright blue eyes, short brown hair, slight smile, clean shaven"

Initial prompt: "photorealistic portrait of a professional man with sharp angular jawline, bright blue eyes, short brown hair, subtle smile, clean shaven face, studio lighting"