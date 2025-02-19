from flask import session
from flask_socketio import SocketIO, emit
import requests
from ast import literal_eval
from db.db_manager import db_manager

socketio = SocketIO()

@socketio.on("join_game")
def player_joined(data):
    print("data uwu:")
    print(data)
    dbMan = db_manager()
    methodQuery = "SELECT * FROM piskvorky WHERE uuid LIKE %s"
    dbMan.cursor.execute(methodQuery, [data["gameuuid"]])
    result = dbMan.cursor.fetchone()
    result["board"] = literal_eval(result["board"])

    if result["x"] == "" or result["x"] == None:
        methodQuery = "UPDATE piskvorky SET X = %s WHERE uuid LIKE %s"
        dbMan.cursor.execute(methodQuery, [data["playeruuid"], data["gameuuid"]])
        dbMan.conn.commit()
        emit("X_joined", session["user"]["uuid"], broadcast=True, include_self=True)
        emit("join_gamed", { "result": True })
        return
    elif result["o"] == "" or result["o"] == None:
        methodQuery = "UPDATE piskvorky SET O = %s WHERE uuid LIKE %s"
        dbMan.cursor.execute(methodQuery, [data["playeruuid"], data["gameuuid"]])
        dbMan.conn.commit()
        emit("O_joined", session["user"]["uuid"], broadcast=True, include_self=True)
        emit("join_gamed", { "result": False })
        return

@socketio.on("update_game")
def update_game_b(data):
    emit("update_turn", data, broadcast=True, include_self=False)
    emit("update_me", data, broadcast=True, include_self=True)

@socketio.on('disconnect')
def disconnect_uwu(data):
    print(data)
    print(session["user"])
    emit("leave_game", session["user"], broadcast=True, include_self=False)
    print("player left")

@socketio.on('end_game')
def i_am_steve(data):
    dbMan = db_manager()

    if data["winner"] == "x":
        methodQuery = "UPDATE users SET wins = wins + 1 WHERE uuid LIKE %s"
        dbMan.cursor.execute(methodQuery, [data["x"]])
        methodQuery = "UPDATE users SET losses = losses + 1 WHERE uuid LIKE %s"
        dbMan.cursor.execute(methodQuery, [data["o"]])
        print("Cum")
        print(data)
    
    elif data["winner"] == "o":
        methodQuery = "UPDATE users SET wins = wins + 1 WHERE uuid LIKE %s"
        dbMan.cursor.execute(methodQuery, [data["o"]])
        methodQuery = "UPDATE users SET losses = losses + 1 WHERE uuid LIKE %s"
        dbMan.cursor.execute(methodQuery, [data["x"]])
        print("Piss")
        print(data)

    
    else:
        methodQuery = "UPDATE users SET draws = draws + 1 WHERE uuid LIKE %s"
        dbMan.cursor.execute(methodQuery, [data["x"]])
        dbMan.cursor.execute(methodQuery, [data["o"]])
        print("Peanut")
        print(data)


    dbMan.free()
