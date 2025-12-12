from langchain_openai import AzureChatOpenAI

from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv

# Need to setup a AZURE_OPENAI_API_KEY and AZURE_OPENAI_ENDPOINT in a .env file. 
# These AZURE_OPENAI_API_KEY and AZURE_OPENAI_ENDPOINT should get from your Azure OpenAI resource in Azure Portal.
load_dotenv() # Load environment variables from .env file

# Initialize the Azure OpenAI chat model with the specified deployment name
llm = AzureChatOpenAI(
    deployment_name="gpt-5-nano",
    model_name="gpt-5-nano",
    azure_api_version="2024-12-01-preview",
)

prompt = PromptTemplate.from_template(
    "What is the capital of {country}?"
)

chain = prompt | llm  # LCEL

response = chain.invoke(
    {"country": "France"}
)

print(response.content) 