import streamlit as st
import pandas as pd
from modules.ai import generate_insights

st.set_page_config(
    page_title="Chat with Dataset",
    page_icon="💬",
    layout="wide"
)

st.title("💬 Chat with Dataset")

# Check if dataset is uploaded
if "df" not in st.session_state:
    st.warning("⚠️ Please upload a dataset first.")
    st.stop()

df = st.session_state["df"]


# -----------------------------
# Pandas-based Assistant
# -----------------------------
def answer_with_pandas(question, df):
    q = question.lower().strip()

    # Dataset Overview
    if "tell me about dataset" in q or "about dataset" in q:
        return f"""
## 📊 Dataset Overview

- **Rows:** {df.shape[0]}
- **Columns:** {df.shape[1]}
- **Missing Values:** {df.isnull().sum().sum()}
- **Duplicate Rows:** {df.duplicated().sum()}

### Column Names

{", ".join(df.columns)}
"""

    # Rows
    elif "rows" in q:
        return f"📊 The dataset contains **{df.shape[0]} rows**."

    # Columns
    elif "columns" in q and "column names" not in q:
        return f"📋 The dataset contains **{df.shape[1]} columns**."

    # Column Names
    elif "column names" in q or "list columns" in q:
        return "### 📋 Column Names\n\n" + "\n".join(
            [f"- {col}" for col in df.columns]
        )

    # Missing Values
    elif "missing" in q:
        return "### Missing Values\n\n```\n" + df.isnull().sum().to_string() + "\n```"

    # Duplicate Rows
    elif "duplicate" in q:
        return f"🔁 Duplicate Rows: **{df.duplicated().sum()}**"

    # Data Types
    elif "data type" in q or "dtypes" in q:
        return "### Data Types\n\n```\n" + df.dtypes.to_string() + "\n```"

    # Statistics
    elif "statistics" in q or "summary" in q or "describe" in q:
        return "### Statistical Summary\n\n```\n" + df.describe(include="all").to_string() + "\n```"

    # Numeric Columns
    elif "numeric columns" in q:
        cols = df.select_dtypes(include="number").columns.tolist()
        return "### Numeric Columns\n\n" + "\n".join([f"- {c}" for c in cols])

    # Categorical Columns
    elif "categorical columns" in q:
        cols = df.select_dtypes(exclude="number").columns.tolist()
        return "### Categorical Columns\n\n" + "\n".join([f"- {c}" for c in cols])

    # Memory Usage
    elif "memory" in q:
        mem = df.memory_usage(deep=True).sum() / 1024**2
        return f"💾 Dataset Memory Usage: **{mem:.2f} MB**"

    # Shape
    elif "shape" in q:
        return f"Dataset Shape: **{df.shape}**"

    # Head
    elif "head" in q or "top rows" in q:
        return df.head().to_markdown(index=False)

    # Tail
    elif "tail" in q or "last rows" in q:
        return df.tail().to_markdown(index=False)

    # Null Percentage
    elif "missing percentage" in q:
        percent = (df.isnull().mean() * 100).round(2)
        return "```\n" + percent.to_string() + "\n```"

    # Unknown question
    else:
        return None


# -----------------------------
# Chat History
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# -----------------------------
# Chat Input
# -----------------------------
question = st.chat_input("Ask anything about your dataset...")

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            # Try Pandas first
            answer = answer_with_pandas(question, df)

            # If Pandas doesn't know, ask Gemini
            if answer is None:

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

Use ONLY the following dataset information to answer.

{dataset_summary}

User Question:
{question}
"""

                answer = generate_insights(prompt)

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
