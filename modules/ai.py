import google.generativeai as genai

# Replace with your API key temporarily
API_KEY = "AQ.Ab8RN6J4lDO74PCDhNyY56kk47od65pQhBqidljZngRpsvOLaw"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_insights(prompt):
    response = model.generate_content(prompt)
    return response.text