from typing import Tuple
from aws_mcp_cli.utils.nlp_utils import normalize, detect_intent
from aws_mcp_cli.parsers.s3_parser import parse_s3_command
from aws_mcp_cli.parsers.ec2_parser import parse_ec2_command
from aws_mcp_cli.parsers.iam_parser import parse_iam_command
from aws_mcp_cli.parsers.dynamodb_parser import parse_dynamodb_command
from aws_mcp_cli.parsers.apigateway_parser import parse_apigateway_command

def generate_command(nlp_input: str) -> Tuple[str, str]:
    """
    Core dispatcher: detect service + action loosely, then defer to the service parser.
    """
    t = normalize(nlp_input)
    service, action = detect_intent(t)

    # pass-through to the right parser; each parser still does its own flexible logic
    if service == "s3":
        return parse_s3_command(t)
    if service == "ec2":
        return parse_ec2_command(t)
    if service == "iam":
        return parse_iam_command(t)
    if service == "dynamodb":
        return parse_dynamodb_command(t)
    if service == "apigateway":
        return parse_apigateway_command(t)

    # if we couldn't detect service, try a best-effort sweep
    for parser in (parse_s3_command, parse_ec2_command, parse_iam_command, parse_dynamodb_command, parse_apigateway_command):
        cmd, expl = parser(t)
        if cmd != "aws help":
            return cmd, expl

    return "aws help", "I couldn’t detect the AWS service. Try including words like S3, EC2, IAM, DynamoDB, or API."
