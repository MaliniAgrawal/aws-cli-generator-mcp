# src/aws_mcp_cli/validators.py

def validate_input(user_input: str):
    if len(user_input.strip()) < 5:
        return False, "Input too short."
    return True, ""
