import sqlite3

class db_manager:
    sqlDBPath = "app/db/sql.db"
    sqlInit = '''
    CREATE TABLE IF NOT EXISTS piskvorky (
        uuid TEXT PRIMARY KEY,
        createdAt DATE,
        updatedAt DATE,
        name TEXT,
        difficulty TEXT,
        gameState TEXT,
        board TEXT
    )
    '''
    conn = None
    cursor = None
    def __init__(self):
        self.conn = sqlite3.connect(self.sqlDBPath)
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.sqlInit)
    
    def __del__(self):
        self.cursor.close()
        self.conn.close()