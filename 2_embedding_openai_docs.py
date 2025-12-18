from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Initialize OpenAI Embeddings with the specified model
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

# Example usage: Embed sample documents
documents = [
    "The Eiffel Tower is located in Paris.",
    "The Great Wall of China is visible from space.",
    "Mount Everest is the highest mountain in the world."
]

result = embeddings.embed_documents(documents)

# Print the resulting embeddings
print(str(result))