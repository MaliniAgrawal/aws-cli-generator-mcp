# src/aws_mcp_cli/command_generator.py

def generate_command(user_input: str):
    user_input = user_input.lower()

    if "s3" in user_input and "create" in user_input and "bucket" in user_input:
        bucket_name = extract_bucket_name(user_input)
        region = extract_region(user_input)
        command = f"aws s3 mb s3://{bucket_name} --region {region}" if region else f"aws s3 mb s3://{bucket_name}"
        explanation = f"Creates an S3 bucket named '{bucket_name}'"
        return command, explanation

    elif "iam" in user_input and "user" in user_input and "create" in user_input:
        user_name = extract_name(user_input)
        command = f"aws iam create-user --user-name {user_name}"
        explanation = f"Creates a new IAM user named '{user_name}'"
        return command, explanation

    elif "ec2" in user_input and "instance" in user_input and "launch" in user_input:
        instance_type = extract_instance_type(user_input)
        ami_id = extract_ami(user_input)
        command = f"aws ec2 run-instances --image-id {ami_id} --instance-type {instance_type}"
        explanation = f"Launches an EC2 instance with AMI {ami_id} and type {instance_type}"
        return command, explanation

    elif "dynamodb" in user_input and "table" in user_input and "create" in user_input:
        table_name = extract_table_name(user_input)
        command = f"aws dynamodb create-table --table-name {table_name} --key-schema ... --attribute-definitions ... --billing-mode PAY_PER_REQUEST"
        explanation = f"Creates a DynamoDB table named '{table_name}'"
        return command, explanation

    elif "api gateway" in user_input and "create" in user_input and "rest" in user_input:
        name = extract_name(user_input)
        command = f"aws apigateway create-rest-api --name \"{name}\""
        explanation = f"Creates a new REST API in API Gateway with name '{name}'"
        return command, explanation

    else:
        return "aws help", "Sorry, I couldn't understand that. Showing AWS help."


# -- Extractor Functions (Add more as needed)
def extract_bucket_name(text):
    words = text.split()
    for i, word in enumerate(words):
        if word in {"bucket", "bucketname", "bucket-name"} and i + 1 < len(words):
            return words[i + 1]
    return "my-bucket"

def extract_region(text):
    for word in text.split():
        if word.startswith("us-") or word.startswith("eu-"):
            return word
    return ""

def extract_name(text):
    words = text.split()
    for i, word in enumerate(words):
        if word in {"named", "name"} and i + 1 < len(words):
            return words[i + 1]
    return "default-name"

def extract_instance_type(text):
    if "t2.micro" in text:
        return "t2.micro"
    return "t2.micro"

def extract_ami(text):
    if "ami-" in text:
        return text.split("ami-")[1].split()[0]
    return "ami-0c55b159cbfafe1f0"

def extract_table_name(text):
    words = text.split()
    for i, word in enumerate(words):
        if word == "table" and i + 1 < len(words):
            return words[i + 1]
    return "my-table"
