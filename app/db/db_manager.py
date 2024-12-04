import sqlite3

def dict_factory(cursor, row):
    fields = [x[0] for x in cursor.description]
    return {key: value for key, value in zip(fields, row)}

class db_manager:
    sqlDBPath = "app/db/games.db"
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
        self.conn = sqlite3.connect(self.sqlDBPath)
        self.conn.row_factory = dict_factory
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.sqlInitPiskvorky)
        self.cursor.execute(self.sqlInitUsers)
    
    def free(self):
        print("[owo] database has been closed")
        self.cursor.close()
        self.conn.close()