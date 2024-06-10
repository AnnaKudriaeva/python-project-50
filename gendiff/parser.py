import json
import yaml

def load_data(data_or_path):
    if isinstance(data_or_path, str):
        with open(data_or_path) as f:
            if data_or_path.endswith('.json'):
                return json.load(f)
            elif data_or_path.endswith('.yml') or data_or_path.endswith('.yaml'):
                return yaml.safe_load(f)
            else:
                raise ValueError("Unsupported file format")
    return data_or_path
