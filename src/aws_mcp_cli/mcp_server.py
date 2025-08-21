"""
AWS CLI Generator - Flask + Mangum
Phase 2: SAM/Lambda Ready
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from mangum import Mangum
import os
from aws_mcp_cli.command_generator import generate_command

# --- Flask app ---
app = Flask(__name__, static_folder="../../web", static_url_path="")
CORS(app)

# --- Routes ---
@app.route("/")
def index():
    """Serve the frontend index.html"""
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy", "service": "AWS CLI Generator"}), 200

@app.route("/mcp/generate-cli", methods=["POST"])
def generate_cli():
    try:
        data = request.get_json()
        nlp_input = data.get("nlp_input", "")
        if not nlp_input:
            return jsonify({"error": "Missing input"}), 400

        command, explanation = generate_command(nlp_input)
        return jsonify({"command": command, "explanation": explanation}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(app.static_folder, "favicon.ico")

# --- Lambda handler (via Mangum) ---
handler = Mangum(app)

# --- Local run ---
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
