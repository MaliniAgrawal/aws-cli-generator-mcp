import pytest
from src.aws_mcp_cli.parsers.ec2_parser import parse_ec2_command

def test_start_instance():
    cmd, explanation = parse_ec2_command("start ec2 instance")
    assert "start-instances" in cmd
    assert "Starts" in explanation

def test_stop_instance():
    cmd, explanation = parse_ec2_command("stop ec2 instance")
    assert "stop-instances" in cmd
    assert "Stops" in explanation

def test_describe_instances():
    cmd, explanation = parse_ec2_command("describe instances")
    assert cmd == "aws ec2 describe-instances"
    assert "Describes all EC2 instances" in explanation

def test_unknown_ec2_command():
    cmd, explanation = parse_ec2_command("launch rockets")
    assert cmd == "aws help"
    assert "couldn't understand" in explanation.lower()
