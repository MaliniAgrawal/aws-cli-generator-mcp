

 🛠️ AWS CLI Generator MCP – Phase 1 (Local)

This project is a Model Context Protocol (MCP) server that converts natural language (NLP) into AWS CLI commands, designed for cloud support engineers, developers, and DevOps practitioners.
Phase 1 is focused on local development:

 ✅ Modular parsers for S3, EC2, IAM, DynamoDB, API Gateway
 ✅ Flask server to serve an API (`/mcp/generate-cli`)
 ✅ CLI client (`scripts/mcp_cli_client.py`) for interactive local testing
 ✅ Web frontend (`web/index.html`, `web/styles.css`, `web/script.js`) for live demo
 ✅ Unit tests per parser with `pytest`
 ✅ Dark mode toggle for better UI experience

 ⚡ This is Phase 1 (Local-only). Future phases will expand to serverless AWS deployment and Marketplace readiness.



 🚀 Features

 🔌 Natural Language → AWS CLI
  Example:


  "create an s3 bucket named mybucket in us-east-1"
  → aws s3 mb s3://mybucket --region us-east-1


 📦 Services Supported

   Amazon S3
   Amazon EC2
   IAM
   DynamoDB
   API Gateway

 🧪 Tested with `pytest` – unit tests for each parser ensure correctness

 🖥️ Two Interfaces

   CLI: Interactive loop in terminal
   Web UI: Lightweight Flask + HTML/CSS/JS frontend



 📂 Project Structure


aws-cli-generator-mcp/
│── src/aws_mcp_cli/
│   ├── mcp_server.py          Flask backend
│   ├── command_generator.py   Central dispatcher
│   └── parsers/               Service-specific parsers
│── scripts/
│   └── mcp_cli_client.py      CLI client loop
│── tests/parsers/             Unit tests for each parser
│── web/
│   ├── index.html             Web frontend
│   ├── styles.css             Styling (with dark mode toggle)
│   └── script.js              Frontend logic
│── requirements.txt
│── Dockerfile (optional)
│── README.md




 🖥️ Run Locally

1. Clone repo & install dependencies

 bash
   git clone <your-repo-url
   cd aws-cli-generator-mcp
   python3 -m venv venv-local
   source venv-local/bin/activate
   pip install -r requirements.txt
 

2. Run Flask server

 bash
   export FLASK_APP=src/aws_mcp_cli/mcp_server.py
   flask run
 

   Visit 👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

3. Use CLI client

 bash
   python scripts/mcp_cli_client.py
 

4. Run tests

 bash
   pytest -v tests/parsers/
 



 🎯 Roadmap

Phase 1 (✅ Done) – Local CLI + Web UI with modular parsers
Phase 2 (🔜 Next) – Serverless deployment on AWS (API Gateway + Lambda + S3 + CloudFront)
Phase 3 – Marketplace-ready package (CI/CD, templates, IAM OIDC, multi-tenant setup)





