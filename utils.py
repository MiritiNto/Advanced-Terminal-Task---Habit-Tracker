import csv
import json
import shutil
from db import get_connection, DB_NAME

def export_tasks_csv(filename="tasks.csv"):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Title", "Status", "Priority", "Due Date"])
        writer.writerows(rows)
    print(f"Exported to {filename}")

def export_tasks_json(filename="tasks.json"):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()
    data = [{"id": r[0], "title": r[1], "status": r[2]} for r in rows]
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Exported to {filename}")

def backup_db():
    shutil.copyfile(DB_NAME, f"{DB_NAME}.bak")
    print("Database backed up successfully.")