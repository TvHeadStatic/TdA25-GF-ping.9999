from flask import Flask, jsonify, Blueprint, request
from flask_httpauth import HTTPBasicAuth
import requests
import hashlib

from db.db_manager import db_manager

gateway_bp = Blueprint('gateway_bp', __name__)

apiURL = "https://50336bc6.app.deploy.tourde.app/api/v1/games"

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    dbMan = db_manager()
    methodQuery = "SELECT * FROM users WHERE address LIKE ?"
    dbMan.cursor.execute(methodQuery, [username])
    user = dbMan.cursor.fetchone()
    dbMan.free()
    if user != None and user["password"] == hashlib.sha256(f"{password}{user['salt']}".encode()).hexdigest():
        return username

@gateway_bp.route("/api/gateway", methods=["GET", "POST"])
@auth.login_required
def api_getall():
    match(request.method):
        case "POST":
            r = requests.post(apiURL, json=request.get_json(force=True))
            result = (jsonify(r.json()), r.status_code)
        case _:
            r = requests.get(apiURL)
            result = (jsonify(r.json()), r.status_code)
    return result

@gateway_bp.route("/api/gateway/<id>", methods=["GET", "PUT", "DELETE"])
@auth.login_required
def api(id):
    match(request.method):
        case "PUT":
            r = requests.put(f"{apiURL}/{id}", json=request.get_json(force=True))
            result = (jsonify(r.json()), r.status_code)
        case "DELETE":
            r = requests.delete(f"{apiURL}/{id}")
            result = (jsonify({ "uuid": id }), r.status_code)
        case _:
            r = requests.get(f"{apiURL}/{id}")
            result = (jsonify(r.json()), r.status_code)
    return result