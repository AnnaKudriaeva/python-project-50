import yaml


def parse_yaml(file_path):
    try:
        with open(file_path) as file:
            return yaml.safe_load(file)
    except Exception as e:
        print(f"Error loading YAML file {file_path}: {e}")
        return None
