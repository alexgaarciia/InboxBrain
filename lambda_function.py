import base64
import boto3
import email
from email import policy
from email.parser import BytesParser

from utils.email_utils import extract_excel, send_response_email
from utils.llm_utils import call_mistral_llm

s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # Extract SES and S3 info from the event trigger
        record = event['Records'][0]
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        # Download the raw .eml email file from S3
        response = s3.get_object(Bucket=bucket, Key=key)
        raw_email = response['Body'].read()

        # Parse the email using Python's built-in email tools
        msg = BytesParser(policy=policy.default).parsebytes(raw_email)
        sender = msg['From']
        recipient = msg['To']
        subject = msg['Subject']
        body = msg.get_body(preferencelist=('plain', 'html')).get_content()

        # Extract structured content from the Excel or CSV attachment
        excel_content = extract_excel(raw_email)

        # Use Mistral (via AWS Bedrock) to generate a reply based on the email and spreadsheet content
        llm_response = call_mistral_llm(body, excel_content)

        # Send the generated response back to the original sender via SES
        send_response_email(recipient, sender, subject, llm_response)

        return {
            'statusCode': 200,
            'body': 'Response sent successfully.'
        }

    except Exception as e:
        logger.exception("Error processing the email")
        return {
            'statusCode': 500,
            'body': f"Error: {str(e)}"
        }
