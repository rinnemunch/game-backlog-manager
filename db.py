import sqlite3

DB_NAME = "games.db"


def create_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            platform TEXT,
            genre TEXT,
            status TEXT,
            hours_played INTEGER
        )
    """)
    conn.commit()
    conn.close()


def add_game(title, platform, genre, status, hours_played):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO games (title, platform, genre, status, hours_played)
        VALUES (?, ?, ?, ?, ?)
    """, (title, platform, genre, status, hours_played))
    conn.commit()
    conn.close()
    print(f"✅ '{title}' added to backlog.")


def get_all_games():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM games")
    rows = cursor.fetchall()
    conn.close()
    return rows


def filter_by_status(status):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM games WHERE status = ?", (status,))
    rows = cursor.fetchall()
    conn.close()
    return rows


def filter_by_platform(platform):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM games WHERE platform = ?", (platform,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_game(game_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM games WHERE id = ?", (game_id,))
    conn.commit()
    conn.close()
    print(f"🗑️ Game with ID {game_id} deleted.")

