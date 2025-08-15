import pytest
from src.aws_mcp_cli.parsers.apigateway_parser import parse_apigateway_command

def test_create_api():
    cmd, explanation = parse_apigateway_command("create api gateway")
    assert "create-rest-api" in cmd
    assert "Creates a new API Gateway" in explanation

def test_list_apis():
    cmd, explanation = parse_apigateway_command("list apis")
    assert cmd == "aws apigateway get-rest-apis"
    assert "Lists all API Gateway REST APIs" in explanation

def test_unknown_apigateway_command():
    cmd, explanation = parse_apigateway_command("delete universe")
    assert cmd == "aws help"
    assert "couldn't understand" in explanation.lower()
