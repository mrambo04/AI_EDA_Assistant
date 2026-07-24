import os
from dotenv import load_dotenv
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_insights(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text

    except ResourceExhausted:
        return """
🚫 **Gemini API quota exceeded**

You have reached the free API request limit.

Please wait for the quota to reset or use a new API key.
"""

    except Exception as e:
        return f"❌ Error: {str(e)}"



