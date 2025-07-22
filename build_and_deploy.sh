#!/bin/bash

set -e  # Stop the script immediately if any command fails

# Name of AWS Lambda function
LAMBDA_FUNCTION_NAME="autoResponderWorkmail"

echo "Cleaning previous build..."
rm -rf lambda_build lambda_package.zip
mkdir lambda_build

echo "Copying source code..."
cp lambda_function.py lambda_build/
cp -r utils lambda_build/

echo "Creating deployment package with PowerShell..."
powershell.exe -Command "Compress-Archive -Path lambda_build\* -DestinationPath lambda_package.zip -Force"

echo "Uploading to AWS Lambda..."
aws lambda update-function-code \
  --function-name "$LAMBDA_FUNCTION_NAME" \
  --zip-file fileb://lambda_package.zip

echo "Deployment completed successfully."
