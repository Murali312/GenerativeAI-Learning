# Import necessary libraries
from langchain_aws import ChatBedrockConverse
from langchain_core.prompts import PromptTemplate
from dotenv import load_env

# Get AWS credentials like access key, secret key, and region from AWS portal and set them in a .env file
# Load environment variables from a .env file (for AWS credentials and config)
load_dotenv()

# Initialize the Bedrock LLM with the specified model and AWS region
llm = ChatBedrockConverse(
    model_id="amazon.titan-text-express-v1",
    region_name="ap-south-1"
)

# Create a prompt template for the question
prompt = PromptTemplate.from_template(
    "What is the capital of {country}?"
)

# Combine the prompt and LLM into a chain
chain = prompt | llm

# Invoke the chain with a specific input
response = chain.invoke({"country": "India"})

# Print the response from the LLM
print(response.content)

