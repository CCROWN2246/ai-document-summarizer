import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load environment variables from .env file
load_dotenv()

# Get config from environment with default values (Option 1)
api_key = os.getenv("AZURE_OPENAI_API_KEY", "")
api_version = os.getenv("AZURE_OPENAI_API_VERSION", "")
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT", "")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "")

# Initialize AzureOpenAI client
client = AzureOpenAI(
    api_key=api_key,
    api_version=api_version,
    azure_endpoint=azure_endpoint,
)

# Test the connection
try:
    response = client.chat.completions.create(
        model=deployment,
        messages=[{"role": "user", "content": "Ahoy! Speak like a pirate."}],
        temperature=0.7
    )
    print("\n SUCCESS:")
    print(response.choices[0].message.content)
except Exception as e:
    print("\n Connection failed:", e)
