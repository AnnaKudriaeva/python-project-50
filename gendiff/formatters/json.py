import json


def format_json(diff):
    return json.dumps(diff, sort_keys=True, indent=4, ensure_ascii=False)
