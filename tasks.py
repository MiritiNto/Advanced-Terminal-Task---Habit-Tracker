from db import get_connection

def add_task(title):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
        conn.commit()
    print(f"Task added: '{title}'")