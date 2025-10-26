# db.py
import sqlite3
import random
import json


class my_db:

    DB_NAME = ""

    def __init__(self, s: str):
        """Constructor"""
        self.DB_NAME = s
        self.conn = sqlite3.connect(self.DB_NAME, check_same_thread=False)
        self.c = self.conn.cursor()

    def init_db(self):
        """Initialize the database and create the urls table if not exists."""

        self.c.execute(
            """
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                long_url TEXT UNIQUE NOT NULL,
                short_code TEXT UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                click_count INTEGER DEFAULT 0 NOT NULL
            )
        """
        )
        # Table for metadata
        self.c.execute(
            """
            CREATE TABLE IF NOT EXISTS meta (
                key TEXT PRIMARY KEY,
                value TEXT
            )
        """
        )
        # ---- Base Key ----
        self.c.execute("SELECT value FROM meta WHERE key='base_key'")
        row = self.c.fetchone()
        if not row:
            base_key = [random.randint(0, 57) for _ in range(6)]
            self.c.execute(
                "INSERT INTO meta (key, value) VALUES (?, ?)",
                ("base_key", json.dumps(base_key)),
            )
            print(f"[DB INIT] Created new base key: {base_key}")
        else:
            print("[DB INIT] Existing base key loaded.")

        # ---- Cipher Map ----
        self.c.execute("SELECT value FROM meta WHERE key='cipher_map'")
        row = self.c.fetchone()
        if not row:
            numbers = list(range(58))
            shuffled = numbers.copy()
            random.shuffle(shuffled)
            cipher_map = {i: shuffled[i] for i in range(58)}
            reverse_map = {shuffled[i]: i for i in range(58)}  # reverse mapping

            self.c.execute(
                "INSERT INTO meta (key, value) VALUES (?, ?)",
                ("cipher_map", json.dumps(cipher_map)),
            )
            self.c.execute(
                "INSERT INTO meta (key, value) VALUES (?, ?)",
                ("reverse_map", json.dumps(reverse_map)),
            )
            print(f"[DB INIT] Created new cipher map + reverse map.")
        else:
            print("[DB INIT] Existing cipher map loaded.")

        self.conn.commit()

    # expiration of links
    def _cleanup_old_entries(self):
        """Delete URL records older than 30 days."""
        self.c.execute(
            """
            DELETE FROM urls 
            WHERE julianday('now') - julianday(created_at) >= 30
            """
        )
        self.conn.commit()

    def increment_click_count(self, short_code):
        """Increment click count for a given short_code."""
        self.c.execute(
            "UPDATE urls SET click_count = click_count + 1 WHERE short_code = ?",
            (short_code,),
        )
        self.conn.commit()

    def get_click_count(self, short_code):
        """Fetch the original long URL for a given short code."""
        self.c.execute(
            "SELECT click_count FROM urls WHERE short_code = ?", (short_code,)
        )
        row = self.c.fetchone()
        return row[0] if row else None

    # helper functions for retrieving database parameters
    def get_base_key(self):
        """Return the 6-element base key array."""
        self.c.execute("SELECT value FROM meta WHERE key='base_key'")
        row = self.c.fetchone()
        return json.loads(row[0]) if row else None

    def get_cipher_map(self):
        """Return the cipher map: index -> index."""
        self.c.execute("SELECT value FROM meta WHERE key='cipher_map'")
        row = self.c.fetchone()
        return {int(k): v for k, v in json.loads(row[0]).items()} if row else None

    def get_reverse_map(self):
        """Return the reverse cipher map: substituted index -> original index."""
        self.c.execute("SELECT value FROM meta WHERE key='reverse_map'")
        row = self.c.fetchone()
        return {int(k): v for k, v in json.loads(row[0]).items()} if row else None

    # insertion and retrieval of urls/codes
    def insert_url(self, long_url, short_code):
        """Insert a new long-short mapping."""
        self.c.execute(
            "INSERT INTO urls (long_url, short_code) VALUES (?, ?)",
            (long_url, short_code),
        )
        self.conn.commit()

    def get_long_url(self, short_code):
        """Fetch the original long URL for a given short code."""
        self.c.execute("SELECT long_url FROM urls WHERE short_code = ?", (short_code,))
        row = self.c.fetchone()
        return row[0] if row else None

    def get_short_code(self, long_url):
        """Check if a long URL already has a short code."""
        self.c.execute("SELECT short_code FROM urls WHERE long_url = ?", (long_url,))
        row = self.c.fetchone()
        return row[0] if row else None

    def get_last_short_code(self):
        """Return the most recently inserted short_code, or None if table empty."""
        self.c.execute("SELECT short_code FROM urls ORDER BY id DESC LIMIT 1")
        row = self.c.fetchone()
        return row[0] if row else None

    def get_all_urls(self):
        """Returns list of all urls:code pairs for debugging"""
        self.c.execute("SELECT long_url,short_code FROM urls")
        rows = self.c.fetchall()
        return rows if rows else None

    def __del__(self):
        """Destructor"""
        self.conn.close()


my_db = my_db("urls.db")
my_db.init_db()
