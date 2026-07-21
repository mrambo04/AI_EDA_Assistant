import streamlit as st
import plotly.express as px

from modules.missing import missing_analysis

st.set_page_config(layout="wide")

st.title("🚨 Missing Value Analysis")

if "df" not in st.session_state:

    st.warning("⚠ Please upload a dataset from Home.")

    st.stop()

df = st.session_state["df"]

missing_df = missing_analysis(df)

if missing_df.empty:

    st.success("🎉 No Missing Values")

else:

    st.dataframe(missing_df)

    fig = px.bar(
        missing_df,
        x="Column",
        y="Percentage",
        color="Percentage",
        text="Percentage"
    )

    st.plotly_chart(fig, use_container_width=True)