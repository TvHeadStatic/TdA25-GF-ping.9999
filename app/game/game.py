from flask import Flask, render_template, Blueprint, request, session, url_for, redirect
import requests
from ast import literal_eval
from db.db_manager import db_manager

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
                "difficulty": "medium",
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

@game_bp.route("/game/matchmaking")
def matchumakingu():
    dbMan = db_manager()
    methodQuery = '''
    select piskvorky.uuid, piskvorky.x, users.elo from piskvorky
    join users on piskvorky.x = users.uuid
    where piskvorky.o is null and elo <= %s order by elo desc limit 1;
    '''
    dbMan.cursor.execute(methodQuery)
    result = dbMan.cursor.fetchall()
    dbMan.free()
    return result