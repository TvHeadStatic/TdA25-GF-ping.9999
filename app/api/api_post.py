from flask import jsonify
import sqlite3
import uuid
import datetime

from api.db_manager import db_manager

def api_post(req):
    dbMan = db_manager()
    methodQuery = "INSERT INTO piskvorky(uuid, createdAt, updatedAt, name, difficulty, gameState, board) VALUES(?, ?, ?, ?, ?, ?, ?)"
    newuuid = str(uuid.uuid4())
    createdAt = str(datetime.datetime.now())
    updatedAt = str(datetime.datetime.now())
    dbMan.cursor.execute(methodQuery, [newuuid, createdAt, updatedAt, req["name"], req["difficulty"], None, str(req["board"])])
    dbMan.conn.commit()
    dbMan.free()
    return jsonify({
        "uuid": newuuid,
        "createdAt": createdAt,
        "updatedAt": updatedAt,
        "name": req["name"],
        "difficulty": req["difficulty"],
        "gameState": None,
        "board": req["board"]
    }), 201
