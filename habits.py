from db import get_connection

def create_habit(name):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO habits (name) VALUES (?)", (name,))
            conn.commit()
        print(f"Habit created: '{name}'")
    except Exception as e:
        print(f"Error: Habit may already exist. ({e})")