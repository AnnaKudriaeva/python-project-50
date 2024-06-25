from gendiff.formatters import format_json, format_plain, format_stylish
from gendiff.parser import load_data


def format_diff(diff, format_name):
    if format_name == "stylish":
        return format_stylish(diff)
    elif format_name == "plain":
        return "\n".join(format_plain(diff))
    elif format_name == "json":
        return format_json(diff)
    else:
        raise ValueError(f"Unknown format: {format_name}")


def generate_diff(file1_path, file2_path, format="stylish"):
    file1_data = load_data(file1_path)
    file2_data = load_data(file2_path)
    diff = find_differences(file1_data, file2_data)
    return format_diff(diff, format)


def find_differences(data1, data2):
    diff = {}

    keys = set(data1.keys()).union(set(data2.keys()))

    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if value1 == value2:
            diff[key] = {"type": "unchanged", "value": value1}
        elif key not in data1:
            diff[key] = {"type": "added", "value": value2}
        elif key not in data2:
            diff[key] = {"type": "removed", "value": value1}
        else:
            if isinstance(value1, dict) and isinstance(value2, dict):
                diff[key] = {"type": "nested", "value": find_differences(value1, value2)}
            else:
                diff[key] = {"type": "changed", "value": (value1, value2)}

    return diff
