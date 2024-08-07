import argparse

from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", metavar="first_file")
    parser.add_argument("second_file", metavar="second_file")
    parser.add_argument(
        "--format", "-f",
        default="stylish",
        choices=["stylish", "plain", "json"],
        help="set format of output",
    )

    args = parser.parse_args()

    formatted_diff = generate_diff(args.first_file, args.second_file, args.format)
    print(formatted_diff)


if __name__ == "__main__":
    main()
