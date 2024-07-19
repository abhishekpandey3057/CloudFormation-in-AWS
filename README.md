**AWS CloudFormation Template for Serverless CRUD Application**

This repository contains a CloudFormation template (template.yaml) and a Python-based Lambda function (index.py) for setting up a serverless CRUD (Create, Read, Update, Delete) application on AWS. The template automates the creation of AWS Lambda functions, API Gateway endpoints, IAM roles, and DynamoDB tables necessary for managing student records.

**Features: **

Lambda Function: Executes CRUD operations on DynamoDB via API Gateway.

API Gateway: Provides endpoints for interacting with student records.

IAM Roles: Manages permissions for Lambda functions to interact with other AWS services.

DynamoDB Table: Stores student information including StudentID, StudentName, and Department.


**Usage:**

Setup: Upload the index.py Lambda function to an S3 bucket.

Configuration: Customize template.yaml to specify your AWS region, S3 bucket name, and AWS account ID.

Deployment: Use AWS CloudFormation to deploy the stack defined in template.yaml.

Testing: Utilize POSTMAN to perform CRUD operations (Create, Read, Update, Delete) on student records via the generated API Gateway endpoints.

**Repository Structure:**

index.py: Lambda function code for CRUD operations on DynamoDB.

template.yaml: CloudFormation template defining Lambda, API Gateway, IAM roles, and DynamoDB resources.

Documentation: Detailed instructions on setting up and deploying the CloudFormation stack.

**Follow the comprehensive guide in the README.md to seamlessly deploy and manage the serverless application for managing student records on AWS.**
