import argparse

def parse_args():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest="command")


    #add
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("text")

    #list
    subparsers.add_parser("list")

    #done
    done_parser = subparsers.add_parser("done")
    done_parser.add_argument("id", type=int)

    return parser.parse_args()


