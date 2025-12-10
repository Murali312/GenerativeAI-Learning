import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("GOOGLE_API_KEY"))

# Configure with your API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create a model instance
model = genai.GenerativeModel("gemini-2.5-flash")

# Generate a simple response
response = model.generate_content("What is the capital of India")

# Print the output
print(response.text)