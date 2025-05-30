import sqlite3

with sqlite3.connect("games.db") as conn:
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(games)")
    for column in cursor.fetchall():
        print(column)
