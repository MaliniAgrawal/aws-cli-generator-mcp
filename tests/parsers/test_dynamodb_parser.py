import pytest
from src.aws_mcp_cli.parsers.dynamodb_parser import parse_dynamodb_command

def test_create_table():
    cmd, explanation = parse_dynamodb_command("create dynamodb table")
    assert "create-table" in cmd
    assert "Creates a DynamoDB table" in explanation

def test_list_tables():
    cmd, explanation = parse_dynamodb_command("list tables")
    assert cmd == "aws dynamodb list-tables"
    assert "Lists all DynamoDB tables" in explanation

def test_unknown_dynamodb_command():
    cmd, explanation = parse_dynamodb_command("drop database")
    assert cmd == "aws help"
    assert "couldn't understand" in explanation.lower()
