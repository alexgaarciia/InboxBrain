import boto3
from email import policy
from email.parser import BytesParser
from utils.email_utils import send_response_email, extract_excel

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Get bucket and object key from the incoming SES+S3 event
    record = event['Records'][0]
    bucket = record['s3']['bucket']['name']
    key = record['s3']['object']['key']

    # Retrieve the raw .eml file from S3
    response = s3.get_object(Bucket=bucket, Key=key)
    raw_email = response['Body'].read()

    # Parse the email using the default policy
    msg = BytesParser(policy=policy.default).parsebytes(raw_email)

    # Extract sender, recipient, and subject headers
    sender = msg['From']
    recipient = msg['To']
    subject = msg['Subject']

    # Extract Excel or CSV content from the email
    excel_content = extract_excel(raw_email)

    # Send automatic response to the sender
    send_response_email(from_address=recipient, to_address=sender, subject=subject)

    # Print Excel content to CloudWatch logs
    print(excel_content)

    return { "statusCode": 200, "body": "Email processed and reply sent" }
