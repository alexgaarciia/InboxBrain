import pandas as pd
import io
import boto3
import email
from email import policy
from email.parser import BytesParser

ses = boto3.client('ses')

def send_response_email(from_address, to_address, subject):
    """
    Sends a confirmation email using AWS SES in reply to a received message.

    Args:
        from_address (str): Email address of your system.
        to_address (str): Email address of the original sender.
        subject (str): Subject of the original email.
    """
    # Extract the actual email address (e.g., from "Name <email@example.com>")
    real_email = email.utils.parseaddr(to_address)[1]

    if not real_email:
        return  # Skip if address is invalid

    # Build the subject line for the response
    subject_line = f"Re: {subject}" if subject else "Re: your email"

    # Send the email via AWS SES
    ses.send_email(
        Source=from_address,
        Destination={"ToAddresses": [real_email]},
        Message={
            "Subject": {"Data": subject_line},
            "Body": {
                "Text": {
                    "Data": "Dear user, I have successfully received your email.",
                    "Charset": "UTF-8"
                }
            }
        }
    )

def extract_excel(raw_email):
    """
    Parses a raw email and extracts content from any attached Excel or CSV files.

    Supported formats:
    - .xlsx
    - .xls
    - .csv

    Returns:
        A single string containing file names, column headers, and full tabular content.
        If no valid files are found, returns a default message.
    """
    msg = BytesParser(policy=policy.default).parsebytes(raw_email)
    contents = []

    for part in msg.walk():
        filename = part.get_filename()
        if not filename:
            continue

        filename = filename.lower()
        if filename.endswith(('.xlsx', '.xls', '.csv')):
            try:
                file_bytes = part.get_content()
                if filename.endswith('.csv'):
                    df = pd.read_csv(io.BytesIO(file_bytes))
                else:
                    df = pd.read_excel(
                        io.BytesIO(file_bytes),
                        engine='openpyxl' if filename.endswith('.xlsx') else None
                    )
                columns = ", ".join(df.columns)
                content = df.to_string(index=False)
                contents.append(f"File: {filename}\nColumns: {columns}\nContent:\n{content}")
            except Exception as e:
                contents.append(f"Error reading file {filename}: {str(e)}")

    if not contents:
        return "No Excel or CSV files were found in the email."

    return "\n\n---\n\n".join(contents)
