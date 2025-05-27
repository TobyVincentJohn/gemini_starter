from google import genai
from dotenv import load_dotenv
import json
import re
import os

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["How does AI work?"]
)
print(response.text)

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

result = extract_and_validate_json(response.text)
print(result)