import os
import sys
import time
from google import genai
from playwright.sync_api import sync_playwright

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("ERROR: Please set your GEMINI_API_KEY environment variable.")
    sys.exit(1)

client = genai.Client(api_key=api_key)

def run_english_test(url: str, test_instruction: str):
    print(f"\n[INFO] Opening URL: {url}")
    print(f"[INFO] Running Test Case: \"{test_instruction}\"")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        
        # Wait for PHP Travels dynamic JavaScript and widgets to fully render
        print("[INFO] Waiting for page and dynamic components to load...")
        time.sleep(6) 
        page.wait_for_load_state("networkidle")

        # Extract all visible text from the entire document body
        page_text = page.locator("body").inner_text()[:25000]

        prompt = f"""
        You are an autonomous QA test agent. 
        The user wants to execute this test case: "{test_instruction}"
        Current Page URL: {url}
        
        Here is the full visible text content extracted from the webpage:
        {page_text}

        Based on this content, check if the test instruction is satisfied.
        Return your answer as a JSON object with these exact keys:
        1. "actions": list of actions taken (e.g. ["navigated to demo page"])
        2. "assertion_passed": true or false
        3. "report": a brief sentence explaining why it passed or failed.
        
        Output ONLY valid JSON without markdown code fences.
        """

        print("[INFO] AI is evaluating the page content...")
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        
        print("\n--- AI Test Execution Report ---")
        print(response.text.strip())
        print("--------------------------------")

        browser.close()

if __name__ == "__main__":
    # Clean URL string with NO brackets
    target_url = "https://phptravels.com/demo"
    test_case = "Verify the demo page loads and check if booking options are visible"
    
    run_english_test(target_url, test_case)