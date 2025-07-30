# src/aws_mcp_cli/mcp_server.py
import sys
import os
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from flask import Flask, request, jsonify
from mangum import Mangum

from aws_mcp_cli.command_generator import generate_command
from aws_mcp_cli.validators import validate_input
from aws_mcp_cli.utils.helpers import format_error_response

# Initialize Flask app
app = Flask(__name__)

@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "ok", "message": "MCP AWS CLI Generator is running"}), 200

@app.route("/mcp/generate-cli", methods=["POST"])
def generate_cli():
    try:
        # Expecting JSON with {"input": "<natural language text>"}
        data = request.get_json(force=True)
        user_input = data.get("input", "")

        if not user_input.strip():
            return jsonify({"error": "Input cannot be empty."}), 400

        # Step 1: Validate input (optional, can expand later)
        is_valid, error = validate_input(user_input)
        if not is_valid:
            return jsonify({"error": error}), 400

        # Step 2: Generate CLI command
        cli_command, explanation = generate_command(user_input)

        return jsonify({
            "command": cli_command,
            "explanation": explanation
        }), 200

    except Exception as e:
        return format_error_response(e)

# For AWS Lambda support (via Mangum)
handler = Mangum(app)
# ...existing code...

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
