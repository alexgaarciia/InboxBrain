# Amazon SES in InboxBrain
## 1. What is Amazon SES and how is it used in this project?
Amazon SES (Simple Email Service) is a cloud-based service by AWS that enables applications and systems to send, receive, and process emails at scale.

In this project, Amazon SES is used to receive emails sent to your WorkMail address and to define how those emails are processed—specifically, by saving each incoming email as a file in S3 for further automated processing.

## 2. Verifying your domain or email address in SES
Before SES can accept emails for your WorkMail domain, you need to verify your domain (or, in some cases, individual email addresses):

Steps:
1. Go to the SES service in the AWS Console.
2. In the “Identities” section, add and verify your WorkMail domain or specific mailbox.
   - If using the free test domain from WorkMail, AWS may handle verification automatically.
   - For custom emails, you must manually add each email address as a new identity in SES and follow the verification process.
3. Wait for verification to complete before proceeding.

## 3. Creating an IAM Role for SES to write to S3
To allow Amazon SES to deliver incoming emails to your S3 bucket, you must create an IAM Role that grants SES the necessary permissions.

Steps:
1. Create the IAM Role using CloudShell (replace `<desired-role-name>` with your preferred role name (e.g., SESS3WriteRole).
```
aws iam create-role   --role-name <desired-role-name>   --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {             
          "Service": "ses.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
      }
    ]
  }'
```

2. Attach the Permissions Policy (replace `<your-bucket-name>` with your actual bucket name).
```
aws iam put-role-policy   --role-name <desired-role-name>   --policy-name <desired-policy-name>   --policy-document '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": [             
          "s3:PutObject"
        ],
        "Resource": "arn:aws:s3:::<your-bucket-name>/*"
      }
    ]
  }'
```

## 4. Creating an SES Receipt Rule to deliver emails to S3
To process incoming emails, create a receipt rule in SES:
1. In the SES Console, go to “Rule Sets” under “Mail Manager.”
2. Click “Create rule set” and give it a name (e.g., receive-email).
3. Click on the rule set you just created to open it.
4. Click "Edit".
5. Click "Create new rule".
6. Enter the rule details as follows:
<div align="center">
  <img src="https://github.com/alexgaarciia/InboxBrain/blob/main/images/ses/ses-rule-details.png" alt="Rule details – general settings" width="500"><br>
  <img src="https://github.com/alexgaarciia/InboxBrain/blob/main/images/ses/ses-s3-action.png" alt="Rule details – S3 action settings" width="500">
</div>
7. Click "Save rule set" to finish.

## 5. Next Step: Processing Emails with Lambda
After emails are delivered to your S3 bucket by SES, the next step is to [set up a Lambda function](https://github.com/alexgaarciia/InboxBrain/blob/main/docs/lambda.md) that is triggered by S3 events (e.g., file upload), so you can extract, analyze, and respond to each incoming email.

