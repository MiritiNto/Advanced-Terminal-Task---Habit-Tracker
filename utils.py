import csv
import json
from db import get_connection

def export_tasks_csv(filename="tasks.csv"):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()
        
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Title", "Status", "Priority"])
        writer.writerows(rows)
    print(f"Exported to {filename}")

def export_tasks_json(filename="tasks.json"):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()
        
    data = [{"id": r[0], "title": r[1], "status": r[2], "priority": r[3]} for r in rows]
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Exported to {filename}")