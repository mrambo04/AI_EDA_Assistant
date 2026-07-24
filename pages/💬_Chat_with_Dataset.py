import streamlit as st
from modules.ai import generate_insights

st.set_page_config(
    page_title="Chat with Dataset",
    page_icon="💬",
    layout="wide"
)

st.title("💬 Chat with Dataset")

# Check dataset
if "df" not in st.session_state:
    st.warning("Please upload a dataset first.")
    st.stop()

df = st.session_state["df"]

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
question = st.chat_input("Ask anything about your dataset...")

if question:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Create dataset summary
    dataset_summary = f"""
Rows: {df.shape[0]}
Columns: {df.shape[1]}

Column Names:
{list(df.columns)}

Data Types:
{df.dtypes}

Missing Values:
{df.isnull().sum()}

Statistics:
{df.describe(include='all').head()}

Sample Data:
{df.head()}
"""

    prompt = f"""
You are an expert Data Analyst.

Here is the dataset information.

{dataset_summary}

User Question:

{question}

Answer only based on the uploaded dataset.
"""

    # AI response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            answer = generate_insights(prompt)

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )