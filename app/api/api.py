from flask import Flask, jsonify, Blueprint, request
from api.api_get import api_get, api_get_all
from api.api_post import api_post
from api.api_delete import api_delete
import sqlite3

api_bp = Blueprint('api_bp', __name__)

@api_bp.route("/api/v1/games", methods=["GET", "POST"])
def api_getall():
    match(request.method):
        case "POST": result = api_post(request.get_json(force=True))
        case _: result = api_get_all()
    return result

@api_bp.route("/api/v1/games/<id>", methods=["GET", "PUT", "DELETE"])
def api(id):
    match(request.method):
        case "PUT": pass
        case "DELETE": result = api_delete(id)
        case _: result = api_get(id)
    return result
