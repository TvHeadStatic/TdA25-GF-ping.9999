from flask import Flask, jsonify

from db.db_manager import db_manager

def users_get_all():
    dbMan = db_manager()
    methodQuery = "SELECT users.uuid, users.createdAt, users.username, users.elo, users.wins, users.draws, users.losses FROM users"
    dbMan.cursor.execute(methodQuery)
    result = dbMan.cursor.fetchall()
    dbMan.free()
    return jsonify(result), 200

def users_get(id):
    dbMan = db_manager()
    methodQuery = "SELECT users.uuid, users.createdAt, users.username, users.elo, users.wins, users.draws, users.losses FROM users WHERE uuid LIKE %s"
    dbMan.cursor.execute(methodQuery, [id])
    result = dbMan.cursor.fetchone()
    if result is None: return jsonify({ "response": 404 }), 404
    dbMan.free()
    return jsonify(result), 200