# ---------------------------
# API Gateway REST/HTTP tests
# ---------------------------
import aws_mcp_cli.command_generator as generator

def test_apigateway_rest_with_name():
    """REST API with explicit name"""
    result = generator.generate_command("create rest api name myapi in us-east-1")
    assert "apigateway create-rest-api" in result["command"]
    assert "--name myapi" in result["command"]
    assert "--region us-east-1" in result["command"]
    assert "rest api" in result["explanation"].lower()

def test_apigateway_rest_without_name():
    """REST API without explicit 'name' keyword"""
    result = generator.generate_command("create rest api myapi in us-west-2")
    assert "apigateway create-rest-api" in result["command"]
    assert "--name myapi" in result["command"]
    assert "--region us-west-2" in result["command"]

def test_apigateway_http_with_name():
    """HTTP API with explicit name"""
    result = generator.generate_command("create http api name http-one in us-east-2")
    assert "apigatewayv2 create-api" in result["command"]
    assert "--name http-one" in result["command"]
    assert "--region us-east-2" in result["command"]
    assert "http api" in result["explanation"].lower()

def test_apigateway_http_without_name():
    """HTTP API without 'name' keyword"""
    result = generator.generate_command("create http api http-two in us-west-1")
    assert "apigatewayv2 create-api" in result["command"]
    assert "--name http-two" in result["command"]
    assert "--region us-west-1" in result["command"]
import pytest
from aws_mcp_cli.command_generator import generate_command

# ---------------------------
# Parametrized service tests
# ---------------------------
@pytest.mark.parametrize("nlp_input,expected_service", [
    ("create s3 bucket named mybucket", "s3"),
    ("launch ec2 instance t2.micro", "ec2"),
    ("add iam user developer", "iam"),
    ("create lambda function myfunc", "lambda"),
    ("create dynamodb table mytable", "dynamodb"),
    ("create rest api name myapi", "apigateway"),
    ("create http api name http api", "apigateway"),
    ("create rds instance mydb", "rds"),
    ("create sqs queue jobqueue", "sqs"),
    ("create sns topic mytopic", "sns"),
    ("create cloudwatch alarm highcpu", "cloudwatch"),
])
def test_generate_command_services(nlp_input, expected_service):
    """Tests CLI generation for multiple AWS services."""
    result = generate_command(nlp_input)
    assert "aws" in result["command"]
    assert expected_service in result["command"].lower()


# ---------------------------
# Region detection
# ---------------------------
@pytest.mark.parametrize("nlp_input,expected_region", [
    ("create ec2 instance in us east 1", "us-east-1"),
    ("create s3 bucket in oregon", "us-west-2"),
    ("create lambda function in tokyo", "ap-northeast-1"),
    ("create dynamodb table in frankfurt", "eu-central-1"),
])
def test_region_detection(nlp_input, expected_region):
    """Checks if regions are correctly detected and included."""
    result = generate_command(nlp_input)
    assert expected_region in result["command"]


# ---------------------------
# Edge cases
# ---------------------------
def test_empty_input():
    """Handles empty input gracefully."""
    result = generate_command("")
    assert result["command"] == "aws help"
    assert "no input provided" in result["explanation"].lower()

def test_unknown_service():
    """Handles unknown NLP input gracefully."""
    result = generate_command("build spaceship to mars")
    assert result["command"] == "aws help"
    assert "couldn't determine" in result["explanation"].lower()
