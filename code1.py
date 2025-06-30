from langchain.chat_models import AzureChatOpenAI
import os
from dotenv import load_dotenv
import streamlit  as st

load_dotenv()
st.write("first chatbot")
llm = AzureChatOpenAI(
    openai_api_base=os.getenv("AZURE_OPENAI_API_BASE"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    openai_api_key= os.getenv("AZURE_OPENAI_API_KEY"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    model_name="gpt-4o",
    temperature=0.7,
)

while True:
   text_in= st.text_input("Enter youy query :")
   result= llm.invoke(text_in)
   st.write(result.content)
# result = llm.invoke("Hello tell me about chat gpt 4.0")

print(result.content)