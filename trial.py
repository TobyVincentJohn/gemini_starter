'''
import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)
'''
'''
import json
import re

def extract_and_validate_json(text):
    pattern = r"\[.*\]"
    matches = re.findall(pattern, text, re.DOTALL)
    
    if matches:
        json_text = matches[-1]
        try:
            json_data = json.loads(json_text)
            return json_data
        except json.JSONDecodeError:
            return "Invalid JSON format."
    else:
        return "No JSON found in the text."

# Example usage
text = """
Impact: {
    "description": "How new technologies are affecting cybersecurity",
    "associated_risks": ["Risk 1", "Risk 2"]
}
Compliance and Regulatory Issues: {
    "Challenges": {
        "description": "Current compliance challenges faced",
        "regulatory_updates": "Recent regulatory updates"
    }
}
Provide a comprehensive analysis that a cybersecurity professional would find informative and actionable.
"""

result = extract_and_validate_json(text)
print(result)'''