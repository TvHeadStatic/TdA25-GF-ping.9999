from flask import jsonify
import sqlite3

def api_post(id, cursor):
    return jsonify({"organization": "Student Cyber Games"}), 200