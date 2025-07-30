# src/aws_mcp_cli/utils/helpers.py

def format_error_response(error):
    return {
        "error": str(error),
        "type": type(error).__name__
    }, 500
