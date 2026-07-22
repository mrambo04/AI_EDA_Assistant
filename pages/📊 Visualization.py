import streamlit as st

from modules.visualization import (
    histogram,
    boxplot,
    scatter,
    bar_chart,
    pie_chart
)

st.set_page_config(layout="wide")

st.title("📊 Data Visualization")

if "df" not in st.session_state:
    st.warning("Please upload a dataset from the Home page.")
    st.stop()

df = st.session_state["df"]

numeric_cols = df.select_dtypes(include="number").columns.tolist()
categorical_cols = df.select_dtypes(exclude="number").columns.tolist()

chart = st.selectbox(
    "Select Chart",
    [
        "Histogram",
        "Box Plot",
        "Scatter Plot",
        "Bar Chart",
        "Pie Chart"
    ]
)

if chart == "Histogram":

    column = st.selectbox("Select Numeric Column", numeric_cols)

    fig = histogram(df, column)

    st.plotly_chart(fig, use_container_width=True)

elif chart == "Box Plot":

    column = st.selectbox("Select Numeric Column", numeric_cols)

    fig = boxplot(df, column)

    st.plotly_chart(fig, use_container_width=True)

elif chart == "Scatter Plot":

    x = st.selectbox("X Axis", numeric_cols)

    y = st.selectbox("Y Axis", numeric_cols)

    fig = scatter(df, x, y)

    st.plotly_chart(fig, use_container_width=True)

elif chart == "Bar Chart":

    column = st.selectbox("Categorical Column", categorical_cols)

    fig = bar_chart(df, column)

    st.plotly_chart(fig, use_container_width=True)

elif chart == "Pie Chart":

    column = st.selectbox("Categorical Column", categorical_cols)

    fig = pie_chart(df, column)

    st.plotly_chart(fig, use_container_width=True)