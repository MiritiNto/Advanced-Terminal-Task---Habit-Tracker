import argparse
from db import init_db
from tasks import add_task, list_tasks

def main():
    init_db()
    parser = argparse.ArgumentParser(description="Advanced Task & Habit Tracker")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("title", type=str, help="Task title")
    
    parser_list = subparsers.add_parser("list", help="List all tasks")
    
    args = parser.parse_args()
    
    if args.command == "add":
        add_task(args.title)
    elif args.command == "list":
        list_tasks()
    elif not args.command:
        parser.print_help()

if __name__ == "__main__":
    main()