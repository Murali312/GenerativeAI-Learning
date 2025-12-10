from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

model = ChatOllama(model="llama3.2:3b")

prompt = PromptTemplate.from_template("Tell me the key achievements of {name} in 4 bullet points.")

chain = prompt | model #LCEL -> LangChain Expression Language

response = chain.invoke({"name" : "Virat Kohli"})

print(response.content)