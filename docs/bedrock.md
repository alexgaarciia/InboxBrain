If you plan on using Amazon Bedrock, you need to perform two essential steps to ensure your Lambda function can access Bedrock:

### 1. Request access to specific models in Bedrock
Amazon Bedrock requires you to explicitly request access to each foundation model you want to use. To do this:

1. Open the Amazon Bedrock Console
2. Go to "Model access" in the left-hand menu
3. Click on "Modify model access"
4. Enable access for the specific models you intend to use 
5. Wait for the access request to be approved (usually takes a few minutes)

### 2. Grant Lambda permission to invoke Bedrock (via CloudShell)
   
Once model access is granted, open CloudShell and run this command (adjusting your Lambda role name):

```
aws iam put-role-policy \
  --role-name <your-lambda-execution-role-name> \
  --policy-name AllowBedrockInvokeModel \
  --policy-document '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": ["bedrock:InvokeModel"],
        "Resource": "*"
      }
    ]
  }'
```
