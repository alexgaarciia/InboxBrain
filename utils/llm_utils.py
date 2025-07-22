import os
import logging
from dotenv import load_dotenv
from mistralai import Mistral

# Load environment variables from .env file
load_dotenv()

def get_llm_client() -> Mistral:
    """
    Initialize and return a Mistral LLM client using the API key from environment.
    """
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        raise ValueError("MISTRAL_API_KEY is not set in environment variables.")
    return Mistral(api_key=api_key)


def call_mistral_llm(email_body: str, excel_content: str) -> str:
    """
    Call Mistral LLM with the email body and a textual summary of an Excel file.
    Returns the model's generated response.
    """
    try:
        client = get_llm_client()
        model = os.getenv("MISTRAL_MODEL", "mistral-medium")

        messages = [
            {"role": "system", "content": "You help users understand and summarize Excel files."},
            {"role": "user", "content": f"Email Body:\n{email_body}\n\nExcel Content:\n{excel_content}"}
        ]

        response = client.chat.complete(model=model, messages=messages)
        return response.choices[0].message.content.strip()

    except Exception as e:
        logging.exception("Error calling Mistral LLM: %s", e)
        return ""
