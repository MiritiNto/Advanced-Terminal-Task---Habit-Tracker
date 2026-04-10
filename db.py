import sqlite3

DB_NAME = "tracker.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                status TEXT DEFAULT 'pending',
                priority INTEGER DEFAULT 3,
                due_date DATE
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS habits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS habit_logs (
                habit_id INTEGER,
                log_date DATE DEFAULT CURRENT_DATE,
                PRIMARY KEY (habit_id, log_date),
                FOREIGN KEY (habit_id) REFERENCES habits(id)
            )
        ''')
        conn.commit()