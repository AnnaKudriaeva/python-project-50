import json


def format_plain(diff, path=""):
    lines = []

    for key in sorted(diff.keys()):
        item = diff[key]
        item_type = item["type"]
        current_path = f"{path}.{key}" if path else key

        if item_type == "added":
            value = format_value_plain(item["value"])
            lines.append(f"Property '{current_path}' was added with value: {value}")
        elif item_type == "removed":
            lines.append(f"Property '{current_path}' was removed")
        elif item_type == "changed":
            old_value = format_value_plain(item["value"][0])
            new_value = format_value_plain(item["value"][1])
            lines.append(
                f"Property '{current_path}' was updated. From {old_value} to {new_value}"
            )
        elif item_type == "nested":
            lines.extend(format_plain(item["value"], current_path))

    return lines


def format_value_plain(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif value is None:
        return "null"
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return json.dumps(value, ensure_ascii=False)
