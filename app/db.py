import sqlite3

def init_db():
    conn = sqlite3.connect("threats.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS indicators (
            id INTEGER PRIMARY KEY,
            source TEXT,
            indicator TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def insert_indicator(source, indicator):
    conn = sqlite3.connect("threats.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO indicators (source, indicator) VALUES (?, ?)", (source, indicator))
    conn.commit()
    conn.close()
