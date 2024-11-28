from flask import jsonify
import sqlite3
import uuid
import datetime

from api.db_manager import db_manager
from api.ticktacktoe_functionality import validate_gamestate, has_invalid_char, has_illegal_size, has_bad_actor

def api_post(req):
    dbMan = db_manager()
    methodQuery = "INSERT INTO piskvorky(uuid, createdAt, updatedAt, name, difficulty, gameState, board) VALUES(?, ?, ?, ?, ?, ?, ?)"
    newuuid = str(uuid.uuid4())
    createdAt = str(datetime.datetime.now())
    updatedAt = str(datetime.datetime.now())
    if has_invalid_char(req["board"]) or has_illegal_size(req["board"]) or has_bad_actor(req["board"]):
        return jsonify({
            "status": 422
        }), 422
    gameState = validate_gamestate(req["board"])
    dbMan.cursor.execute(methodQuery, [newuuid, createdAt, updatedAt, req["name"], req["difficulty"], gameState, str(req["board"])])
    dbMan.conn.commit()
    dbMan.free()
    return jsonify({
        "uuid": newuuid,
        "createdAt": createdAt,
        "updatedAt": updatedAt,
        "name": req["name"],
        "difficulty": req["difficulty"],
        "gameState": gameState,
        "board": req["board"]
    }), 201
