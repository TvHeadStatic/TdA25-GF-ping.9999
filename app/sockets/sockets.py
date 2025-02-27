from flask import session
from flask_socketio import SocketIO, emit
import requests
from math import ceil
from ast import literal_eval
from db.db_manager import db_manager
import json

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
    session["user"]["lastgame"] = data["gameuuid"]
    if result["x"] == "" or result["x"] == None:
        methodQuery = "UPDATE piskvorky SET X = %s WHERE uuid LIKE %s"
        dbMan.cursor.execute(methodQuery, [data["playeruuid"], data["gameuuid"]])
        dbMan.conn.commit()
        emit("X_joined", session["user"]["uuid"], broadcast=True, include_self=True)
        emit("join_gamed", { "result": True })
        dbMan.free()
        return
    elif result["o"] == "" or result["o"] == None:
        methodQuery = "UPDATE piskvorky SET O = %s WHERE uuid LIKE %s"
        dbMan.cursor.execute(methodQuery, [data["playeruuid"], data["gameuuid"]])
        dbMan.conn.commit()
        emit("O_joined", session["user"]["uuid"], broadcast=True, include_self=True)
        emit("join_gamed", { "result": False })
        dbMan.free()
        return

@socketio.on("update_game")
def update_game_b(data):
    if "premature" in data:
        emit("show_pre_loss", data, broadcast=True, include_self=False)
    emit("update_turn", data, broadcast=True, include_self=False)
    emit("update_me", data, broadcast=True, include_self=True)

@socketio.on('disconnect')
def disconnect_uwu(data):
    if "user" in session:
        if "isguest" in session["user"]:
            session.pop("user", None)
    print(data)
    print(session["user"])
    emit("leave_game", session["user"], broadcast=True, include_self=False)
    dbMan = db_manager()
    methodQuery = "DELETE FROM piskvorky WHERE uuid LIKE %s"
    dbMan.cursor.execute(methodQuery, [session["user"]["lastgame"]])
    dbMan.conn.commit()
    dbMan.free()
    print("player left")

@socketio.on('end_game')
def i_am_steve(data):
    dbMan = db_manager()
    methodQuery = "SELECT users.username, users.elo FROM users WHERE uuid LIKE %s"
    dbMan.cursor.execute(methodQuery, [session["user"]["uuid"]])
    myResult = dbMan.cursor.fetchone()
    if data["mode"] == "private":
        print("privát ;3")
        return
    if data["winner"] == "x":
        dbMan.cursor.execute(methodQuery, [data["o"]])
        opResult = dbMan.cursor.fetchone()
        methodQuery = "UPDATE users SET wins = wins + 1 WHERE uuid LIKE %s"
        dbMan.cursor.execute(methodQuery, [data["x"]])
        dbMan.conn.commit()
        methodQuery = "UPDATE users SET losses = losses + 1 WHERE uuid LIKE %s"
        dbMan.cursor.execute(methodQuery, [data["o"]])
        dbMan.conn.commit()
        calculate_elo(data["x"], data["o"], 1)
        calculate_elo(data["o"], data["x"], 0)
        append_game_to_history(session["user"]["username"], opResult["username"], myResult["elo"], session["user"]["uuid"], data["o"], " - win")
        append_game_to_history(opResult["username"], session["user"]["username"], opResult["elo"], data["o"], session["user"]["uuid"], " - loss")
        print("Cum")
        print(data)
    elif data["winner"] == "o":
        dbMan.cursor.execute(methodQuery, [data["x"]])
        opResult = dbMan.cursor.fetchone()
        methodQuery = "UPDATE users SET wins = wins + 1 WHERE uuid LIKE %s"
        dbMan.cursor.execute(methodQuery, [data["o"]])
        dbMan.conn.commit()
        methodQuery = "UPDATE users SET losses = losses + 1 WHERE uuid LIKE %s"
        dbMan.cursor.execute(methodQuery, [data["x"]])
        dbMan.conn.commit()
        calculate_elo(data["x"], data["o"], 0)
        calculate_elo(data["o"], data["x"], 1)
        append_game_to_history(session["user"]["username"], opResult["username"], myResult["elo"], session["user"]["uuid"], data["x"], " - win")
        append_game_to_history(opResult["username"], session["user"]["username"], opResult["elo"], data["x"], session["user"]["uuid"], " - loss")
        print("Piss")
        print(data)
    else:
        methodQuery = "UPDATE users SET draws = draws + 1 WHERE uuid LIKE %s"
        dbMan.cursor.execute(methodQuery, [data["x"]])
        dbMan.conn.commit()
        dbMan.cursor.execute(methodQuery, [data["o"]])
        dbMan.conn.commit()
        calculate_elo(data["x"], data["o"], 0.5)
        calculate_elo(data["o"], data["x"], 0.5)
        append_game_to_history(session["user"]["username"], opResult["username"], myResult["elo"], session["user"]["uuid"], data["x"], " - draw")
        append_game_to_history(opResult["username"], session["user"]["username"], opResult["elo"], data["x"], session["user"]["uuid"], " - draw")
        print("Peanut")
        print(data)
    dbMan.free()


def append_game_to_history(myname, opname, myelo, myuuid, opuuid, gameresult):
    dbMan = db_manager()
    methodQuery = "UPDATE users SET \"gameHistory\" = %s::jsonb || \"gameHistory\" WHERE uuid LIKE %s"
    dbMan.cursor.execute(methodQuery, [json.dumps({"title": str(myname + " Vs. " + opname + gameresult), "opid": opuuid, "elo": myelo}), myuuid])
    dbMan.conn.commit()
    dbMan.free()

def calculate_elo(playerId, opponentId, realScore):
    dbMan = db_manager()
    methodQuery = "SELECT users.elo, users.wins, users.draws, users.losses FROM users WHERE uuid LIKE %s"
    dbMan.cursor.execute(methodQuery, [playerId])
    playerResult = dbMan.cursor.fetchone()
    dbMan.cursor.execute(methodQuery, [opponentId])
    opponentResult = dbMan.cursor.fetchone()
    
    playerELO = playerResult["elo"]
    opponentELO = opponentResult["elo"]
    W = playerResult["wins"]
    D = playerResult["draws"]
    L = playerResult["losses"]
    
    prediction = 1 / (1 + 10**((opponentELO - playerELO) / 400))
    finalElo = ceil(playerELO + (40 * (realScore - prediction) * (1 + (0.5 * (0.5 - ((W + D) / (W + D + L)))))))

    dbMan.cursor.execute("UPDATE users SET elo = %s WHERE uuid LIKE %s", [finalElo, playerId])
    dbMan.conn.commit()
    dbMan.free()
