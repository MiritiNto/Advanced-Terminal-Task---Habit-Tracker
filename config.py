import json
import os

CONFIG_FILE = "config.json"
DEFAULT_CONFIG = {"theme": "dark", "default_priority": 3}

def load_config():
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'w') as f:
            json.dump(DEFAULT_CONFIG, f)
        return DEFAULT_CONFIG
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)