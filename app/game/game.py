from flask import Flask, render_template, Blueprint, request, session, url_for, redirect
import requests
from ast import literal_eval
from db.db_manager import db_manager
from api.api_post import api_post

game_bp = Blueprint('game_bp', __name__, template_folder = "./templates", static_folder="static", static_url_path="/")

@game_bp.errorhandler(404) 
def not_found(e): 
    return render_template("404.html") 

@game_bp.route("/")
def main():
    return render_template("index.html", title = "TdA | Home"), 200

@game_bp.route("/game")
def game():
    if "user" in session:
        apiRez = requests.get(url_for("api_bp.api_getall", _external=True))
        return render_template("game.html", title = "TdA | Game", gamez = apiRez.json(), userData = session["user"]), 200
    return redirect(url_for("game_bp.main"))

@game_bp.route("/game/canvas")
def gamemaking():
    if "user" in session:
        gameDat = {
        "board": [
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ],
                "gameMode": "public",
                "gameState": "opening",
                "name": "",
        }
        return render_template("board_canvas.html", title = "TdA | New Project", gameData = gameDat, userData = session["user"]), 200
    return redirect(url_for("game_bp.main"))

@game_bp.route("/game/<id>")
def gaming(id):
    if "user" in session:
        apiRes = requests.get(url_for("api_bp.api", id=id, _external=True))
        if apiRes.status_code != 200:
            return redirect("/404")
        return render_template("board.html", title = "TdA | " + apiRes.json()["name"], gameData = apiRes.json(), userData = session["user"]), 200
    return redirect(url_for("game_bp.main"))

@game_bp.route("/game/user/<id>")
def profiling(id):
    if "user" in session:
        dbMan = db_manager()
        methodQuery = "SELECT username, losses, wins, draws, uuid, elo, createdat FROM users WHERE uuid LIKE %s"
        dbMan.cursor.execute(methodQuery, [id])
        result = dbMan.cursor.fetchone()
        dbMan.free()
        if result == None:
            return redirect("/404")
    print(result)
    return render_template("user_profile.html", title = "TdA | " + result["username"], userData = result), 200

@game_bp.route("/game/leaderboard/<id>")
def jacking(id):
    dbMan = db_manager()
    match(id):
        case "losses":
            methodQuery = "SELECT username, losses, wins, draws, uuid, elo FROM users ORDER BY losses DESC LIMIT 20"
        case "wins":
            methodQuery = "SELECT username, losses, wins, draws, uuid, elo FROM users ORDER BY wins DESC LIMIT 20"
        case _:
            methodQuery = "SELECT username, losses, wins, draws, uuid, elo FROM users ORDER BY elo DESC LIMIT 20"
    dbMan.cursor.execute(methodQuery)
    result = dbMan.cursor.fetchall()
    dbMan.free()
    return render_template("leaderboard.html", title = "TdA | Leaderboard " + id, boardData = result, orderedby = id), 200

@game_bp.route("/game/matchmaking")
def matchumakingu():
    dbMan = db_manager()
    methodQuery = "SELECT elo FROM users WHERE uuid LIKE %s"
    dbMan.cursor.execute(methodQuery, [session["user"]["uuid"]])
    myElo = dbMan.cursor.fetchone()
    methodQuery = '''
    SELECT piskvorky.uuid, piskvorky.x, users.elo, piskvorky.gamemode FROM piskvorky
    JOIN users ON piskvorky.x = users.uuid
    WHERE piskvorky.o like '' AND elo <= %s + 100 AND gamemode not like 'private' ORDER BY elo DESC;
    '''
    dbMan.cursor.execute(methodQuery, [int(myElo["elo"])])
    result = dbMan.cursor.fetchall()
    dbMan.free()

    gameDat = {
        "board": [
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ],
                "gameMode": "public",
                "gameState": "opening",
                "name": "WIP",
    }

    if len(result) == 0:
        r = requests.post(url_for("api_bp.api_getall", _external=True), json = gameDat)
        return redirect(url_for("game_bp.gaming", id=r.json()["uuid"]))
    else:
        return redirect(url_for("game_bp.gaming", id=result[0]["uuid"]))
    