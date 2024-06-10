def format_stylish(diff, depth=0):
    indent_size = 4
    current_indent = " " * (depth * indent_size)
    lines = []

    def format_value(value, depth):
        if isinstance(value, dict):
            formatted_items = []
            nested_current_indent = " " * ((depth + 1) * indent_size)
            nested_nested_indent = " " * ((depth + 2) * indent_size)
            for k, v in value.items():
                formatted_items.append(
                    f"{nested_nested_indent}{k}: {format_value(v, depth + 1)}"
                )
            return f"{{\n{'\n'.join(formatted_items)}\n{nested_current_indent}}}"
        elif value is None:
            return "null"
        elif isinstance(value, bool):
            return str(value).lower()
        else:
            return str(value)

    for key in sorted(diff.keys()):
        item = diff[key]
        if item["type"] == "unchanged":
            lines.append(
                f"{current_indent}    {key}: {format_value(item['value'], depth)}"
            )
        elif item["type"] == "added":
            lines.append(
                f"{current_indent}  + {key}: {format_value(item['value'], depth)}"
            )
        elif item["type"] == "removed":
            lines.append(
                f"{current_indent}  - {key}: {format_value(item['value'], depth)}"
            )
        elif item["type"] == "changed":
            old_value, new_value = item["value"]
            lines.append(f"{current_indent}  - {key}: {format_value(old_value, depth)}")
            lines.append(f"{current_indent}  + {key}: {format_value(new_value, depth)}")
        elif item["type"] == "nested":
            lines.append(
                f"{current_indent}    {key}: {format_stylish(item['value'], depth + 1)}"
            )

    return f"{{\n{'\n'.join(lines)}\n{current_indent}}}"
