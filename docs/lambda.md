# AWS Lambda in InboxBrain
## 1. What is AWS Lambda and how is it used in this project?
AWS Lambda is a serverless compute service that lets you run code in response to events without provisioning or managing servers.

In this project, Lambda is used to process every new email file (`.eml`) stored in your S3 bucket. The Lambda function extracts the email content, interacts with a Large Language Model (LLM) via Amazon Bedrock, generates a response, and sends it back via email.

## 2. Creating the Lambda function
Steps:
1. Go to the AWS Lambda console and click “Create function.”
2. Choose “Author from scratch.”
3. Enter a function name.
4. Choose the runtime (e.g., Python 3.11 or the version you are using).
5. Click “Create function.”

Once the function is created, you can either:
1. Use the code provided in this repository, adapting it as needed for your workflow,
2. Write your own logic from scratch to process and respond to incoming emails (check out [this link](https://github.com/alexgaarciia/InboxBrain/blob/main/docs/bedrock.md) if you plan on using Amazon Bedrock)

**Important: Every time you make changes to the Lambda code, you must click “Deploy” in the AWS Lambda console for your changes to take effect.**

## 3. Granting Lambda Permission to Read from S3
By default, your Lambda function cannot access S3 buckets. You must attach a policy to its execution role that allows reading email files.

Steps:
1. Identify the Lambda execution role assigned to your function (you can find this in the Lambda configuration page).
<div align="center">
  <img src="https://github.com/alexgaarciia/InboxBrain/blob/main/images/lambda/lambda-execution-rule.png" alt="Lambda execution rule" width="500"><br>
</div>

2. Open AWS CloudShell.
3. Run the following command, replacing `<lambda-execution-role-name>` with your actual Lambda role name, `<your-bucket-name>` with your bucket name, and `<desired-policy-name> with a name you want to use for the policy:
```
aws iam put-role-policy \
  --role-name <lambda-execution-role-name> \
  --policy-name <desired-policy-name> \
  --policy-document '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": ["s3:GetObject"],
        "Resource": "arn:aws:s3:::<your-bucket-name>/*"
      }
    ]
  }'
```

## 4. Configuring the S3 Event Trigger
Once your Lambda function is created and has the necessary permissions, you need to return to your S3 bucket to complete the integration.

By setting up an event trigger in S3, you ensure that every time a new `.eml` file is uploaded (i.e., every time SES delivers an email), your Lambda function will be invoked automatically to process the message.

Steps:
1. In the S3 Console, go to your bucket.
2. Under the “Properties” tab, scroll to “Event notifications.”
3. Click “Create event notification.”
4. Configure:
   - Event name: _as desired_
   - Event type: PUT
   - Destination: Lambda function (specify Lambda function from your Lambda functions)

5. Save changes.

Now, every time a new .eml file is added to the bucket, your Lambda function will be triggered automatically.

