def parse_dynamodb_command(nlp_input: str) -> tuple[str, str]:
    """
    Parses NLP input into AWS DynamoDB CLI commands.
    """
    lowered_input = nlp_input.lower()

    if "create" in lowered_input and "table" in lowered_input:
        return (
            "aws dynamodb create-table --table-name MyTable "
            "--attribute-definitions AttributeName=Id,AttributeType=S "
            "--key-schema AttributeName=Id,KeyType=HASH "
            "--billing-mode PAY_PER_REQUEST",
            "Creates a DynamoDB table named 'MyTable' with a primary key 'Id'."
        )

    elif "list" in lowered_input and "tables" in lowered_input:
        return (
            "aws dynamodb list-tables",
            "Lists all DynamoDB tables in your AWS account."
        )

    else:
        return (
            "aws help",
            "Sorry, I couldn't understand that DynamoDB command. Please try again."
        )
