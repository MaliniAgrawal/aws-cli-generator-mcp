# src/aws_mcp_cli/mcp_server.py

from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
import os
from aws_mcp_cli.command_generator import generate_command

app = Flask(
    __name__,
    static_folder="../web",  # Serve static assets from web/
    template_folder="../web"  # HTML in same folder for simplicity
)

CORS(app)

@app.route("/")
def index():
    return send_from_directory(app.template_folder, "index.html")

@app.route("/<path:filename>")
def serve_static(filename):
    """Serve CSS, JS, favicon, etc."""
    return send_from_directory(app.static_folder, filename)

@app.route("/mcp/generate-cli", methods=["POST"])
def generate_cli():
    try:
        data = request.get_json()
        if not data or "input" not in data:
            return jsonify({"error": "Missing 'input' field"}), 400

        cli_command, explanation = generate_command(data["input"])
        return jsonify({
            "command": cli_command,
            "explanation": explanation
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
