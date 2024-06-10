import json
import yaml

def load_data(file_path):
    with open(file_path) as f:
        if file_path.endswith(('.yaml', '.yml')):
            return yaml.safe_load(f)
        elif file_path.endswith('.json'):
            return json.load(f)
        else:
            raise ValueError("Unsupported file format")
