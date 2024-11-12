from flask import Flask, jsonify, Blueprint

api_bp = Blueprint('api_bp', __name__)

@api_bp.route("/api")
def api():
    return jsonify({"organization": "Student Cyber Games"}), 200