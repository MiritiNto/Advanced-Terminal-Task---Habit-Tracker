import csv
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