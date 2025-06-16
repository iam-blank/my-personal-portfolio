query= '''CREATE TABLE IF NOT EXISTS contact (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    name TEXT NOT NULL,
    message TEXT NOT NULL
)
'''
import sqlite3

def createTable():
    conn = sqlite3.connect("database.db")
    # conn.row_factory = sqlite3.row()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()
    print("Table created successfully!")

createTable()
