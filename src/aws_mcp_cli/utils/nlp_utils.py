"""
nlp_utils.py - NLP helpers for AWS CLI Generator
Rule-based extractors + ML hooks for future upgrade.
"""

import re
from typing import Optional


# ---------------------------
# Region Extractor
# ---------------------------
def extract_region(text: str) -> Optional[str]:
    """Extract AWS region from input text (rule-based)."""
    region_map = {
        "us east 1": "us-east-1",
        "us east one": "us-east-1",
        "virginia": "us-east-1",
        "us west 2": "us-west-2",
        "oregon": "us-west-2",
        "mumbai": "ap-south-1",
        "tokyo": "ap-northeast-1",
        "singapore": "ap-southeast-1",
        "frankfurt": "eu-central-1",
        "ireland": "eu-west-1",
    }

    text = text.lower()
    for k, v in region_map.items():
        if k in text:
            return v
    return None


# ---------------------------
# Name Extractor
# ---------------------------

def extract_name(text: str) -> str:
    """
    Extracts a resource name from text.
    Handles both explicit ("name myapi") and implicit ("http api myapi").
    """
    lowered = text.lower()

    # Explicit "name myresource"
    match = re.search(r"(?:name|called|named)\s+([a-zA-Z0-9-_]+)", lowered)
    if match:
        return match.group(1)

    # Handle patterns like "s3 bucket mybucket", "http api myapi"
    match = re.search(r"(?:bucket|api|table|queue|topic|function|user)\s+([a-zA-Z0-9-_]+)", lowered)
    if match:
        return match.group(1)

    return None


# ---------------------------
# ML Hooks (Phase-3.5)
# ---------------------------
def detect_intent_ml(text: str) -> Optional[str]:
    """
    Placeholder for ML intent detection (HuggingFace/Bedrock/SageMaker).
    For now returns None (rule-based only).
    """
    # Example future:
    # model = load_pipeline()
    # return model(text)
    return None


def extract_entities_ml(text: str) -> dict:
    """
    Placeholder for ML-based entity extraction.
    Returns dict of entities (service, region, resource).
    """
    return {}
