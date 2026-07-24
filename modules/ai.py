import streamlit as st
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted

API_KEY = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_insights(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text

    except ResourceExhausted:
        return """
🚫 **Gemini API quota exceeded**

Please try again later or use another API key.
"""

    except Exception as e:
        return f"❌ Error: {e}"



