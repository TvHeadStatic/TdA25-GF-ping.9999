from flask import Flask, jsonify, Blueprint, request, redirect, session, url_for

import uuid
import hashlib
import random

from db.db_manager import db_manager

users_bp = Blueprint('users_bp', __name__)

@users_bp.route("/api/users/login", methods=["POST"])
def api_login():
    if "user" in session:
        return jsonify({
            "response": "session already active, you're good to go",
            "token": newsessiontoken,
        }), 201
    if request.json["address"] == "" or request.json["password"] == "":
        return jsonify({ "status": 401, "reason": "1 or more fields are empty" }), 401
    if "@" not in str(request.json["address"]) and "." not in str(request.json["address"]) and len(str(request.json["address"])) < 5:
        return jsonify({ "status": 401, "reason": "this 'e-mail address' is... not an e-mail address" }), 401
    if " " in str(request.json["password"]) and len(str(request.json["password"])) < 8:
        return jsonify({ "status": 401, "reason": "password should be atleast 8 characters long and contain no whitespace" }), 401
    
    dbMan = db_manager()
    methodQuery = "SELECT * FROM users WHERE address = ?"
    dbMan.cursor.execute(methodQuery, [request.json["address"]])
    result = dbMan.cursor.fetchone()
    dbMan.conn.commit()
    dbMan.free()

    if result == None or hashlib.sha256(f"{request.json['password']}{result['salt']}".encode()).hexdigest() != result['password']:
        return jsonify({ "status": 401, "reason": "incorrect e-mail or password" }), 401

    newsessiontoken = str(uuid.uuid4())

    session.permanent = True
    session["user"] = {
        "address": request.json["address"],
        "username": result["username"],
        "token": newsessiontoken,
    }
    return jsonify({
        "address": request.json["address"],
        "username": result["username"],
        "token": newsessiontoken,
    }), 201

@users_bp.route("/api/users/register", methods=["POST"])
def api_register():
    if request.json["username"] == "" or request.json["address"] == "" or request.json["password"] == "":
        return jsonify({ "status": 401, "reason": "1 or more fields are empty" }), 401
    if "@" not in str(request.json["address"]) and "." not in str(request.json["address"]) and len(str(request.json["address"])) < 5:
        print(len(str(request.json["address"])))
        return jsonify({ "status": 401, "reason": "this 'e-mail address' is... not an e-mail address" }), 401
    if " " in str(request.json["password"]) and len(str(request.json["password"])) < 8:
        return jsonify({ "status": 401, "reason": "password should be atleast 8 characters long and contain no whitespace" }), 401
    
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

    session["user"] = {
        "address": request.json["address"],
        "username": request.json["username"],
    }
    return jsonify({
        "address": request.json["address"],
        "username": request.json["username"],
    }), 201

@users_bp.route("/api/users/signout")
def api_signout():
    if "user" in session:
        session.pop("user", None)
    return jsonify({
        "response": "all good meister, see you later"
    }), 201