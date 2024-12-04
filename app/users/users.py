from flask import Flask, jsonify, Blueprint, request

import hashlib
import random

from db.db_manager import db_manager

users_bp = Blueprint('users_bp', __name__)

@users_bp.route("/api/users/register", methods=["POST"])
def api_register():
    if "@" not in str(request.json["address"]):
        return jsonify({ "status": 401, "reason": "this 'e-mail address' we received is... not an e-mail address" }), 401
    
    dbMan = db_manager()
    methodQuery = "SELECT * FROM users WHERE address LIKE ?"
    dbMan.cursor.execute(methodQuery, [request.json["address"]])
    result = dbMan.cursor.fetchone()
    if result != None:
        return jsonify({ "status": 401, "reason": "a user with this e-mail address already exists" }), 401

    methodQuery = "INSERT INTO users(address, username, password, salt) VALUES(?, ?, ?, ?)"
    salt = hex(random.randrange(0, 2**24))
    newPassword = hashlib.sha256(f"{request.json['password']}{salt}".encode()).hexdigest()
    dbMan.cursor.execute(methodQuery, [request.json["address"], request.json["username"], newPassword, salt])
    dbMan.conn.commit()
    dbMan.free()
    return jsonify({
        "address": request.json["address"],
        "username": request.json["username"],
    }), 201