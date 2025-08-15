import pytest
from src.aws_mcp_cli.parsers.s3_parser import parse_s3_command

def test_create_bucket():
    cmd, explanation = parse_s3_command("create bucket named mybucket")
    assert "aws s3 mb s3://mybucket" in cmd
    assert "mybucket" in explanation

def test_list_buckets():
    cmd, explanation = parse_s3_command("list buckets")
    assert cmd == "aws s3 ls"
    assert "Lists all S3 buckets" in explanation

def test_unknown_s3_command():
    cmd, explanation = parse_s3_command("remove object")
    assert cmd == "aws help"
    assert "couldn't understand" in explanation.lower()
