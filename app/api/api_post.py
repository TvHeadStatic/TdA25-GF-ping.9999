from flask import jsonify
import sqlite3
import uuid

def api_post(cursor, req, conn):
    state = "INSERT INTO piskvorky(uuid, createdAt, updatedAt, name, difficulty, gameState, board) VALUES(?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(state, [str(uuid.uuid4), req.createdAt, req.updatedAt, req.name, req.difficulty, req.gameState, str(req.board)])
    conn.commit()
    return jsonify(req), 201