import argparse
from db import init_db
from tasks import add_task, list_tasks, complete_task, delete_task
from habits import create_habit

def main():
    init_db()
    parser = argparse.ArgumentParser(description="Advanced Task & Habit Tracker")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("title", type=str, help="Task title")
    parser_add.add_argument("--priority", type=int, choices=[1,2,3], default=3)
    
    parser_list = subparsers.add_parser("list", help="List all tasks")
    
    parser_done = subparsers.add_parser("done", help="Complete a task")
    parser_done.add_argument("id", type=int, help="Task ID")
    
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("id", type=int, help="Task ID")
    
    parser_habit = subparsers.add_parser("habit", help="Create a habit")
    parser_habit.add_argument("name", type=str, help="Habit name")
    
    args = parser.parse_args()
    
    if args.command == "add":
        add_task(args.title, args.priority)
    elif args.command == "list":
        list_tasks()
    elif args.command == "done":
        complete_task(args.id)
    elif args.command == "delete":
        delete_task(args.id)
    elif args.command == "habit":
        create_habit(args.name)
    elif not args.command:
        parser.print_help()

if __name__ == "__main__":
    main()