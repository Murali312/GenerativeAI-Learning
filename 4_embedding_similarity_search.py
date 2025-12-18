from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

# Load environment variables from a .env file
load_dotenv()

# Initialize OpenAI Embeddings with the specified model
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

text="Delhi is the capital of India."

# Example usage: Embed sample documents
documents = [
    "The Eiffel Tower is located in Paris.",
    "The Great Wall of China is visible from space.",
    "Mount Everest is the highest mountain in the world."
]

query = "Where does Eiffel Tower located?"

# result_text = embeddings.embed_query(text)
# print(str(result_text))

result_docs = embeddings.embed_documents(documents)

query_embedding =  embeddings.embed_query(query)

similarity_score =  cosine_similarity([query_embedding], [result_docs])

# Print the resulting embeddings
print("Query:", query)
print("Similarity Scores:", similarity_score)
print("Most similar document:", documents[similarity_score.argmax()])
print("Most similar document score:", similarity_score.max())