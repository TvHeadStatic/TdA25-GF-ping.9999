from flask import Flask, jsonify
import uuid

from db.db_manager import db_manager

def users_delete(id):
    dbMan = db_manager()
    methodQuery = "DELETE FROM users WHERE uuid LIKE %s"
    dbMan.cursor.execute(methodQuery, [id])
    dbMan.conn.commit()
    dbMan.free()
    return jsonify({
        "uuid": id
    }), 204