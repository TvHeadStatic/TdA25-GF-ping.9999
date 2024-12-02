from flask import Flask, jsonify, Blueprint, request
import requests

gateway_bp = Blueprint('gateway_bp', __name__)

apiURL = "https://50336bc6.app.deploy.tourde.app/api/v1/games"

@gateway_bp.route("/api/gateway", methods=["GET", "POST"])
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