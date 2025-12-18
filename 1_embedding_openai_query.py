from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Initialize OpenAI Embeddings with the specified model
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

# Example usage: Embed sample documents
result = embeddings.embed_query("Delhi is the capital of India.")

# Print the resulting embeddings
print(str(result))