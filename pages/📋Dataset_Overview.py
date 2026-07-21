import streamlit as st
from modules.overview import dataset_overview

st.set_page_config(layout="wide")

st.title("📋 Dataset Overview")

if "df" not in st.session_state:

    st.warning("⚠ Please upload a dataset from the Home page.")

    st.stop()

df = st.session_state["df"]

overview = dataset_overview(df)

col1, col2, col3 = st.columns(3)

col1.metric("Rows", overview["Rows"])
col2.metric("Columns", overview["Columns"])
col3.metric("Memory", overview["Memory Usage (KB)"])

col1, col2, col3 = st.columns(3)

col1.metric("Missing", overview["Missing Values"])
col2.metric("Duplicates", overview["Duplicate Rows"])
col3.metric("Numeric", overview["Numeric Columns"])

col1, col2, col3 = st.columns(3)

col1.metric("Categorical", overview["Categorical Columns"])
col2.metric("Boolean", overview["Boolean Columns"])
col3.metric("Datetime", overview["Datetime Columns"])

st.divider()

st.subheader("Dataset Preview")

st.dataframe(df)