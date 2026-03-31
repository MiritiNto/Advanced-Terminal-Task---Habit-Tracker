from db import get_connection

def add_task(title):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
        conn.commit()
    print(f"Task added: '{title}'")

def list_tasks():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, status FROM tasks")
        for row in cursor.fetchall():
            print(f"[{row[0]}] {row[1]} - {row[2].upper()}")