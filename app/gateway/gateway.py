from flask import Flask, jsonify, Blueprint, request, session, url_for
from flask_httpauth import HTTPTokenAuth
import requests
import hashlib

from db.db_manager import db_manager

gateway_bp = Blueprint('gateway_bp', __name__)

auth = HTTPTokenAuth()

@auth.verify_token
def verify_token(token):
    if "user" in session and "token" in session["user"]:
        if token == session["user"]["token"]:
            return session["user"]["username"]

@gateway_bp.route("/api/gateway", methods=["GET", "POST"])
@auth.login_required
def api_getall():
    match(request.method):
        case "POST":
            r = requests.post(url_for("api_bp.api_getall", _external=True), json=request.get_json(force=True))
            result = (jsonify(r.json()), r.status_code)
        case _:
            r = requests.get(url_for("api_bp.api_getall", _external=True))
            result = (jsonify(r.json()), r.status_code)
    return result

@gateway_bp.route("/api/gateway/<id>", methods=["GET", "PUT", "DELETE"])
@auth.login_required
def api(id):
    match(request.method):
        case "PUT":
            r = requests.put(url_for("api_bp.api", id=id, _external=True), json=request.get_json(force=True))
            result = (jsonify(r.json()), r.status_code)
        case "DELETE":
            r = requests.delete(url_for("api_bp.api", id=id, _external=True))
            result = (jsonify({ "uuid": id }), r.status_code)
        case _:
            r = requests.get(url_for("api_bp.api", id=id, _external=True))
            result = (jsonify(r.json()), r.status_code)
    return result