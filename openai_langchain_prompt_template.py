from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# llm = ChatOpenAI() - by default it uses "gpt-3.5-turbo" model

llm = ChatOpenAI(model="gpt-5-nano")    # If we want a specific model to be used

response = llm.invoke("What is the capital of India")

print(response)

