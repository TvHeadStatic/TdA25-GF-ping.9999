from flask import jsonify
import uuid
import datetime
import os

from db.db_manager import db_manager
from api.ticktacktoe_functionality import validate_gamestate, has_invalid_char, has_illegal_size, has_bad_actor

def api_post(req):
    dbMan = db_manager()
    methodQuery = "INSERT INTO piskvorky(uuid, createdAt, updatedAt, name, gameMode, gameState, board, x, o) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    newuuid = str(os.urandom(3).hex())
    createdAt = str(datetime.datetime.now())
    updatedAt = str(datetime.datetime.now())
    if has_invalid_char(req["board"]) or has_illegal_size(req["board"]) or has_bad_actor(req["board"]):
        return jsonify({
            "status": 422
        }), 422
    gameState = validate_gamestate(req["board"])
    dbMan.cursor.execute(methodQuery, [newuuid, createdAt, updatedAt, req["name"], req["gameMode"], gameState, str(req["board"]), str(""), str("")])
    dbMan.conn.commit()
    dbMan.free()
    return jsonify({
        "uuid": newuuid,
        "createdAt": createdAt,
        "updatedAt": updatedAt,
        "name": req["name"],
        "gameMode": req["gameMode"],
        "gameState": gameState,
        "board": req["board"]
    }), 201
