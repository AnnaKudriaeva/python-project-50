from gendiff.parser import load_data

def generate_diff(file1_path, file2_path):
    file1_data = load_data(file1_path)
    file2_data = load_data(file2_path)
    return find_differences(file1_data, file2_data)


def find_differences(data1, data2):
    diff = {}
    keys = set(data1.keys()) | set(data2.keys())

    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if value1 == value2:
            diff[key] = {"type": "unchanged", "value": value1}
        elif key not in data1:
            diff[key] = {"type": "added", "value": value2}
        elif key not in data2:
            diff[key] = {"type": "removed", "value": value1}
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff[key] = {"type": "nested", "value": find_differences(value1, value2)}
        else:
            diff[key] = {"type": "changed", "value": (value1, value2)}

    return diff
