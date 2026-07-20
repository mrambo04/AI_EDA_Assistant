import streamlit as st
from modules.loader import load_dataset

st.set_page_config(
    page_title="AI EDA Assistant",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI EDA Assistant")

st.markdown("""
## Welcome 👋

Upload your dataset once.

Then navigate through the pages from the sidebar.
""")

uploaded_file = st.file_uploader(
    "Upload CSV or Excel",
    type=["csv", "xlsx"]
)

if uploaded_file:

    df = load_dataset(uploaded_file)

    # Save dataset globally
    st.session_state["df"] = df

    st.success("✅ Dataset Uploaded Successfully")

    st.write("### Dataset Preview")

    st.dataframe(df.head())

else:

    st.info("Please upload a dataset.")


