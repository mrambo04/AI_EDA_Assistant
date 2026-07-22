import streamlit as st

from modules.ai import generate_insights

st.set_page_config(layout="wide")

st.title("🤖 AI Insights")

if "df" not in st.session_state:
    st.warning("Please upload a dataset first.")
    st.stop()

df = st.session_state["df"]

st.write("Click the button to generate AI insights.")

if st.button("Generate AI Report"):

    prompt = f"""
You are an expert Data Analyst.

Analyze this dataset summary.

Rows: {df.shape[0]}
Columns: {df.shape[1]}

Data Types:
{df.dtypes}

Missing Values:
{df.isnull().sum()}

Statistics:
{df.describe(include='all')}

Provide:

1. Dataset Summary
2. Data Quality Issues
3. Missing Value Suggestions
4. Outlier Suggestions
5. Correlation Suggestions
6. Recommended Machine Learning Problem
7. Overall Conclusion
"""

    with st.spinner("Generating AI Insights..."):
        answer = generate_insights(prompt)

    st.markdown(answer)