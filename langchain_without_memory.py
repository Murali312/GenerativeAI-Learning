# langchain_without_memory.py
#
# This script demonstrates a simple use of LangChain with the Ollama LLM (phi3:3.8b) for stateless conversation.
# It shows that the model does not remember previous interactions (no memory).

from langchain_ollama import ChatOllama

# Initialize the Ollama LLM with the phi3:3.8b model
llm = ChatOllama(model="phi3:3.8b")

# First prompt: introduce yourself to the model
response = llm.invoke("Hi, My name is John.")

# Print the model's response to the introduction
print(response.content)

# Second prompt: ask the model to recall your name
response2 = llm.invoke("What is my name?")

# Print the model's response to the recall question
print(response2.content)