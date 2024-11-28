from flask import jsonify
import sqlite3
import uuid
import datetime

from api.db_manager import db_manager

def validate_gamestate(board):
    oCounter = 1
    for y in board:
        for x in y:
            oCounter += int(x =="O")
    if oCounter > 5: return "midgame"
    return "opening"

def api_post(req):
    dbMan = db_manager()
    methodQuery = "INSERT INTO piskvorky(uuid, createdAt, updatedAt, name, difficulty, gameState, board) VALUES(?, ?, ?, ?, ?, ?, ?)"
    newuuid = str(uuid.uuid4())
    createdAt = str(datetime.datetime.now())
    updatedAt = str(datetime.datetime.now())
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
