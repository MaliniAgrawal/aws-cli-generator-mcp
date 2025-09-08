```python
import os

def create_directory_structure(base_dir='.'):
    # Create base directories and files
    os.makedirs(os.path.join(base_dir, '.aws-sam'), exist_ok=True)  # empty
    os.makedirs(os.path.join(base_dir, '.git'), exist_ok=True)
    os.makedirs(os.path.join(base_dir, '.github'), exist_ok=True)
    open(os.path.join(base_dir, '.gitignore'), 'w').close()
    os.makedirs(os.path.join(base_dir, '.pytest_cache'), exist_ok=True)
    open(os.path.join(base_dir, 'Dockerfile'), 'w').close()
    open(os.path.join(base_dir, 'README.md'), 'w').close()
    open(os.path.join(base_dir, 'create_project.py'), 'w').close()
    
    # data/
    data_dir = os.path.join(base_dir, 'data')
    os.makedirs(data_dir, exist_ok=True)
    open(os.path.join(data_dir, 'keyword_map.json'), 'w').close()
    
    open(os.path.join(base_dir, 'requirements.txt'), 'w').close()
    
    # scripts/
    scripts_dir = os.path.join(base_dir, 'scripts')
    os.makedirs(scripts_dir, exist_ok=True)
    open(os.path.join(scripts_dir, '__init__.py'), 'w').close()
    open(os.path.join(scripts_dir, 'mcp_cli_client.py'), 'w').close()
    
    # src/
    src_dir = os.path.join(base_dir, 'src')
    os.makedirs(src_dir, exist_ok=True)
    open(os.path.join(src_dir, '__init__.py'), 'w').close()
    open(os.path.join(src_dir, 'mcp_server.py'), 'w').close()
    
    # src/aws_mcp_cli/
    aws_mcp_cli_dir = os.path.join(src_dir, 'aws_mcp_cli')
    os.makedirs(aws_mcp_cli_dir, exist_ok=True)
    open(os.path.join(aws_mcp_cli_dir, '__init__.py'), 'w').close()
    open(os.path.join(aws_mcp_cli_dir, 'command_generator.py'), 'w').close()
    open(os.path.join(aws_mcp_cli_dir, 'validator.py'), 'w').close()
    
    # src/aws_mcp_cli/utils/
    utils_dir = os.path.join(aws_mcp_cli_dir, 'utils')
    os.makedirs(utils_dir, exist_ok=True)
    open(os.path.join(utils_dir, '__init__.py'), 'w').close()
    open(os.path.join(utils_dir, 'helpers.py'), 'w').close()
    open(os.path.join(utils_dir, 'nlp_utils.py'), 'w').close()
    
    # tests/
    tests_dir = os.path.join(base_dir, 'tests')
    os.makedirs(tests_dir, exist_ok=True)
    open(os.path.join(tests_dir, '__init__.py'), 'w').close()
    open(os.path.join(tests_dir, 'test_command_generator.py'), 'w').close()
    
    os.makedirs(os.path.join(base_dir, 'venv-phase3'), exist_ok=True)
    
    # web/
    web_dir = os.path.join(base_dir, 'web')
    os.makedirs(web_dir, exist_ok=True)
    open(os.path.join(web_dir, 'favicon.ico'), 'w').close()
    open(os.path.join(web_dir, 'index.html'), 'w').close()
    open(os.path.join(web_dir, 'script.js'), 'w').close()
    open(os.path.join(web_dir, 'style.css'), 'w').close()
    
    open(os.path.join(base_dir, 'template.yaml'), 'w').close()

# Run the function to create the structure in the current directory
create_directory_structure()
```