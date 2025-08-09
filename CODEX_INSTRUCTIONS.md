# 🤖 GPT Codex Implementation Instructions

## 📋 Your Task
Implement the Face Refinement System using the 3-module architecture described in the README.

## 🏗️ Implementation Plan

### Step 1: API Connectivity Test
Create `tests/test_endpoints.py`:
- Test Chub.ai image generation endpoint (`/images/text2img`)
- Test chat completions endpoint (`/v1/chat/completions`) 
- Verify API keys work correctly
- Log response times and success rates

### Step 2: Module Implementation
Create these files in `src/`:

**`generator.py`**:
- Function: `generate_face(prompt, reference_url=None)`
- Uses `/images/text2img` or `/images/img2img` 
- Handles async polling with `/check` endpoint
- Returns image URL or None

**`verifier.py`**:
- Function: `verify_match(image_url, target_description)`
- Uses `/v1/chat/completions` with vision-capable model
- Returns: `{"match_score": float, "errors": dict}`
- Prompt engineering for accurate scoring

**`refiner.py`**:
- Function: `refine_prompt(current_prompt, errors)`
- Uses text completion models
- Returns improved prompt string
- Focus on facial feature adjustments

### Step 3: Main Orchestrator
Create `src/main.py`:
- Implements the main refinement loop
- Logs all iterations to CSV in `data/` folder
- Real-time progress display
- Convergence detection and reporting

## 🎯 Success Criteria
1. **API connectivity confirmed** via test suite
2. **Complete 3-5 iterations** showing score improvement
3. **CSV output generated** with iteration data
4. **Clear console logging** of progress
5. **Handle errors gracefully** with informative messages

## 🔧 Technical Requirements
- Use the existing API documentation in repo
- Follow rate limiting (2-3 second delays)
- Implement proper error handling
- Generate timestamped CSV outputs
- Maintain session continuity

## 🚀 Execution Flow
```
1. Run tests/test_endpoints.py
2. Execute python src/main.py  
3. Monitor real-time output
4. Check data/ for results
5. Report final convergence status
```

## 💡 Key Implementation Notes
- **Generator**: Handle async image generation with polling
- **Verifier**: Engineer prompts for consistent scoring
- **Refiner**: Focus on anatomical prompt improvements  
- **Main**: Implement clean iteration loop with logging

Start with Step 1 (API tests) and proceed through each step systematically.