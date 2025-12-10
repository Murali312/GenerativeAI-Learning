from langchain_aws import ChatBedrockConverse
from langchain_core.prompts import PromptTemplate
from dotenv import load_env

load_dotenv()

llm = ChatBedrockConverse(
    model_id="amazon.titan-text-express-v1",
    region_name="ap-south-1"
)

