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

def users_search():
    conn = sqlite3.connect(config.db_name)
    c = conn.cursor()
    c.execute('create table if not exists users_answers (id integer primary key autoincrement, answer text, user_id integer)')
    users = c.fetchall()
    conn.close()
    return users


def create_user(name, chat_id, user_id):
    conn = sqlite3.connect(config.db_name)
    c = conn.cursor()
    c.execute('INSERT INTO users (name, chat_id, user_id) VALUES (?, ?, ?)', (name, chat_id, user_id))
    conn.commit()
    conn.close()

def write_user_answer(user_id, answer):
    conn = sqlite3.connect(config.db_name)
    c = conn.cursor()
    c.execute('INSERT INTO users_answers (user_id, answer) VALUES (?, ?)', (user_id, answer))
    conn.commit()
    conn.close()


def get_user(user_id):
    conn = sqlite3.connect(config.db_name)
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE user_id=?', (user_id,))
    user = c.fetchone()
    conn.close()
    return user

def update_user(user_id, name):
    conn = sqlite3.connect(config.db_name)
    c = conn.cursor()
    c.execute('UPDATE users SET name=? WHERE user_id=?', (name, user_id))
    conn.commit()
    conn.close()

def delete_user(user_id):
    conn = sqlite3.connect(config.db_name)
    c = conn.cursor()
    c.execute('DELETE FROM users WHERE user_id=?', (user_id,))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_db()
    users_search()