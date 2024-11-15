from flask import jsonify
import sqlite3
import json

from api.db_manager import db_manager

def api_get_all():
    dbMan = db_manager()
    methodQuery = "SELECT * FROM piskvorky"
    dbMan.cursor.execute(methodQuery)
    result = dbMan.cursor.fetchall()
    for i in range(len(result)):
        result[i]["board"] = json.loads(result[i]["board"])
    dbMan.free()
    return jsonify(result), 200

def api_get(id):
    dbMan = db_manager()
    methodQuery = "SELECT * FROM piskvorky WHERE uuid LIKE ?"
    dbMan.cursor.execute(methodQuery, [id])
    result = dbMan.cursor.fetchone()
    if result is None: return jsonify({ "response": 404 }), 404
    result["board"] = json.loads(result["board"])
    dbMan.free()
    return jsonify(result), 200