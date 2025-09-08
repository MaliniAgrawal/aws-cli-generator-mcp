import os
import uuid
import boto3
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from mangum import Mangum
from aws_mcp_cli.command_generator import generate_command


# Serve static frontend from ../web
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WEB_DIR = os.path.join(BASE_DIR, "..", "web")

app = Flask(__name__, static_folder=WEB_DIR, static_url_path="")
CORS(app)
# ---- Frontend Routes ----
@app.route("/")
def index():
    return send_from_directory(WEB_DIR, "index.html")

# DynamoDB setup (only if running in AWS)
dynamodb = None
table = None
TABLE_NAME = os.getenv("MCP_LOGS_TABLE")

if TABLE_NAME:
    try:
        dynamodb = boto3.resource("dynamodb", region_name=os.getenv("AWS_REGION", "us-east-1"))
        table = dynamodb.Table(TABLE_NAME)
    except Exception as e:
        print(f"[WARN] Could not initialize DynamoDB: {e}")


@app.route("/health", methods=["GET"])
def health_check():
    """Simple health endpoint."""
    return jsonify({"status": "ok"}), 200


@app.route("/generate", methods=["POST"])
def generate():
    """Generate AWS CLI command from NLP input and log to DynamoDB."""
    try:
        data = request.get_json(force=True)
        user_input = data.get("input", "").strip()

        result = generate_command(user_input)

        # Log to DynamoDB
        if table:
            log_item = {
                "RequestId": str(uuid.uuid4()),
                "UserInput": user_input,
                "Command": result.get("command", ""),
                "Explanation": result.get("explanation", ""),
            }
            try:
                table.put_item(Item=log_item)
            except Exception as e:
                print(f"[WARN] Failed to log to DynamoDB: {e}")

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# For AWS Lambda
handler = Mangum(app)

# For local dev (python src/aws_mcp_cli/mcp_server.py)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
