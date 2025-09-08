import os
from pathlib import Path

def create_project_structure():
    """
    Automates the creation of the project's directory and file structure.
    Uses pathlib for modern, object-oriented path manipulation and os.makedirs.
    """
    
    # Define the directories to be created
    directories = [
        '.aws-sam',
        '.github',
        'data',
        'scripts',
        'src',
        'src/aws_mcp_cli',
        'src/aws_mcp_cli/utils',
        'tests',
        'web'
    ]

    # Define the files to be created within each directory
    # The key is the directory path, the value is a list of file names.
    files_to_create = {
        'scripts': ['__init__.py', 'mcp_cli_client.py'],
        'src': ['__init__.py'],
        'src/aws_mcp_cli': ['__init__.py', 'command_generator.py', 'validator.py', 'mcp_server.py'],
        'src/aws_mcp_cli/utils': ['__init__.py', 'helpers.py', 'nlp_utils.py'],
        'tests': ['__init__.py', 'test_command_generator.py'],
        'web': ['favicon.ico', 'index.html', 'script.js', 'style.css'],
        # Top-level files
        '.': ['.gitignore', 'Dockerfile', 'README.md', 'requirements.txt', 'template.yaml']
    }

    print("Creating project directory structure...")

    # Create all directories first
    for path in directories:
        os.makedirs(path, exist_ok=True)
        print(f"Directory created: {path}")

    print("\nCreating files...")
    # Create all the files within their respective directories
    for directory, file_list in files_to_create.items():
        for file_name in file_list:
            file_path = Path(directory) / file_name
            file_path.touch()
            print(f"File created: {file_path}")

    print("\nProject structure created successfully! 🚀")

if __name__ == "__main__":
    create_project_structure()