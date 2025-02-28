from flask import Flask, render_template, Blueprint, request, session, url_for, redirect
import requests
from ast import literal_eval
from db.db_manager import db_manager
from api.api_post import api_post
import random

game_bp = Blueprint('game_bp', __name__, template_folder = "./templates", static_folder="static", static_url_path="/")

@game_bp.errorhandler(404) 
def not_found(e): 
    finalPage = "404.html"
    if "darkmode" in request.args:
        finalPage = "dark_mode/404.html"
    return render_template(finalPage) 

@game_bp.route("/")
def main():
    finalPage = "index.html"
    if "darkmode" in request.args:
        finalPage = "dark_mode/index.html"
    return render_template(finalPage, title = "TdA | Home"), 200

@game_bp.route("/game")
def game():
    finalPage = "game.html"
    if "darkmode" in request.args:
        finalPage = "dark_mode/game.html"
    heks = [
        'Did you know, "Tick Tack Toe" has nothing to do with putting tic-tacs between your toes?',
        'Did you know, that if you took out your organs and put them in a line over the equator, you\'d be dead?',
        'Did you know, that if we\'d spinned the "X" in our game a little, we\'d be breaking the Geneva convention?',
        'Did you know, Tick Tack Toe can be dated to 1st century BC?',
        'Did you know, Tick Tack Toe\'s less popular name is noughts and crosses?',
        'Did you know, that probably everyone, who\'s ever going to live, will play Tick Tack Toe at some point?',
        'Did you know, that Tic Tac Toe has a very indepth lore?',
        'Did you know, a game of Tic Tac Toe will always end in a tie if both players are plain at their best?',
        'Did you know, that unlike in chess, you cannot move your pieces in Tic Tac Toe?',
        '🤫🧏🤫🧏, 🤫🧏🤫🧏🤫🧏,🤫🧏🤫🧏?'
    ]
    if "user" in session:
        if "isguest" in session["user"]:
            session.pop("user", None)
            return redirect(url_for("game_bp.main"))
        return render_template(finalPage, title = "TdA | Game", userData = session["user"], hek = random.choice(heks)), 200
    return redirect(url_for("game_bp.main"))

@game_bp.route("/game/canvas")
def gamemaking():
    finalPage = "board_canvas.html"
    if "darkmode" in request.args:
        finalPage = "dark_mode/board_canvas.html"
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
        return render_template(finalPage, title = "TdA | New Project", gameData = gameDat, userData = session["user"]), 200
    return redirect(url_for("game_bp.main"))

@game_bp.route("/game/<id>")
def gaming(id):
    finalPage = "board.html"
    if "darkmode" in request.args:
        finalPage = "dark_mode/board.html"
    if "user" in session:
        apiRes = requests.get(url_for("api_bp.api", id=id, _external=True))
        if apiRes.status_code != 200:
            return redirect("/404")
        return render_template(finalPage, title = "TdA | " + apiRes.json()["name"], gameData = apiRes.json(), userData = session["user"]), 200
    return redirect(url_for("game_bp.main"))

@game_bp.route("/freeplay")
def free_of_charge():
    finalPage = "board.html"
    if "darkmode" in request.args:
        finalPage = "dark_mode/board.html"
    if "code" not in request.args:
        return redirect("/404")
    apiRes = requests.get(url_for("api_bp.api", id=request.args.get("code"), _external=True))
    if apiRes.status_code != 200:
        return redirect("/404")
    if "gamemode" in apiRes.json():
        if apiRes.json()["gamemode"] != "private":
            return redirect("/404")
    if "user" not in session:
        session.permanent = False
        session["user"] = {
                "uuid": str(random.randrange(0, 2**24)),
                "email": "guester",
                "username": "guest" + str(random.randrange(0, 2**24)),
                "token": str(random.randrange(0, 2**24)),
                "isguest": True
        }
    return render_template(finalPage, title = "TdA | " + apiRes.json()["name"], gameData = apiRes.json(), userData = session["user"]), 200

@game_bp.route("/game/user/<id>")
def profiling(id):
    finalPage = "user_profile.html"
    finalAPage = "admin_profile.html"
    finalMPage = "mein_user_profile.html"
    if "darkmode" in request.args:
        finalPage = "dark_mode/user_profile.html"
        finalAPage = "dark_mode/admin_profile.html"
        finalMPage = "dark_mode/mein_user_profile.html"


    if "user" in session:
        dbMan = db_manager()
        methodQuery = "SELECT username, losses, wins, draws, uuid, elo, createdat, email, \"gameHistory\" FROM users WHERE uuid LIKE %s"
        dbMan.cursor.execute(methodQuery, [id])
        result = dbMan.cursor.fetchone()
        methodQuery = "SELECT username, losses, wins, draws, uuid, elo, createdat, email FROM users"
        dbMan.cursor.execute(methodQuery)
        result2 = dbMan.cursor.fetchall()
        dbMan.free()
        if result == None:
            return redirect("/404")
        print(result)
    else:
        return redirect(url_for("game_bp.main"))
    if session["user"]["uuid"] == result['uuid']:
        if result['email'] == "tda@scg.cz":
            return render_template(finalAPage, title = "TdA | " + result["username"], userData = result, allUserData = result2), 200
        return render_template(finalMPage, title = "TdA | " + result["username"], userData = result), 200
    return render_template(finalPage, title = "TdA | " + result["username"], userData = result), 200

@game_bp.route("/game/leaderboard/<id>")
def jacking(id):
    finalPage = "leaderboard.html"
    if "darkmode" in request.args:
        finalPage = "dark_mode/leaderboard.html"
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
    return render_template(finalPage, title = "TdA | Leaderboard " + id, boardData = result, orderedby = id), 200

@game_bp.route("/game/matchmaking")
def matchumakingu():
    yoMom = ""
    if "darkmode" in request.args:
        yoMom = "?darkmode=true"
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
                "name": "Match",
    }

    if len(result) == 0:
        r = requests.post(url_for("api_bp.api_getall", _external=True), json = gameDat)
        return redirect(str(url_for("game_bp.gaming", id=r.json()["uuid"])+yoMom))
    else:
        return redirect(str(url_for("game_bp.gaming", id=result[0]["uuid"])+yoMom))