import os
import psycopg2
from psycopg2.extras import RealDictCursor

class db_manager:
    sqlInitPiskvorky = '''
    CREATE TABLE IF NOT EXISTS piskvorky (
        uuid VARCHAR(36) PRIMARY KEY,
        createdAt DATE,
        updatedAt DATE,
        name TEXT,
        difficulty TEXT,
        gameState TEXT,
        board TEXT
    )
    '''
    sqlInitUsers = '''
    CREATE TABLE IF NOT EXISTS users (
        address VARCHAR(36) PRIMARY KEY,
        username TEXT,
        password TEXT,
        salt TEXT
    )
    '''
    conn = None
    cursor = None
    
    def __init__(self):
        print("[uwu] database has been opened")
        self.conn = psycopg2.connect(
            user=str(os.getenv("DB_USER")),
            password=str(os.getenv("DB_PASS")),
            host=str(os.getenv("DB_HOST")),
            port=str(os.getenv("DB_PORT")),
            dbname=str(os.getenv("DB_NAME"))
        )
        self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        self.cursor.execute(self.sqlInitPiskvorky)
        self.cursor.execute(self.sqlInitUsers)
    
    def free(self):
        print("[owo] database has been closed")
        self.cursor.close()
        self.conn.close()