import boto3
import email.utils

ses = boto3.client('ses')

def send_response_email(from_address, to_address, subject):
    # Clean name in case it is in the format "Name <name@example.com>"
    real_email = email.utils.parseaddr(to_address)[1]

    if not real_email:
        print("Invalid address, response not sent.")
        return
    
    subject_line = f"Re: {subject}" if subject else "Re: your email"

    response = ses.send_email(
        Source=from_address,
        Destination={"ToAddresses": [real_email]},
        Message={
            "Subject": {"Data": subject_line},
            "Body": {
                "Text": {
                    "Data": "Dear user, I have successfully received your answer",
                    "Charset": "UTF-8"
                }
            }
        }
    )
    print(f"Response sent to {real_email}")
