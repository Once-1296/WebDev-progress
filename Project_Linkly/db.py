# db.py
import sqlite3
import random
import json
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
 # Table for metadata
    c.execute("""
        CREATE TABLE IF NOT EXISTS meta (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    """)

    # ---- Base Key ----
    c.execute("SELECT value FROM meta WHERE key='base_key'")
    row = c.fetchone()
    if not row:
        base_key = [random.randint(0, 57) for _ in range(6)]
        c.execute("INSERT INTO meta (key, value) VALUES (?, ?)", ("base_key", json.dumps(base_key)))
        print(f"[DB INIT] Created new base key: {base_key}")
    else:
        print("[DB INIT] Existing base key loaded.")

    # ---- Cipher Map ----
    c.execute("SELECT value FROM meta WHERE key='cipher_map'")
    row = c.fetchone()
    if not row:
        numbers = list(range(58))
        shuffled = numbers.copy()
        random.shuffle(shuffled)
        cipher_map = {i: shuffled[i] for i in range(58)}
        reverse_map = {shuffled[i]: i for i in range(58)}  # reverse mapping

        c.execute("INSERT INTO meta (key, value) VALUES (?, ?)", ("cipher_map", json.dumps(cipher_map)))
        c.execute("INSERT INTO meta (key, value) VALUES (?, ?)", ("reverse_map", json.dumps(reverse_map)))
        print(f"[DB INIT] Created new cipher map + reverse map.")
    else:
        print("[DB INIT] Existing cipher map loaded.")

    conn.commit()
    conn.close()


def get_base_key():
    """Return the 6-element base key array."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT value FROM meta WHERE key='base_key'")
    row = c.fetchone()
    conn.close()
    return json.loads(row[0]) if row else None


def get_cipher_map():
    """Return the cipher map: index -> index."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT value FROM meta WHERE key='cipher_map'")
    row = c.fetchone()
    conn.close()
    return {int(k): v for k, v in json.loads(row[0]).items()} if row else None


def get_reverse_map():
    """Return the reverse cipher map: substituted index -> original index."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT value FROM meta WHERE key='reverse_map'")
    row = c.fetchone()
    conn.close()
    return {int(k): v for k, v in json.loads(row[0]).items()} if row else None

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

def get_last_short_code():
    """Return the most recently inserted short_code, or None if table empty."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT short_code FROM urls ORDER BY id DESC LIMIT 1")
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