def parse_iam_command(nlp_input: str) -> tuple[str, str]:
    """
    Parses NLP input into AWS IAM CLI commands.
    """
    lowered_input = nlp_input.lower()

    if "create" in lowered_input and "user" in lowered_input:
        parts = lowered_input.split()
        username = None
        for i, word in enumerate(parts):
            if word == "named" and i + 1 < len(parts):
                username = parts[i + 1]
                break
            if word == "name" and i + 1 < len(parts):
                username = parts[i + 1]
                break
        username = username or "new-user"
        return (
            f"aws iam create-user --user-name {username}",
            f"Creates a new IAM user named '{username}'."
        )

    elif "list" in lowered_input and "users" in lowered_input:
        return (
            "aws iam list-users",
            "Lists all IAM users in your AWS account."
        )

    else:
        return (
            "aws help",
            "Sorry, I couldn't understand that IAM command. Please try again."
        )
