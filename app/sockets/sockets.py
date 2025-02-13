from flask import url_for, session
from flask_socketio import SocketIO, emit
import requests
from db.db_manager import db_manager

socketio = SocketIO()

@socketio.on("join_game")
def player_joined(json):
    dbMan = db_manager()
    r = requests.get(url_for("api_bp.api", id=json["gameuuid"], _external=True))
    result = r.json()
    print(json["playeruuid"])
    if result["x"] == "" or result["x"] == None:
        methodQuery = "UPDATE piskvorky SET X = %s WHERE uuid LIKE %s"
        dbMan.cursor.execute(methodQuery, [json["playeruuid"], json["gameuuid"]])
        dbMan.conn.commit()
        emit("join_gamed", { "result": True })
    elif result["o"] == "" or result["o"] == None:
        methodQuery = "UPDATE piskvorky SET O = %s WHERE uuid LIKE %s"
        dbMan.cursor.execute(methodQuery, [json["playeruuid"], json["gameuuid"]])
        dbMan.conn.commit()
        emit("join_gamed", { "result": False })

@socketio.on("update_game")
def handle_my_custom_event(json):
    emit("update_me", json, broadcast=True, include_self=True)
    emit("update_turn", json, broadcast=True, include_self=False)

@socketio.on('disconnect')
def handle_my_custom_event(json):
    print(json)
    print(session["user"])
    emit("leave_game", session["user"], broadcast=True, include_self=False)
    print("player left")