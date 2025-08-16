import json
import os
import re
from typing import Dict, Tuple, Optional

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..", "data"))
KEYWORD_FILE = os.path.join(DATA_DIR, "keyword_map.json")

# cache
_KEYMAP: Optional[Dict] = None

def load_keyword_map() -> Dict:
    global _KEYMAP
    if _KEYMAP is None:
        with open(KEYWORD_FILE, "r", encoding="utf-8") as f:
            _KEYMAP = json.load(f)
    return _KEYMAP

def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())

def find_action(text: str) -> Optional[str]:
    km = load_keyword_map()
    for canonical, synonyms in km["actions"].items():
        for s in synonyms:
            if f" {s} " in f" {text} ":
                return canonical
    return None

def find_service(text: str) -> Optional[str]:
    km = load_keyword_map()
    for service, synonyms in km["resources"].items():
        for s in synonyms:
            if f" {s} " in f" {text} ":
                return service
    return None

def extract_region(text: str) -> Optional[str]:
    km = load_keyword_map()
    # explicit flag
    m = re.search(r"--region\s+([a-z0-9-]+)", text)
    if m:
        return m.group(1)
    # plain mention
    for r in km["regions"]:
        if r in text:
            return r
    # phrases like "in us-west-2"
    m2 = re.search(r"\bin\s+(us|eu|ap)-[a-z0-9-]+", text)
    if m2:
        return m2.group(0).split()[-1]
    return None

def extract_name(text: str, fallback_key_words=("bucket", "user", "role", "table", "api")) -> Optional[str]:
    # common patterns: 'named X', 'called X', 'name X'
    m = re.search(r"\b(named|called|name)\s+([a-zA-Z0-9._-]+)", text)
    if m:
        return m.group(2)
    # 'bucket <name>', 'table <name>' ...
    pattern = r"\b(" + "|".join(fallback_key_words) + r")\s+([a-zA-Z0-9._-]+)"
    m2 = re.search(pattern, text)
    if m2:
        return m2.group(2)
    # quotes
    m3 = re.search(r"['\"]([a-zA-Z0-9._-]+)['\"]", text)
    if m3:
        return m3.group(1)
    return None

def extract_instance_id(text: str) -> Optional[str]:
    m = re.search(r"\b(i-[0-9a-f]{8,17})\b", text)
    return m.group(1) if m else None

def detect_intent(text: str) -> Tuple[Optional[str], Optional[str]]:
    """
    returns (service, action)
    """
    t = normalize(text)
    return (find_service(t), find_action(t))
