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

## 🎯 SYSTEM SCOPE - TEXT-TO-IMAGE REFINEMENT

**What This System Actually Does:**
- **Input**: Text description of desired face
- **Process**: Iteratively refine text prompts to match target description
- **Output**: Generated image that matches text specification
- **Verification**: AI compares generated image against text description

**Example Target**: "Petite Indian woman with semi-sharp features, expressive dark eyes, long black hair, subtle smile, warm complexion"

**NOT**: Reference image comparison or character consistency across actions
**IS**: Text-driven face generation with iterative prompt refinement