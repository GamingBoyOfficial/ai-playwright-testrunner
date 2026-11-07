### 2. README for `ai-playwright-testrunner` (Task 2)

```markdown
# AI-Driven Playwright Test Runner

An autonomous QA testing tool built with Python, Playwright, and the Google Gemini API. It accepts plain-English test instructions, inspects live website states dynamically, and generates structured JSON pass/fail evaluation reports.

---

## Prerequisites
- Python 3.10+
- Google Gemini API Key (Free Tier)

---

## Setup & Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/GamingBoyOfficial/ai-playwright-testrunner.git](https://github.com/GamingBoyOfficial/ai-playwright-testrunner.git)
   cd ai-playwright-testrunner

Install dependencies:

Bash
pip install playwright google-genai
playwright install

Set your Gemini API key as an environment variable (recommended for security):

PowerShell
# Windows PowerShell
$env:GEMINI_API_KEY="your_actual_api_key_here"
How to Run
Execute the test runner script:

Bash
python test_runner.py

## Engineering Approach & Limitations
# Approach
Dynamic Interpretation: Instead of relying on rigid, hardcoded CSS selectors or brittle element paths, the tool programmatically extracts the live visible text from the page DOM.

LLM Reasoning: Passes the extracted text and plain-English instruction into Gemini (gemini-2.5-flash), returning a structured JSON execution report containing actions taken, assertions passed/failed, and a summary report.

# Limitations
Dependent on token constraints and clarity of the extracted DOM text. Extremely massive single-page applications with deeply nested shadow DOM structures may require more granular element slicing before ingestion.
