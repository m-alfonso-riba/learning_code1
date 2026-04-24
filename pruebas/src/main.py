from services import create_task, show_the_list, mark_as_done
from db import init_db
from cli import parse_args

def main():
    init_db()

    args = parse_args()

    if args.command == "add":
        create_task(args.text)
        print("Creando tarea")

    elif args.command == "list":
        rows = show_the_list()
        for i in rows:
            status = "✓" if i.completed else " "
            print(f"{i.id} - {i.text} [{status}]")

    elif args.command == "done":
        mark_as_done(args.id)
        print("Tarea completada!")

if __name__ == "__main__":
    main()