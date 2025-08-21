"""
Command Generator - NLP to AWS CLI
Phase 2: Optimized with service keywords + modular parsers
"""

# Import service-specific parsers
from aws_mcp_cli.parsers.s3_parser import parse_s3_command
from aws_mcp_cli.parsers.ec2_parser import parse_ec2_command
from aws_mcp_cli.parsers.iam_parser import parse_iam_command
from aws_mcp_cli.parsers.dynamodb_parser import parse_dynamodb_command
from aws_mcp_cli.parsers.apigateway_parser import parse_apigateway_command


# --- Service keywords for NLP detection ---
SERVICE_KEYWORDS = {
    "s3": ["s3", "bucket", "object", "storage"],
    "ec2": ["ec2", "instance", "vm", "compute", "server"],
    "iam": ["iam", "user", "role", "policy", "permission"],
    "dynamodb": ["dynamodb", "nosql", "table", "database"],
    "apigateway": ["api", "gateway", "rest api", "endpoint"],
}

# --- Map service to parser functions ---
SERVICE_PARSERS = {
    "s3": parse_s3_command,
    "ec2": parse_ec2_command,
    "iam": parse_iam_command,
    "dynamodb": parse_dynamodb_command,
    "apigateway": parse_apigateway_command,
}


def generate_command(nlp_input: str):
    """
    Convert a natural language request into an AWS CLI command.
    Returns: (command, explanation)
    """
    if not nlp_input:
        return ("aws help", "No input provided. Please enter a request like 'create s3 bucket'.")

    lowered_input = nlp_input.lower()

    # Detect service based on keywords
    for service, keywords in SERVICE_KEYWORDS.items():
        if any(keyword in lowered_input for keyword in keywords):
            parser = SERVICE_PARSERS[service]
            return parser(nlp_input)

    # --- Fallback ---
    return (
        "aws help",
        "Sorry, I couldn't determine the service. Try again with S3, EC2, IAM, DynamoDB, or API Gateway.",
    )
