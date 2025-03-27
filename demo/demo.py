"""Demo of using cli override.

Try it once with correct args and overrides and once with a misspelled argument.
"""

import argparse
from pprint import pprint
import logging

from cli_override import parse_extra_args

logging.basicConfig(level="DEBUG")


parser = argparse.ArgumentParser(description="A demo of cli overrides.")
parser.add_argument("--example", required=True)
parser.add_argument("--easy_to_mispell", default="Don't want to see me.")


def main():
    args, unknown_args = parser.parse_known_args()
    print("Defined Args")
    pprint(args)
    extra_args = parse_extra_args(unknown_args)
    print("Override Args")
    pprint(extra_args)
    parse_extra_args(unknown_args, strict=True)


if __name__ == "__main__":
    main()
