### agentic-tester/agent/prompts.py
prompt_template = """
You are a helpful testing agent. Your job is to generate a Selenium test script in Python to test the following webpage:

URL: {url}

Your test should:
- Open the page
- Interact with login form if available
- Fill sample inputs
- Click submit or next
- Validate expected outcomes (success, errors)

Use valid XPath or CSS selectors, and ensure the script can run with Selenium and ChromeDriver.
"""

def get_prompt(url):
    return prompt_template.format(url=url)