from flask import jsonify
import sqlite3

def api_get_all(cursor):
    return jsonify({"organization": "Student Cyber Games"}), 200

def api_get(id, cursor):
    return jsonify({"organization": "Student Cyber Games"}), 200