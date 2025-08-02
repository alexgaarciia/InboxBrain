## Important Note: Why We Don’t Use Direct WorkMail → Lambda Integration
Initial idea:
AWS allows you to configure an “Inbound Mail Flow Rule” in WorkMail that can directly invoke a Lambda function upon email reception.

Limitation:
When using this method, the event received by Lambda only contains basic metadata (sender, subject, etc.) but not the actual email body or attachments.
This makes it impossible to extract and analyze the message content programmatically.

Solution:
We switched to a more robust, production-ready architecture using SES and S3 as intermediaries.
