# -*- coding: utf-8 -*-
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY")
  
)

chat_model = ChatHuggingFace(llm=llm)

response = chat_model.invoke("What is the capital of India?")
   
print(response.content)