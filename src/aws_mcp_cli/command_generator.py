# src/aws_mcp_cli/command_generator.py

from aws_mcp_cli.parsers.s3_parser import parse_s3_command
from aws_mcp_cli.parsers.ec2_parser import parse_ec2_command
from aws_mcp_cli.parsers.iam_parser import parse_iam_command
from aws_mcp_cli.parsers.dynamodb_parser import parse_dynamodb_command
from aws_mcp_cli.parsers.apigateway_parser import parse_apigateway_command

def generate_command(user_input: str):
    lowered = user_input.lower()

    if "s3" in lowered:
        return parse_s3_command(user_input)
    elif "ec2" in lowered:
        return parse_ec2_command(user_input)
    elif "iam" in lowered or "user" in lowered or "role" in lowered:
        return parse_iam_command(user_input)
    elif "dynamodb" in lowered:
        return parse_dynamodb_command(user_input)
    elif "api gateway" in lowered or "apigateway" in lowered:
        return parse_apigateway_command(user_input)
    else:
        return ("aws help", "Sorry, I couldn't understand that. Showing AWS help.")
