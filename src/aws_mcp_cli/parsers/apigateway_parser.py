def parse_apigateway_command(nlp_input: str) -> tuple[str, str]:
    """
    Parses NLP input into AWS API Gateway CLI commands.
    """
    lowered_input = nlp_input.lower()

    if "create" in lowered_input and "api" in lowered_input:
        return (
            "aws apigateway create-rest-api --name MyAPI --region us-east-1",
            "Creates a new API Gateway REST API named 'MyAPI' in us-east-1."
        )

    elif "list" in lowered_input and "apis" in lowered_input:
        return (
            "aws apigateway get-rest-apis",
            "Lists all API Gateway REST APIs in your AWS account."
        )

    else:
        return (
            "aws help",
            "Sorry, I couldn't understand that API Gateway command. Please try again."
        )
