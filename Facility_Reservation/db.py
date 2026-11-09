import config
import sqlite3

def get_connection():
    conn = sqlite3.connect(config.DB_PATH)
    return conn

def init_db():
    conn = get_connection()
    with open("schema.sql") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()



