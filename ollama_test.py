#LANGCHAIN_API_KEY="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"
#OPENAI_API_KEY="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"
#LANGCHAIN_PROJECT="JAHIDBPROFILE"

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_community.chat_models import ChatOllama
import streamlit as st
import os 
## environ varable calling
from dotenv import load_dotenv
load_dotenv()
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

prompts = ChatPromptTemplate.from_messages(
    [
        ("system","you are helpful , please "),
        ("user","Question{question}")
    ]
)



st.title("Langchain demo with Ollama ")
input_text = st.text_input("Search whatever you want")
##call openai
llm = ChatOllama (model= "llama3.2:1b")

outputparser = StrOutputParser()
chain = prompts | llm | outputparser

if input_text :
    st.write(chain.invoke({'question':input_text}))



