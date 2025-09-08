# AWS CLI Generator MCP

Generate AWS CLI commands from natural language prompts using rule-based and NLP utilities. Includes a Flask API backend and a simple web frontend.

## Features

- Converts natural language requests to AWS CLI commands
- Supports S3, EC2, IAM, Lambda, DynamoDB, API Gateway (REST/HTTP), RDS, SQS, SNS, CloudWatch
- Rule-based entity extraction (region, resource name)
- Extensible for ML-based intent/entity extraction
- Flask API with `/generate` endpoint
- Web frontend for interactive command generation
- DynamoDB logging (optional)

## Project Structure
.
├── .aws-sam/  # (empty)
├── .git/
├── .github/
├── .gitignore
├── .pytest_cache/
├── Dockerfile
├── README.md
├── create_project.py
├── data/
│   └── keyword_map.json
├── requirements.txt
├── scripts/
│   ├── __init__.py
│   └── mcp_cli_client.py
├── src/
│   ├── __init__.py
│   ├── mcp_server.py
│   └── aws_mcp_cli/
│       ├── __init__.py
│       ├── command_generator.py
│       ├── validator.py
│       └── utils/
│           ├── __init__.py
│           ├── helpers.py
│           └── nlp_utils.py
├── tests/
│   ├── __init__.py
│   └── test_command_generator.py
├── venv-phase3/
├── web/
│   ├── favicon.ico
│   ├── index.html
│   ├── script.js
│   └── style.css
└── template.yaml
automate this with create_project.py file


## Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/MaliniAgrawal/aws-cli-generator-mcp.git
   cd aws-cli-generator-mcp
2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
source venv/bin/activate
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
4. **Run the Flask server**
export FLASK_APP=src/mcp_server.py
export PYTHONPATH=./src
flask run --reload
5. **Access the web frontend**
   Open your browser and go to `http://localhost:5000 in your browser.

   Usage:-

Type an AWS request in natural language (e.g., "create s3 bucket named mybucket in us-east-1") and get the corresponding AWS CLI command.
Supported services: S3, EC2, IAM, Lambda, DynamoDB, API Gateway, RDS, SQS, SNS, CloudWatch.
Testing:-
export PYTHONPATH=./src
pytest
You can customize this further for your needs!

## Future Enhancements
- Integrate ML models for better intent/entity extraction
- Add more AWS services
- Improve web UI/UX
- Add authentication and security features
- Dockerize the application for easier deployment
- Add CI/CD pipelines
- Implement caching for frequent requests
- Add more comprehensive tests
- Improve error handling and logging
- You can customize this further for your needs!

Limitaion:-
- Currently rule-based, may not handle complex requests well
- Limited to certain AWS services
- Basic web UI, can be improved
- No authentication/security features
- No caching, may have latency for frequent requests
- Basic error handling/logging
- Limited tests, can be expanded
License:
MIT
See LICENSE for details.
Author:-
Malini Agrawal
