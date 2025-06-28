import sqlite3
import config

def create_db():
    conn = sqlite3.connect(config.db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        chat_id INTEGER,
        user_id INTEGER
    )''')
    conn.commit()
    conn.close()


def create_user(name, chat_id, user_id):
    conn = sqlite3.connect(config.db_name)
    c = conn.cursor()
    c.execute('INSERT INTO users (name, chat_id, user_id) VALUES (?, ?, ?)', (name, chat_id, user_id))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_db()