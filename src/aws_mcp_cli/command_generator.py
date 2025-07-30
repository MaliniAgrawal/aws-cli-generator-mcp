# src/aws_mcp_cli/command_generator.py

def generate_command(user_input: str):
    user_input = user_input.lower().strip()

    # S3 bucket creation
    if "s3 bucket" in user_input and "create" in user_input:
        bucket_name = extract_name(user_input)
        return f"aws s3 mb s3://{bucket_name}", "Creates a new S3 bucket"

    # List EC2 instances
    elif "ec2" in user_input and ("list" in user_input or "show" in user_input):
        return "aws ec2 describe-instances", "Lists all EC2 instances"

    # Start EC2 instance
    elif "ec2" in user_input and "start" in user_input:
        return "aws ec2 start-instances --instance-ids i-1234567890abcdef0", "Starts an EC2 instance (replace with actual instance ID)"

    # Stop EC2 instance
    elif "ec2" in user_input and "stop" in user_input:
        return "aws ec2 stop-instances --instance-ids i-1234567890abcdef0", "Stops an EC2 instance (replace with actual instance ID)"

    # IAM user creation
    elif "create" in user_input and "iam user" in user_input:
        username = extract_name(user_input)
        return f"aws iam create-user --user-name {username}", "Creates a new IAM user"

    # IAM list users
    elif "list" in user_input and "iam users" in user_input:
        return "aws iam list-users", "Lists all IAM users"

    # Fallback
    return "aws help", "Sorry, I couldn't understand that. Showing AWS help."



def extract_name(text: str):
    # Basic NLP-ish name extractor (e.g., from “named xyz” or “called abc”)
    for keyword in ["named", "called"]:
        if keyword in text:
            return text.split(keyword)[-1].strip().replace(" ", "-")
    return "example-resource"
