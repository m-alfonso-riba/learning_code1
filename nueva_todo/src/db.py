import sqlite3

DB_NAME = "tasks.db"

def init_db():
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            text TEXT,
            completed INTEGER
        )
    """)

    con.commit()
    con.close()


def insert_task(text):
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    cur.execute("INSERT INTO tasks (text, completed) VALUES (?, 0)", (text,))
    con.commit()
    con.close()

def show_the_list():
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    cur.execute("SELECT id,text,completed FROM tasks")
    rows = cur.fetchall()

    con.close()
    return rows

def mark_done(task_id):
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    cur.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))
    con.commit()
    con.close()

