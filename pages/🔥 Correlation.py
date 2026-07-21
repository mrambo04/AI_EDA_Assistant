import streamlit as st
import plotly.express as px

from modules.correlation import (
    correlation_matrix,
    high_correlation
)

st.set_page_config(layout="wide")

st.title("🔥 Correlation Analysis")

if "df" not in st.session_state:
    st.warning("Please upload a dataset first.")
    st.stop()

df = st.session_state["df"]

corr = correlation_matrix(df)

st.subheader("Correlation Matrix")

st.dataframe(corr)

fig = px.imshow(
    corr,
    text_auto=".2f",
    color_continuous_scale="RdBu_r",
    title="Correlation Heatmap"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("Highly Correlated Features")

threshold = st.slider(
    "Correlation Threshold",
    0.5,
    1.0,
    0.8,
    0.05
)

high_corr = high_correlation(df, threshold)

if high_corr.empty:

    st.success("No highly correlated features found.")

else:

    st.dataframe(high_corr)