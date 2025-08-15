import pytest
from src.aws_mcp_cli.parsers.iam_parser import parse_iam_command

def test_create_user():
    cmd, explanation = parse_iam_command("create user named alice")
    assert "--user-name alice" in cmd
    assert "alice" in explanation

def test_list_users():
    cmd, explanation = parse_iam_command("list users")
    assert cmd == "aws iam list-users"
    assert "Lists all IAM users" in explanation

def test_unknown_iam_command():
    cmd, explanation = parse_iam_command("grant magic powers")
    assert cmd == "aws help"
    assert "couldn't understand" in explanation.lower()
