import boto3
import email
from email import policy
from email.parser import BytesParser
from email_utils import send_response_email

s3 = boto3.client('s3')

def lambda_handler(event, context):
    record = event['Records'][0]
    bucket = record['s3']['bucket']['name']
    key = record['s3']['object']['key']

    response = s3.get_object(Bucket=bucket, Key=key)
    raw_email = response['Body'].read()
    msg = BytesParser(policy=policy.default).parsebytes(raw_email)

    sender = msg['From']
    recipient = msg['To']
    subject = msg['Subject']

    # Extract body
    text_body = None
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == 'text/plain':
                text_body = part.get_content()
                break
    else:
        text_body = msg.get_content()

    print("== EMAIL RECEIVED ==")
    print("From:", sender)
    print("To:", recipient)
    print("Subject:", subject)
    print("Text body (preview):", text_body[:500] if text_body else "[None]")
    print("====================")

    # Send response
    send_response_email(recipient, sender, subject)

    return { "statusCode": 200, "body": "Email processed and reply sent" }
