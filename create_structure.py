import os

def create_project_structure(base_path="aws-cli-generator-mcp"):
    """
    Creates the specified directory and file structure for the AWS CLI generator project.

    Args:
        base_path (str): The base directory name for the project.
    """
    print(f"Creating project structure under: {os.path.abspath(base_path)}")

    # Define the structure as a dictionary where keys are paths and values are lists of files
    # or nested dictionaries for subdirectories.
    project_structure = {
        "requirements.txt": "",  # Empty string for empty file, or content
        "create_structure.py": "", # This file itself, will be overwritten if run in place
        "src/aws_mcp_cli/": {
            "mcp_server.py": "# Your Flask app\n",
            "command_generator.py": "# Next to implement\n",
            "validators.py": "# Stub it for now\n",
            "utils/": {
                "helpers.py": "# Error formatting\n"
            }
        }
    }

    def create_items(current_path, structure_dict):
        for name, content in structure_dict.items():
            full_path = os.path.join(current_path, name)
            if isinstance(content, dict):
                # It's a directory, create it and recurse
                os.makedirs(full_path, exist_ok=True)
                print(f"Created directory: {full_path}")
                create_items(full_path, content)
            else:
                # It's a file, create it with content
                # Ensure parent directory exists for files directly under base_path
                os.makedirs(os.path.dirname(full_path) or '.', exist_ok=True)
                with open(full_path, "w") as f:
                    f.write(content)
                print(f"Created file: {full_path}")

    # Create the base directory if it doesn't exist
    os.makedirs(base_path, exist_ok=True)
    create_items(base_path, project_structure)

    # Add specific content for requirements.txt
    requirements_path = os.path.join(base_path, "requirements.txt")
    with open(requirements_path, "w") as f:
        f.write("Flask==2.3.2\n") # Example dependency
        f.write("boto3\n") # AWS SDK for Python

    print("\nProject structure created successfully!")
    print("You might want to populate the files with initial code.")

if __name__ == "__main__":
    create_project_structure()
