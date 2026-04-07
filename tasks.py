from db import get_connection

def add_task(title, priority=3):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (title, priority) VALUES (?, ?)", (title, priority))
        conn.commit()
    print(f"Task added: '{title}' [Priority: {priority}]")

def list_tasks():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, status, priority FROM tasks ORDER BY priority ASC")
        for row in cursor.fetchall():
            print(f"[{row[0]}] {row[1]} - {row[2].upper()} (P{row[3]})")

def complete_task(task_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET status = 'done' WHERE id = ?", (task_id,))
        conn.commit()
    print(f"Task {task_id} marked as done.")

def delete_task(task_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
    print(f"Task {task_id} deleted.")