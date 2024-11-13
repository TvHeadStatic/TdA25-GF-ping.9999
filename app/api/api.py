from flask import Flask, jsonify, Blueprint, request
from api.api_get import api_get, api_get_all
from api.api_post import api_post
import sqlite3

sqlDBPath = "app/db/sql.db"
sqlInit = '''
    CREATE TABLE IF NOT EXISTS piskvorky (
        uuid TEXT PRIMARY KEY,
        createdAt DATE,
        updatedAt DATE,
        name TEXT,
        difficulty TEXT,
        gameState TEXT,
        board TEXT
    )
    '''

api_bp = Blueprint('api_bp', __name__)

@api_bp.route("/api")
def api_getall():
    conn = sqlite3.connect(sqlDBPath)
    cursor = conn.cursor()
    cursor.execute(sqlInit)
    result = api_get_all(cursor)
    cursor.close()
    conn.close()
    return result

@api_bp.route("/api/<id>", methods=["GET", "POST", "PUT", "DELETE"])
def api(id):
    conn = sqlite3.connect(sqlDBPath)
    cursor = conn.cursor()
    cursor.execute(sqlInit)
    match(request.method):
        case "POST": result = api_post(id, cursor)
        case "PUT": pass
        case "DELETE": pass
        case _: result = api_get(id, cursor)
    cursor.close()
    conn.close()
    return result