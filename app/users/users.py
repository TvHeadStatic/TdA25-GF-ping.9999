from flask import Flask, jsonify, Blueprint, request, redirect, session, url_for
from users.users_post import users_post
from users.users_get import users_get, users_get_all
from users.users_put import users_put
from users.users_delete import users_delete

import uuid
import hashlib
import random
import datetime

from db.db_manager import db_manager

users_bp = Blueprint('users_bp', __name__)

@users_bp.route("/api/v1/users", methods=["POST", "GET"])
def api_users():
    match(request.method):
        case "POST": return users_post(request.get_json(force=True))
        case _: return users_get_all()

@users_bp.route("/api/v1/users/<id>", methods=["PUT", "GET", "DELETE"])
def api_user(id):
    match(request.method):
        case "PUT": return users_put(id, request.get_json(force=True))
        case "DELETE": return users_delete(id)
        case _: return users_get(id)

@users_bp.route("/api/v1/users/login", methods=["POST"])
def api_login():
    if "user" in session:
        return jsonify({
            "response": "session already active, you're good to go",
            "token": session["user"]["token"],
        }), 201
    if request.json["email"] == "" or request.json["password"] == "":
        return jsonify({ "status": 401, "reason": "1 or more fields are empty" }), 401
    if "@" not in str(request.json["email"]) and "." not in str(request.json["email"]) and len(str(request.json["email"])) < 5:
        return jsonify({ "status": 401, "reason": "this 'e-mail address' is... not an e-mail email" }), 401
    if " " in str(request.json["password"]) and len(str(request.json["password"])) < 8:
        return jsonify({ "status": 401, "reason": "password should be atleast 8 characters long and contain no whitespace" }), 401
    
    dbMan = db_manager()
    methodQuery = "SELECT * FROM users WHERE email = %s"
    dbMan.cursor.execute(methodQuery, [request.json["email"]])
    result = dbMan.cursor.fetchone()
    dbMan.conn.commit()
    dbMan.free()

    if result == None or hashlib.sha256(f"{request.json['password']}{result['salt']}".encode()).hexdigest() != result['password']:
        return jsonify({ "status": 401, "reason": "incorrect e-mail or password" }), 401

    newsessiontoken = str(uuid.uuid4())

    session.permanent = True
    session["user"] = {
        "uuid": result["uuid"],
        "email": request.json["email"],
        "username": result["username"],
        "token": newsessiontoken,
    }
    return jsonify({
        "email": request.json["email"],
        "username": result["username"],
        "token": newsessiontoken,
    }), 201

@users_bp.route("/api/v1/users/signout")
def api_signout():
    if "user" in session:
        session.pop("user", None)
    return jsonify({
        "response": "all good meister, see you later"
    }), 201