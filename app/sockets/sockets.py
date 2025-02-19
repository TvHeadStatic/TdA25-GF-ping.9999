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
        emit("X_joined", session["user"]["uuid"], broadcast=True, include_self=True)
        emit("join_gamed", { "result": True })
        return
    elif result["o"] == "" or result["o"] == None:
        methodQuery = "UPDATE piskvorky SET O = %s WHERE uuid LIKE %s"
        dbMan.cursor.execute(methodQuery, [json["playeruuid"], json["gameuuid"]])
        dbMan.conn.commit()
        emit("O_joined", session["user"]["uuid"], broadcast=True, include_self=True)
        emit("join_gamed", { "result": False })
        return

@socketio.on("update_game")
def update_game_b(json):
    emit("update_turn", json, broadcast=True, include_self=False)
    emit("update_me", json, broadcast=True, include_self=True)

@socketio.on('disconnect')
def disconnect_uwu(json):
    print(json)
    print(session["user"])
    emit("leave_game", session["user"], broadcast=True, include_self=False)
    print("player left")

@socketio.on('end_game')
def i_am_steve(json):
    dbMan = db_manager()

    if json["winner"] == "x":
        methodQuery = "UPDATE users SET wins = wins + 1 WHERE uuid LIKE %s"
        dbMan.cursor.execute(methodQuery, [json["x"]])
        methodQuery = "UPDATE users SET losses = losses + 1 WHERE uuid LIKE %s"
        dbMan.cursor.execute(methodQuery, [json["o"]])
        print("Cum")
        print(json)
    
    elif json["winner"] == "o":
        methodQuery = "UPDATE users SET wins = wins + 1 WHERE uuid LIKE %s"
        dbMan.cursor.execute(methodQuery, [json["o"]])
        methodQuery = "UPDATE users SET losses = losses + 1 WHERE uuid LIKE %s"
        dbMan.cursor.execute(methodQuery, [json["x"]])
        print("Piss")
        print(json)

    
    else:
        methodQuery = "UPDATE users SET draws = draws + 1 WHERE uuid LIKE %s"
        dbMan.cursor.execute(methodQuery, [json["x"]])
        dbMan.cursor.execute(methodQuery, [json["o"]])
        print("Peanut")
        print(json)


    dbMan.free()
