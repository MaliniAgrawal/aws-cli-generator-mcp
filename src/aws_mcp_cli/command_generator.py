"""
command_generator.py - Core AWS CLI generator
Uses rule-based + NLP utils (with ML hooks ready).
"""

from aws_mcp_cli.utils import nlp_utils


def generate_command(nlp_input: str) -> dict:
    """Convert NLP input into AWS CLI command + explanation."""
    if not nlp_input.strip():
        return {
            "command": "aws help",
            "explanation": "No input provided. Try describing an AWS task."
        }

    text = nlp_input.lower()

    # --- Extract entities
    region = nlp_utils.extract_region(text) or "us-east-1"
    name = nlp_utils.extract_name(text)

    # --- ML hook (future)
    ml_intent = nlp_utils.detect_intent_ml(text)
    if ml_intent:
        # (for Phase-3.5, not now)
        pass

    # --- Rule-based services
    if "s3" in text and "bucket" in text:
        cmd = f"aws s3 mb s3://{name}" if name else "aws s3 ls"
        return {
            "command": cmd,
            "explanation": "Creates or lists S3 buckets."
        }

    if "ec2" in text and "instance" in text:
        cmd = f"aws ec2 run-instances --instance-type t2.micro --image-id ami-123456"
        if region:
            cmd += f" --region {region}"
        return {
            "command": cmd,
            "explanation": "Launches an EC2 instance."
        }

    if "iam" in text and "user" in text:
        cmd = f"aws iam create-user --user-name {name}" if name else "aws iam list-users"
        return {
            "command": cmd,
            "explanation": "Creates or lists IAM users."
        }

    if "lambda" in text:
        cmd = f"aws lambda create-function --function-name {name} --runtime python3.9 --role arn:aws:iam::123456789012:role/execution_role --handler lambda_function.lambda_handler --zip-file fileb://function.zip"
        if region:
            cmd += f" --region {region}"
        return {
            "command": cmd,
            "explanation": "Creates a new AWS Lambda function."
        }

    if "dynamodb" in text and "table" in text:
        cmd = f"aws dynamodb create-table --table-name {name} --attribute-definitions AttributeName=Id,AttributeType=S --key-schema AttributeName=Id,KeyType=HASH --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5"
        if region:
            cmd += f" --region {region}"
        return {
            "command": cmd,
            "explanation": "Creates a DynamoDB table."
        }

    # API Gateway (REST vs HTTP API) - Improved Logic
    is_http_api = "http api" in text or "http-api" in text or "httpapi" in text
    is_rest_api = "rest api" in text or "api gateway" in text or "apigateway" in text

    if is_http_api:
        cmd = f"aws apigatewayv2 create-api --name {name or 'MyApi'} --protocol-type HTTP"
        explanation = "Creates an API Gateway HTTP API."
        if region:
            cmd += f" --region {region}"
        return {
            "command": cmd,
            "explanation": explanation
        }
    elif is_rest_api:
        cmd = f"aws apigateway create-rest-api --name {name or 'MyApi'}"
        explanation = "Creates an API Gateway REST API."
        if region:
            cmd += f" --region {region}"
        return {
            "command": cmd,
            "explanation": explanation
        }

    if "rds" in text and ("instance" in text or "db" in text):
        cmd = f"aws rds create-db-instance --db-instance-identifier {name or 'mydb'} --db-instance-class db.t3.micro --engine mysql --allocated-storage 20"
        if region:
            cmd += f" --region {region}"
        return {
            "command": cmd,
            "explanation": "Creates a new RDS database instance."
        }

    if "sqs" in text and "queue" in text:
        cmd = f"aws sqs create-queue --queue-name {name or 'MyQueue'}"
        if region:
            cmd += f" --region {region}"
        return {
            "command": cmd,
            "explanation": "Creates an SQS queue."
        }

    if "sns" in text and "topic" in text:
        cmd = f"aws sns create-topic --name {name or 'MyTopic'}"
        if region:
            cmd += f" --region {region}"
        return {
            "command": cmd,
            "explanation": "Creates an SNS topic."
        }

    if "cloudwatch" in text and "alarm" in text:
        cmd = f"aws cloudwatch put-metric-alarm --alarm-name {name or 'MyAlarm'} --metric-name CPUUtilization --namespace AWS/EC2 --statistic Average --period 300 --threshold 80 --comparison-operator GreaterThanThreshold --evaluation-periods 2 --alarm-actions arn:aws:sns:123456789012:MyTopic"
        if region:
            cmd += f" --region {region}"
        return {
            "command": cmd,
            "explanation": "Creates a CloudWatch alarm."
        }

    # --- Default fallback
    return {
        "command": "aws help",
        "explanation": "Couldn't determine the service. Try: 'aws [service] [action]'."
    }
