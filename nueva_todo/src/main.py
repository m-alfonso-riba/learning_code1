from cli import parse_args
from services import create_task,show_list,mark_as_done
from db import init_db


def main():
    init_db()

    args = parse_args()

    if args.command == "add":
        create_task(args.text)
        print("Tarea añadida")

    elif args.command == "list":
        tasks = show_list()
        for t in tasks:
            status = "✓" if t.completed else " "
            print(f"{t.id} - {t.text} [{status}]")

    elif args.command == "done":
        mark_as_done(args.id)
        print("Tarea completada")


if __name__ == "__main__":
    main()


