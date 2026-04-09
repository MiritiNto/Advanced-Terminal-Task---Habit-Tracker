import argparse
from db import init_db
from tasks import add_task, list_tasks, complete_task, delete_task
from habits import create_habit, log_habit, list_habits
from utils import export_tasks_csv

def main():
    init_db()
    parser = argparse.ArgumentParser(description="Advanced Task & Habit Tracker")
    subparsers = parser.add_subparsers(dest="command")
    
    parser_add = subparsers.add_parser("add")
    parser_add.add_argument("title", type=str)
    parser_add.add_argument("--priority", type=int, choices=[1,2,3], default=3)
    
    subparsers.add_parser("list")
    
    parser_done = subparsers.add_parser("done")
    parser_done.add_argument("id", type=int)
    
    parser_delete = subparsers.add_parser("delete")
    parser_delete.add_argument("id", type=int)
    
    parser_habit = subparsers.add_parser("habit")
    parser_habit.add_argument("name", type=str)
    
    parser_log = subparsers.add_parser("log")
    parser_log.add_argument("id", type=int)
    
    subparsers.add_parser("habits")
    subparsers.add_parser("export-csv")
    
    args = parser.parse_args()
    
    if args.command == "add": add_task(args.title, args.priority)
    elif args.command == "list": list_tasks()
    elif args.command == "done": complete_task(args.id)
    elif args.command == "delete": delete_task(args.id)
    elif args.command == "habit": create_habit(args.name)
    elif args.command == "log": log_habit(args.id)
    elif args.command == "habits": list_habits()
    elif args.command == "export-csv": export_tasks_csv()
    elif not args.command: parser.print_help()

if __name__ == "__main__":
    main()