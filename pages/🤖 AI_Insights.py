import streamlit as st

from modules.ai import generate_insights

st.set_page_config(
    page_title="AI Insights",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Insights")

if "df" not in st.session_state:
    st.warning("Please upload a dataset first.")
    st.stop()

df = st.session_state["df"]

st.write("Generate AI-powered insights for your dataset.")

if st.button("🚀 Generate AI Report"):

    with st.spinner("Analyzing dataset with Gemini AI..."):

        try:

            sample_data = df.head(5).to_string()

            statistics = df.describe(include="all").fillna("").head().to_string()

            missing_values = df.isnull().sum().to_string()

            data_types = df.dtypes.to_string()

            prompt = f"""
You are an expert Data Analyst.

Analyze the following dataset.

Dataset Information

Rows: {df.shape[0]}
Columns: {df.shape[1]}

Column Data Types

{data_types}

Missing Values

{missing_values}

Statistical Summary

{statistics}

Sample Data

{sample_data}

Provide the following:

1. Dataset Summary

2. Data Quality Issues

3. Missing Value Suggestions

4. Outlier Suggestions

5. Correlation Suggestions

6. Recommended Machine Learning Problem

7. Feature Engineering Suggestions

8. Overall Conclusion

Keep the response professional and easy to understand.
"""

            # Prevent huge prompts
            if len(prompt) > 25000:
                st.error("Dataset is too large for AI analysis. Please upload a smaller dataset.")
                st.stop()

            answer = generate_insights(prompt)

            st.success("AI Report Generated Successfully!")

            st.markdown(answer)

        except Exception as e:

            st.error(f"Error: {e}")
