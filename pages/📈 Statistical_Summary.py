import streamlit as st

from modules.statistics import statistics_analysis

st.set_page_config(layout="wide")

st.title("📈 Statistical Summary")

if "df" not in st.session_state:

    st.warning("⚠ Please upload a dataset from Home.")

    st.stop()

df = st.session_state["df"]

stats = statistics_analysis(df)

st.dataframe(stats, use_container_width=True)