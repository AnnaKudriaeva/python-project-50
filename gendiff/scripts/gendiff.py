import argparse

from gendiff import generate_diff
from gendiff.formatters import format_json, format_plain, format_stylish


def format_diff(diff, format_name="stylish"):
    if format_name == "stylish":
        return format_stylish(diff)
    elif format_name == "plain":
        return "\n".join(format_plain(diff))
    elif format_name == "json":
        return format_json(diff)
    else:
        raise ValueError(f"Unknown format: {format_name}")


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", metavar="first_file")
    parser.add_argument("second_file", metavar="second_file")
    parser.add_argument(
        "--format",
        default="stylish",
        choices=["stylish", "plain", "json"],
        help="set format of output",
    )

    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file)
    formatted_diff = format_diff(diff, args.format)
    print(formatted_diff)


if __name__ == "__main__":
    main()
