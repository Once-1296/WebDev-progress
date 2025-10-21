# db.py
import sqlite3

DB_NAME = "urls.db"

def init_db():
    """Initialize the database and create the urls table if not exists."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            long_url TEXT UNIQUE NOT NULL,
            short_code TEXT UNIQUE NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_url(long_url, short_code):
    """Insert a new long-short mapping."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO urls (long_url, short_code) VALUES (?, ?)", (long_url, short_code))
    conn.commit()
    conn.close()

def get_long_url(short_code):
    """Fetch the original long URL for a given short code."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT long_url FROM urls WHERE short_code = ?", (short_code,))
    row = c.fetchone()
    conn.close()
    return row[0] if row else None

def get_short_code(long_url):
    """Check if a long URL already has a short code."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT short_code FROM urls WHERE long_url = ?", (long_url,))
    row = c.fetchone()
    conn.close()
    return row[0] if row else None

def get_all_urls():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT long_url,short_code FROM urls")
    rows = c.fetchall()
    conn.close()
    return rows if rows else None