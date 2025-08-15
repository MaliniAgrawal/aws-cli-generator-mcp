def parse_s3_command(nlp_input: str) -> tuple[str, str]:
    """
    Parses NLP input into AWS S3 CLI commands.
    """
    lowered_input = nlp_input.lower()

    if "create" in lowered_input and "bucket" in lowered_input:
        # Extract bucket name if present
        parts = lowered_input.split()
        bucket_name = None
        for i, word in enumerate(parts):
            if word == "named" and i + 1 < len(parts):
                bucket_name = parts[i + 1]
                break
            if word == "name" and i + 1 < len(parts):
                bucket_name = parts[i + 1]
                break
        bucket_name = bucket_name or "my-bucket"
        return (
            f"aws s3 mb s3://{bucket_name}",
            f"Creates a new S3 bucket named '{bucket_name}'."
        )

    elif "list" in lowered_input and "bucket" in lowered_input:
        return (
            "aws s3 ls",
            "Lists all S3 buckets in your account."
        )

    else:
        return (
            "aws help",
            "Sorry, I couldn't understand that S3 command. Please try again."
        )
