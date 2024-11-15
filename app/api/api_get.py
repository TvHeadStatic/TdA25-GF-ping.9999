from flask import jsonify
import sqlite3

from api.db_manager import db_manager

def api_get_all():
    return jsonify({"organization": "Student Cyber Games"}), 200

def api_get(id):
    return jsonify({"organization": "Student Cyber Games"}), 200