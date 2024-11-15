import sqlite3

class db_manager:
    sqlDBPath = "app/db/sql.db"
    sqlInit = '''
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
    conn = None
    cursor = None

    def dict_factory(cursor, row):
        fields = [x[0] for x in cursor.description]
        return {key: value for key, value in zip(fields, row)}

    def __init__(self):
        self.conn = sqlite3.connect(self.sqlDBPath)
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.sqlInit)
        self.conn.row_factory = self.dict_factory
    
    def free(self):
        print("owo")
        self.cursor.close()
        self.conn.close()