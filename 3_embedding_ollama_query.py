from langchain_ollama import OllamaEmbeddings
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Initialize OpenAI Embeddings with the specified model
embeddings = OllamaEmbeddings(model="granite-embedding:latest")

# Example usage: Embed sample documents
result = embeddings.embed_query("Delhi is the capital of India.")

# Print the resulting embeddings
print(str(result))