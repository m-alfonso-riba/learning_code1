import argparse

def parse_args():
    parser = argparse.ArgumentParser(dest="command")

    subparsers = parser.add_subparsers()

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("text")

    subparsers.add_parser("list")

    done_parser = subparsers.add_parser("done")
    done_parser.add_argument("id", type=int)

    return parser.parse_args
