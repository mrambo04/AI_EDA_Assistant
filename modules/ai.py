import google.generativeai as genai

# Replace with your API key temporarily
API_KEY = "Api Key "

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_insights(prompt):
    response = model.generate_content(prompt)
    return response.text
