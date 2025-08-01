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

### Main Components
This project integrates several AWS services and Python modules to create a fully automated, LLM-powered email workflow:

|  | **Component**        | **Description**                                                                                                                                  |
|--|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| <img src="https://github.com/alexgaarciia/InboxBrain/blob/main/images/icons/workmail.png" width="50"> | **Amazon WorkMail**  | A secure, managed business email and calendar service that integrates with other AWS services.                                                  |
| <img src="https://github.com/alexgaarciia/InboxBrain/blob/main/images/icons/ses.png" width="50"> | **Amazon SES**       | A cloud-based email service for sending, receiving, and processing emails securely and at scale.                                                |
| <img src="https://github.com/alexgaarciia/InboxBrain/blob/main/images/icons/s3.png" width="50"> | **Amazon S3**        | An object storage service that offers industry-leading scalability, data availability, security, and performance.                               |
| <img src="https://github.com/alexgaarciia/InboxBrain/blob/main/images/icons/lambda.png" width="50"> | **AWS Lambda**       | A serverless compute service that lets you run code without provisioning or managing servers.                                                    |
| <img src="https://github.com/alexgaarciia/InboxBrain/blob/main/images/icons/sagemaker.png" width="50"> | **Amazon Bedrock**   | A fully managed service to build and scale generative AI applications using foundation models via API.                                           |

