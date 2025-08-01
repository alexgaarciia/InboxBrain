import os
import logging
import json
import boto3

def get_llm_client():
    """
    Initialize and return a boto3 Bedrock Runtime client.
    No API key needed; uses AWS IAM.
    """
    return boto3.client("bedrock-runtime")

def call_mistral_llm(email_body: str, excel_content: str) -> str:
    """
    Call AWS Bedrock Mistral model with the email body and Excel content.
    Returns the model's generated response.
    """
    try:
        client = get_llm_client()

        prompt = (
            f"<s>[INST] You are an assistant that summarizes tabular data from Excel files "
            f"and answers any questions users might have about them.\n\n"
            f"The user has sent the following email:\n{email_body}\n\n"
            f"The content of the Excel file (as plain text) is:\n{excel_content}\n\n"
            f"Please respond in a helpful, concise way, and ALWAYS using the user's language. [/INST]"
        )
        
        body = {
            "prompt": prompt,
            "max_tokens": 512,
            "temperature": 0.7,
            "top_p": 0.9
        }

        response = client.invoke_model(
            modelId="mistral.mixtral-8x7b-instruct-v0:1",
            contentType="application/json",
            accept="application/json",
            body=json.dumps(body)
        )

        response_body = json.loads(response['body'].read())
        return response_body["outputs"][0]["text"].strip()

    except Exception as e:
        logging.exception("Error calling AWS Bedrock Mistral model: %s", e)
        return ""
