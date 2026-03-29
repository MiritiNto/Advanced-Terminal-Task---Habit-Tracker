import argparse

def main():
    parser = argparse.ArgumentParser(description="Advanced Task & Habit Tracker")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    args = parser.parse_args()
    if not args.command:
        parser.print_help()

if __name__ == "__main__":
    main()