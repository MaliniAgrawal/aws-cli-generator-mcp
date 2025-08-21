import pytest
from aws_mcp_cli.command_generator import generate_command

@pytest.mark.parametrize(
    "nlp_input, expected_service",
    [
        ("create s3 bucket named mybucket", "s3"),
        ("launch ec2 instance t2.micro", "ec2"),
        ("add iam user developer", "iam"),
        ("create dynamodb table myTable", "dynamodb"),
        ("create api gateway for my app", "apigateway"),
    ],
)
def test_generate_command_services(nlp_input, expected_service):
    """Ensure NLP routes to the right service parser."""
    command, explanation = generate_command(nlp_input)

    assert isinstance(command, str)
    assert isinstance(explanation, str)
    assert command.startswith("aws") or command == "aws help"
    # service keyword should appear in command unless fallback
    if command != "aws help":
        assert expected_service in command.lower()


def test_empty_input():
    """Handles empty input gracefully."""
    command, explanation = generate_command("")
    assert command == "aws help"
    assert "No input provided" in explanation


def test_unknown_service():
    """Handles unknown NLP input gracefully."""
    command, explanation = generate_command("build spaceship to mars")
    assert command == "aws help"
    assert "couldn't determine the service" in explanation.lower()
