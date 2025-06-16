import sqlite3

def get_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row  # Enables dictionary-like access to columns
    return conn

query = '''SELECT * FROM contact'''

def show_rows():
    conn = get_connection()
    cursor = conn.cursor()
    rows = cursor.execute(query).fetchall()

    for row in rows:
        # You can print like a dict: row['email'], row['name'], row['message']
        print(f"ID: {row['id']} | Name: {row['name']} | Email: {row['email']} | Message: {row['message']}")

    conn.close()

# Call the function
show_rows()
