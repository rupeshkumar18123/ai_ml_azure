# requirements:
#   pip install -U streamlit python-dotenv openai langchain-openai

from langchain_openai import AzureChatOpenAI   # ✅ new import path
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()                                  # reads your .env file
st.title("First Chatbot (Azure OpenAI)")

# ---- Build the LLM ----
llm = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),          # resource URL
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"), # your model deployment name
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),                  # key1 or key2
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),          # e.g. 2024‑06‑01‑preview
    model_name="gpt-4o",
    temperature=0.7,
)

# ---- Streamlit chat loop (stateless reruns) ----
if "history" not in st.session_state:
    st.session_state.history = []

user_msg = st.chat_input("Type your question…")

if user_msg:
    answer = llm.invoke(user_msg).content
    st.session_state.history.append(("You", user_msg))
    st.session_state.history.append(("Assistant", answer))

for role, msg in st.session_state.history:
    st.markdown(f"**{role}:** {msg}")
