from flask import Flask, jsonify, session
import uuid
import hashlib
import random
import datetime

from db.db_manager import db_manager

def users_put(id, req):
    dbMan = db_manager()

    methodQuery = "UPDATE users SET email = %s, username = %s, password = %s, salt = %s, elo = %s, wins = %s, draws = %s, losses = %s WHERE uuid LIKE %s"
    salt = hex(random.randrange(0, 2**24))
    newPassword = hashlib.sha256(f"{req['password']}{salt}".encode()).hexdigest()
    dbMan.cursor.execute(methodQuery, [req["email"], req["username"], newPassword, salt, req["elo"], req["wins"], req["draws"], req["losses"]])

    methodQuery = "SELECT users.uuid, users.createdAt, users.username, users.elo, users.wins, users.draws, users.losses FROM users WHERE uuid LIKE %s"
    dbMan.cursor.execute(methodQuery, [id])
    result = dbMan.cursor.fetchone()
    dbMan.free()

    if "user" in session:
        if req["email"] != None: session["user"]["email"] = req["email"]
        if req["username"] != None: session["user"]["username"] = req["username"]

    return jsonify(result), 200