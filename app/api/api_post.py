from flask import jsonify
import sqlite3
import uuid
import datetime

from api.db_manager import db_manager

def api_post(req):
    dbMan = db_manager()
    state = "INSERT INTO piskvorky(uuid, createdAt, updatedAt, name, difficulty, gameState, board) VALUES(?, ?, ?, ?, ?, ?, ?)"
    dbMan.cursor.execute(state, [str(uuid.uuid4), str(datetime.datetime.now()), str(datetime.datetime.now()), req["name"], req["difficulty"], None, str(req["board"])])
    dbMan.conn.commit()
    return req, 201
