from flask import jsonify

from db.db_manager import db_manager

def api_delete(id):
    dbMan = db_manager()
    methodQuery = "DELETE FROM piskvorky WHERE uuid LIKE %s"
    dbMan.cursor.execute(methodQuery, [id])
    dbMan.conn.commit()
    dbMan.free()
    return jsonify({
        "uuid": id
    }), 204