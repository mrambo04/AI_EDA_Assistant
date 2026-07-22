import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Read API key from .env
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=API_KEY)

# Create model
model = genai.GenerativeModel("gemini-2.5-flash")

def generate_insights(prompt):
    response = model.generate_content(prompt)
    return response.text



