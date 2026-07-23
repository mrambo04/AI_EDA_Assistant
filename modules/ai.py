import streamlit as st
import google.generativeai as genai

# Read API key from Streamlit Secrets
API_KEY = st.secrets["GEMINI_API_KEY"]

# Configure Gemini
genai.configure(api_key=API_KEY)

# Create model
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_insights(prompt):
    response = model.generate_content(prompt)
    return response.text



