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
| <img src="https://github.com/alexgaarciia/InboxBrain/blob/main/images/icons/workmail.png" width="20"> | **Amazon WorkMail**  | Hosted email service that receives user emails at `assistant@inboxbrain.awsapps.com` and integrates with SES for automatic routing.              |
| <img src="https://github.com/alexgaarciia/InboxBrain/blob/main/images/icons/ses.png" width="20"> | **Amazon SES**       | Cloud-based email service used to receive emails and route them to S3. It applies receipt rules and policies to manage incoming messages.         |
| <img src="https://github.com/alexgaarciia/InboxBrain/blob/main/images/icons/s3.png" width="20"> | **Amazon S3**        | Object storage service used to store the full `.eml` files of received emails. Triggers the Lambda function on new uploads.                      |
| <img src="https://github.com/alexgaarciia/InboxBrain/blob/main/images/icons/lambda.png" width="20"> | **AWS Lambda**       | Serverless compute service that parses `.eml` files, extracts Excel data, queries the LLM, and sends the response email.                          |
| <img src="https://github.com/alexgaarciia/InboxBrain/blob/main/images/icons/sagemaker.png" width="20"> | **Amazon Bedrock**   | Fully managed service to access foundation models (LLMs). It receives structured Excel data and generates human-like responses.                    |
