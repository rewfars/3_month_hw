import sqlite3

class Database:
    def init(self, path):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS reviews(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    phone_number TEXT,
                    rate INTEGER,
                    extra_comments TEXT
                )        
                )
            """),
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS store(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name_product TEXT,
                    size TEXT,
                    category TEXT,
                    price INTEGER,
                    photo TEXT,
                    product_id INTEGER
                )
            """),
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS product_deatil(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id INTEGER,
                    category TEXT,
                    infoproduct TEXT
                )
            """)
            conn.commit()