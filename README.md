# AWS CLI Generator MCP

Natural Language to AWS CLI Generator with Flask + SAM (Serverless Application Model).  
Phase 2: Unified Command Generator + Web Frontend + SAM-ready for Lambda/API Gateway.  

---

## 🚀 Features
- Convert **natural language (NLP)** requests into AWS CLI commands.
- Supports **S3, EC2, IAM, DynamoDB, API Gateway**.
- Provides **explanations** for generated commands.
- Lightweight **Flask backend** with **web UI**.
- Deployable to AWS Lambda + API Gateway via **AWS SAM**.
- Phase 3 ready → Multi-tenant support with API Keys / IAM roles.

---

## 📂 Project Structure
aws-cli-generator-mcp/
├── src/aws_mcp_cli/
│ ├── command_generator.py # Unified NLP → CLI parser
│ ├── mcp_server.py # Flask backend (SAM-ready)
│ └── ...
├── web/
│ ├── index.html # Web UI frontend
│ ├── script.js # JS logic for frontend
│ └── style.css # Styling (with dark mode toggle)
├── tests/
│ └── test_command_generator.py # Unit tests for all services
├── template.yaml # SAM template for Lambda + API GW
├── requirements.txt # Dependencies
└── README.md


---

## 🧪 Local Development

### 1. Install dependencies
```bash
python3 -m venv venv-local
source venv-local/bin/activate
pip install -r requirements.txt

export FLASK_APP=src/aws_mcp_cli/mcp_server.py
flask run

export PYTHONPATH=./src
pytest -v tests/

sam build
sam deploy --guided

🛣 Roadmap

Phase 1: Local Flask app + individual parsers ✅

Phase 2: Unified command generator + SAM-ready ✅

Phase 3: Multi-tenant support (API Keys, IAM) → AWS Marketplace target 🚀
📜 License
MIT