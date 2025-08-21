// AWS CLI command mappings
const commandMappings = {
    // S3 Commands
    'create.*s3.*bucket': {
        template: 'aws s3api create-bucket --bucket {bucket_name} --region {region}',
        explanation: 'Creates a new S3 bucket with the specified name in the given region.',
        extractors: {
            bucket_name: /(?:named?|called?)\s+(\S+)/i,
            region: /(?:in|region)\s+([\w-]+)/i
        },
        defaults: {
            region: 'us-east-1'
        }
    },
    'list.*s3.*bucket': {
        template: 'aws s3 ls',
        explanation: 'Lists all S3 buckets in your AWS account.'
    },
    'delete.*s3.*bucket': {
        template: 'aws s3api delete-bucket --bucket {bucket_name}',
        explanation: 'Deletes an empty S3 bucket.',
        extractors: {
            bucket_name: /(?:bucket\s+)?(?:named?|called?)?\s*(\S+)/i
        }
    },
    'upload.*s3': {
        template: 'aws s3 cp {local_file} s3://{bucket_name}/{key}',
        explanation: 'Uploads a file to an S3 bucket.',
        extractors: {
            local_file: /(?:file|upload)\s+(\S+)/i,
            bucket_name: /(?:to|bucket)\s+(\S+)/i,
            key: /(?:as|key)\s+(\S+)/i
        },
        defaults: {
            key: ''
        }
    },

    // EC2 Commands
    'list.*ec2.*instance': {
        template: 'aws ec2 describe-instances --region {region}',
        explanation: 'Lists all EC2 instances in the specified region.',
        extractors: {
            region: /(?:in|region)\s+([\w-]+)/i
        },
        defaults: {
            region: 'us-east-1'
        }
    },
    'start.*ec2.*instance': {
        template: 'aws ec2 start-instances --instance-ids {instance_id}',
        explanation: 'Starts a stopped EC2 instance.',
        extractors: {
            instance_id: /(?:instance|id)\s+(i-\w+)/i
        }
    },
    'stop.*ec2.*instance': {
        template: 'aws ec2 stop-instances --instance-ids {instance_id}',
        explanation: 'Stops a running EC2 instance.',
        extractors: {
            instance_id: /(?:instance|id)\s+(i-\w+)/i
        }
    },
    'create.*ec2.*instance|launch.*ec2': {
        template: 'aws ec2 run-instances --image-id {ami_id} --instance-type {instance_type} --key-name {key_name} --region {region}',
        explanation: 'Launches a new EC2 instance with specified configuration.',
        extractors: {
            ami_id: /(?:ami|image)\s+(ami-\w+)/i,
            instance_type: /(?:type)\s+([\w.]+)/i,
            key_name: /(?:key)\s+(\S+)/i,
            region: /(?:in|region)\s+([\w-]+)/i
        },
        defaults: {
            ami_id: 'ami-0c55b159cbfafe1f0',
            instance_type: 't2.micro',
            key_name: 'my-key',
            region: 'us-east-1'
        }
    },

    // Lambda Commands
    'create.*lambda.*function': {
        template: 'aws lambda create-function --function-name {function_name} --runtime {runtime} --role {role_arn} --handler {handler} --zip-file fileb://{zip_file}',
        explanation: 'Creates a new Lambda function with the specified configuration.',
        extractors: {
            function_name: /(?:named?|called?)\s+(\S+)/i,
            runtime: /(?:python|node|java|dotnet|go|ruby)[\d.]*/i,
            role_arn: /(?:role)\s+(\S+)/i,
            handler: /(?:handler)\s+(\S+)/i,
            zip_file: /(?:zip|file)\s+(\S+)/i
        },
        defaults: {
            runtime: 'python3.9',
            role_arn: 'arn:aws:iam::123456789012:role/lambda-role',
            handler: 'index.handler',
            zip_file: 'function.zip'
        }
    },
    'list.*lambda.*function': {
        template: 'aws lambda list-functions',
        explanation: 'Lists all Lambda functions in your AWS account.'
    },
    'invoke.*lambda': {
        template: 'aws lambda invoke --function-name {function_name} --payload \'{payload}\' response.json',
        explanation: 'Invokes a Lambda function with the specified payload.',
        extractors: {
            function_name: /(?:function|named?)\s+(\S+)/i,
            payload: /(?:payload|data)\s+(.+)/i
        },
        defaults: {
            payload: '{}'
        }
    },

    // RDS Commands
    'create.*rds.*database|create.*database.*rds': {
        template: 'aws rds create-db-instance --db-instance-identifier {db_id} --db-instance-class {instance_class} --engine {engine} --master-username {username} --master-user-password {password} --allocated-storage {storage}',
        explanation: 'Creates a new RDS database instance.',
        extractors: {
            db_id: /(?:named?|called?|identifier)\s+(\S+)/i,
            instance_class: /(?:class|type)\s+(db\.\w+)/i,
            engine: /(?:mysql|postgres|mariadb|oracle|sqlserver)/i,
            username: /(?:username|user)\s+(\S+)/i,
            storage: /(?:storage|gb)\s+(\d+)/i
        },
        defaults: {
            db_id: 'mydb-instance',
            instance_class: 'db.t3.micro',
            engine: 'mysql',
            username: 'admin',
            password: 'CHANGE_ME',
            storage: '20'
        }
    },
    'list.*rds.*database': {
        template: 'aws rds describe-db-instances',
        explanation: 'Lists all RDS database instances in your AWS account.'
    },

    // IAM Commands
    'create.*iam.*user': {
        template: 'aws iam create-user --user-name {user_name}',
        explanation: 'Creates a new IAM user.',
        extractors: {
            user_name: /(?:named?|called?|user)\s+(\S+)/i
        }
    },
    'list.*iam.*user': {
        template: 'aws iam list-users',
        explanation: 'Lists all IAM users in your AWS account.'
    },
    'create.*iam.*role': {
        template: 'aws iam create-role --role-name {role_name} --assume-role-policy-document file://{policy_file}',
        explanation: 'Creates a new IAM role with the specified trust policy.',
        extractors: {
            role_name: /(?:named?|called?|role)\s+(\S+)/i,
            policy_file: /(?:policy|file)\s+(\S+)/i
        },
        defaults: {
            policy_file: 'trust-policy.json'
        }
    },

    // CloudFormation Commands
    'create.*stack|deploy.*cloudformation': {
        template: 'aws cloudformation create-stack --stack-name {stack_name} --template-body file://{template_file}',
        explanation: 'Creates a new CloudFormation stack from a template.',
        extractors: {
            stack_name: /(?:named?|called?|stack)\s+(\S+)/i,
            template_file: /(?:template|file)\s+(\S+)/i
        },
        defaults: {
            template_file: 'template.yaml'
        }
    },
    'list.*stack': {
        template: 'aws cloudformation list-stacks',
        explanation: 'Lists all CloudFormation stacks in your AWS account.'
    },
    'delete.*stack': {
        template: 'aws cloudformation delete-stack --stack-name {stack_name}',
        explanation: 'Deletes a CloudFormation stack.',
        extractors: {
            stack_name: /(?:named?|called?|stack)\s+(\S+)/i
        }
    }
};

function parseNaturalLanguage(input) {
    const normalizedInput = input.toLowerCase();
    
    // Find matching command pattern
    for (const [pattern, config] of Object.entries(commandMappings)) {
        const regex = new RegExp(pattern, 'i');
        if (regex.test(normalizedInput)) {
            let command = config.template;
            
            // Extract parameters if extractors are defined
            if (config.extractors) {
                for (const [param, extractor] of Object.entries(config.extractors)) {
                    const match = normalizedInput.match(extractor);
                    const value = match ? match[1] : (config.defaults && config.defaults[param]) || `<${param}>`;
                    command = command.replace(`{${param}}`, value);
                }
            }
            
            // Replace any remaining placeholders with defaults or placeholders
            command = command.replace(/\{(\w+)\}/g, (match, param) => {
                return (config.defaults && config.defaults[param]) || `<${param}>`;
            });
            
            return {
                command: command,
                explanation: config.explanation
            };
        }
    }
    
    // If no pattern matches, provide a helpful response
    return {
        command: `# No exact match found. Here are some suggestions:\n# Try: "aws [service] [action]" format\n# Example: aws s3 ls, aws ec2 describe-instances`,
        explanation: `I couldn't find an exact match for "${input}". Try being more specific about the AWS service and action you want to perform.`
    };
}

async function generateCLI() {
    const input = document.getElementById('nlp-input').value.trim();
    if (!input) {
        alert('Please enter a task description.');
        return;
    }

    const outputSection = document.getElementById('output-section');
    const cliCommand = document.getElementById('cli-command');
    const cliExplanation = document.getElementById('cli-explanation');
    const generateButton = document.querySelector('button[onclick="generateCLI()"]');

    // Show output section
    outputSection.style.display = 'block';
    
    // Set loading state
    cliCommand.innerHTML = '<span class="loading"></span> Generating command...';
    cliExplanation.textContent = '';
    generateButton.disabled = true;

    // Simulate processing delay for better UX
    await new Promise(resolve => setTimeout(resolve, 500));

    try {
        // Parse the natural language input
        const result = parseNaturalLanguage(input);
        
        // Display results
        cliCommand.textContent = result.command;
        cliExplanation.textContent = result.explanation;
        
        // Save to history if it's a valid command
        if (!result.command.startsWith('#')) {
            saveToHistory(result.command, result.explanation, input);
            renderHistory();
        }
    } catch (err) {
        console.error('Error:', err);
        cliCommand.innerHTML = '<span class="error">Error generating command. Please try again.</span>';
        cliExplanation.textContent = '';
    } finally {
        generateButton.disabled = false;
    }
}

function saveToHistory(command, explanation, originalInput) {
    let history = JSON.parse(localStorage.getItem('cliHistory')) || [];
    history.unshift({ 
        command, 
        explanation, 
        originalInput,
        timestamp: new Date().toLocaleString() 
    });
    // Keep only last 10 items
    history = history.slice(0, 10);
    localStorage.setItem('cliHistory', JSON.stringify(history));
}

function renderHistory() {
    const historyList = document.getElementById('history-list');
    let history = JSON.parse(localStorage.getItem('cliHistory')) || [];
    
    if (history.length === 0) {
        historyList.innerHTML = '<p style="opacity: 0.6;">No commands generated yet.</p>';
        return;
    }

    historyList.innerHTML = '';
    history.forEach((item, index) => {
        const entry = document.createElement('div');
        entry.classList.add('history-item');
        entry.innerHTML = `
            <strong>#${index + 1}</strong> <code>${item.command}</code>
            <small>${item.explanation}</small>
            <em>${item.timestamp}</em>
        `;
        entry.style.cursor = 'pointer';
        entry.onclick = () => {
            document.getElementById('nlp-input').value = item.originalInput || '';
            document.getElementById('cli-command').textContent = item.command;
            document.getElementById('cli-explanation').textContent = item.explanation;
            document.getElementById('output-section').style.display = 'block';
        };
        historyList.appendChild(entry);
    });
}

function copyToClipboard() {
    const commandText = document.getElementById('cli-command').innerText;
    if (commandText && !commandText.includes('Generating') && !commandText.startsWith('#')) {
        navigator.clipboard.writeText(commandText)
            .then(() => {
                const copyButton = document.querySelector('.copy-button');
                const originalText = copyButton.textContent;
                copyButton.textContent = 'Copied!';
                copyButton.style.background = '#4caf50';
                setTimeout(() => {
                    copyButton.textContent = originalText;
                    copyButton.style.background = '';
                }, 2000);
            })
            .catch(err => {
                console.error('Failed to copy:', err);
                alert('Failed to copy command. Please copy manually.');
            });
    }
}

function clearHistory() {
    if (confirm('Are you sure you want to clear the command history?')) {
        localStorage.removeItem('cliHistory');
        renderHistory();
    }
}

function clearAll() {
    document.getElementById('nlp-input').value = '';
    document.getElementById('cli-command').textContent = '';
    document.getElementById('cli-explanation').textContent = '';
    document.getElementById('output-section').style.display = 'none';
}

function loadExample() {
    const examples = [
        "Create an S3 bucket named my-awesome-bucket in us-west-2",
        "List all EC2 instances in us-east-1",
        "Create a Lambda function named processData with Python runtime",
        "Create an RDS MySQL database named production-db",
        "Create an IAM user named developer",
        "Start EC2 instance i-1234567890abcdef0",
        "Upload file.txt to S3 bucket my-bucket",
        "Create a CloudFormation stack named my-app-stack"
    ];
    const randomExample = examples[Math.floor(Math.random() * examples.length)];
    document.getElementById('nlp-input').value = randomExample;
}

function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    const mode = document.body.classList.contains('dark-mode') ? 'dark' : 'light';
    localStorage.setItem('theme', mode);
    
    // Update button emoji
    const button = document.querySelector('.toggle-dark-mode');
    button.textContent = mode === 'dark' ? '☀️' : '🌙';
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    // Load theme
    if (localStorage.getItem('theme') === 'dark') {
        document.body.classList.add('dark-mode');
        document.querySelector('.toggle-dark-mode').textContent = '☀️';
    }
    
    // Render history
    renderHistory();
    
    // Add enter key support for textarea
    document.getElementById('nlp-input').addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && e.ctrlKey) {
            generateCLI();
        }
    });
});