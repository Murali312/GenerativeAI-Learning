# ! pip install openai

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI()  


response = client.responses.create(
    model="gpt-5-nano",
    input="Write three lines about IT industry in India."
)

print(response.output_text)