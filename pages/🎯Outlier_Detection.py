import streamlit as st
import plotly.express as px

from modules.outliers import detect_outliers

st.set_page_config(layout="wide")

st.title("🎯 Outlier Detection")

if "df" not in st.session_state:
    st.warning("Please upload a dataset first.")
    st.stop()

df = st.session_state["df"]

numeric_columns = df.select_dtypes(include="number").columns.tolist()

if not numeric_columns:
    st.error("No numeric columns found.")
    st.stop()

column = st.selectbox(
    "Select Numeric Column",
    numeric_columns
)

result = detect_outliers(df, column)

col1, col2, col3 = st.columns(3)

col1.metric("Outliers", result["Outlier Count"])
col2.metric("Percentage", f'{result["Outlier Percentage"]}%')
col3.metric("IQR", result["IQR"])

st.divider()

st.subheader("IQR Information")

st.write(result)

fig = px.box(
    df,
    y=column,
    points="outliers",
    title=f"Box Plot - {column}"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Detected Outliers")

st.dataframe(result["Outliers"])