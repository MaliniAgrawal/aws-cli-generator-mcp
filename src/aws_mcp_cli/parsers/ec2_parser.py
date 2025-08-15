def parse_ec2_command(nlp_input: str) -> tuple[str, str]:
    """
    Parses NLP input into AWS EC2 CLI commands.
    """
    lowered_input = nlp_input.lower()

    if "start" in lowered_input and "instance" in lowered_input:
        return (
            "aws ec2 start-instances --instance-ids i-1234567890abcdef0",
            "Starts the specified EC2 instance."
        )

    elif "stop" in lowered_input and "instance" in lowered_input:
        return (
            "aws ec2 stop-instances --instance-ids i-1234567890abcdef0",
            "Stops the specified EC2 instance."
        )

    elif "list" in lowered_input or "describe" in lowered_input:
        return (
            "aws ec2 describe-instances",
            "Describes all EC2 instances in your account."
        )

    else:
        return (
            "aws help",
            "Sorry, I couldn't understand that EC2 command. Please try again."
        )
