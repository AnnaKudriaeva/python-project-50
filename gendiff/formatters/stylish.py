def format_value(value, depth, indent_size=4):
    if isinstance(value, dict):
        formatted_items = []
        nested_current_indent = " " * ((depth + 1) * indent_size)
        nested_nested_indent = " " * ((depth + 2) * indent_size)
        for k, v in value.items():
            formatted_items.append(
                f"{nested_nested_indent}{k}: {format_value(v, depth + 1, indent_size)}"
            )
        formatted_items_str = "\n".join(formatted_items)
        return f"{{\n{formatted_items_str}\n{nested_current_indent}}}"
    elif value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return str(value)


def format_item(key, item, current_indent, depth):
    if item["type"] == "unchanged":
        return f"{current_indent}    {key}: {format_value(item['value'], depth)}"
    elif item["type"] == "added":
        return f"{current_indent}  + {key}: {format_value(item['value'], depth)}"
    elif item["type"] == "removed":
        return f"{current_indent}  - {key}: {format_value(item['value'], depth)}"
    elif item["type"] == "changed":
        old_value, new_value = item["value"]
        lines = []
        lines.append(f"{current_indent}  - {key}: {format_value(old_value, depth)}")
        lines.append(f"{current_indent}  + {key}: {format_value(new_value, depth)}")
        return "\n".join(lines)
    elif item["type"] == "nested":
        return f"{current_indent}    {key}: {format_stylish(item['value'], depth + 1)}"


def format_stylish(diff, depth=0):
    current_indent = " " * (depth * 4)
    lines = []

    for key in sorted(diff.keys()):
        item = diff[key]
        formatted_item = format_item(key, item, current_indent, depth)
        lines.append(formatted_item)

    lines = "\n".join(lines)
    return f"{{\n{lines}\n{current_indent}}}"
