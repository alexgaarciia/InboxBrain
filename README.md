# InboxBrain
## Project overview
This project automates the processing of incoming emails using a serverless architecture on AWS. Incoming messages are received through Amazon WorkMail and Amazon SES, temporarily stored in Amazon S3, and then routed to an AWS Lambda function that:
- Receives and parses the email content (in .eml format).
- Extracts key information such as body text, attachments, sender, subject, etc.
- Processes the attached Excel file to extract its contents.
- Sends the extracted data to a Large Language Model (LLM) with a custom prompt with the user's request.
- Sends a response email back to the sender with the generated answer.

## Why this project?
The main goal of this project is to bridge the gap between users and AI-powered tools by enabling access to LLMs through a familiar and universal interface: email.

- It allows non-technical users to interact with AI agents by simply sending an email — no apps, no APIs, no prompts.
- It makes it easier to automate administrative and operational workflows for people who may not know how to use AI directly.
- It supports more inclusive access to AI capabilities, helping democratize intelligent automation for everyday tasks.
