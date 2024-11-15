from flask import jsonify
import sqlite3
import uuid
import datetime

def api_post(cursor, req, conn):
    state = "INSERT INTO piskvorky(uuid, createdAt, updatedAt, name, difficulty, gameState, board) VALUES(?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(state, [str(uuid.uuid4), str(datetime.datetime.now()), str(datetime.datetime.now()), req.name, req.difficulty, None, str(req.board)])
    conn.commit()
    return req, 201
