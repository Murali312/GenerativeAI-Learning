from langchain_ollama import ChatOllama

llm = ChatOllama(model="phi3:3.8b")

response = llm.invoke("What is the current weather in Bengaluru City?")

print(response.content)