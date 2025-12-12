
# Import required modules from LangChain and Ollama integration
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory



# Initialize the Ollama chat model with the specified model name
model = ChatOllama(model="llama3.2:3b")


# Define a prompt template that includes chat history and user input
prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}"),
])


# Create a runnable chain by piping the prompt to the model (LangChain Expression Language)
runnable = prompt | model # LCEL


# Dictionary to store chat histories for different sessions
history_store = {}


# Function to get or create chat history for a session
def get_session_history(session_id):
    if session_id not in history_store:
        history_store[session_id] = InMemoryChatMessageHistory()
    return history_store[session_id]


# Create a chain that maintains message history for each session
chain = RunnableWithMessageHistory(
    runnable = runnable,
    get_session_history = get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)


# Invoke the chain with the first user input and store the response
response1 = chain.invoke(
    {"input": "Hi, My name is Raj"},
    config ={ "session_id":"session_1"}
)

# Invoke the chain with a follow-up question in the same session
response2 = chain.invoke(
    {"input": "What is my name?"},
    config ={ "session_id":"session_1"}
)

# Print the responses from the model
print(response1.content)
print(response2.content)

