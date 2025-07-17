import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize Azure OpenAI client
client = openai.AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

def summarize_text(text):
    # Truncate long input
    MAX_CHARS = 15000
    if len(text) > MAX_CHARS:
        text = text[:MAX_CHARS]
        text += "\n\n[Text truncated for summarization...]"

    # Attenborough-style summary prompt
    prompt = (
        "In the style of Sir David Attenborough, provide a brief, awe-inspired narration summarizing the following document. "
        "Use rich, descriptive language and a tone of curiosity and wonder:\n\n"
        f"{text}"
    )

    try:
        response = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"⚠️ An error occurred while generating the summary: {e}"
