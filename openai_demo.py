# ! pip install openai

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI()  

# client = OpenAI(api_key=os.getenv("TEST_API_KEY"))     -   If we change name of the key i.e., "OPENAI_API_KEY" with some other name (here - "TEST_API_KEY")


response = client.responses.create(
    model="gpt-5-nano",
    input="Write three lines about IT industry in India."
)

print(response.output_text)