from flask import Flask, render_template, Blueprint, request, session, url_for, redirect
import requests
from ast import literal_eval

game_bp = Blueprint('game_bp', __name__, template_folder = "./templates", static_folder="static", static_url_path="/")

apiURL = "https://50336bc6.app.deploy.tourde.app/api/v1/games"

@game_bp.route("/")
def main():
    return render_template("index.html", title = "TdA | Home"), 200

@game_bp.route("/game")
def game():
    if "user" in session:
        apiRez = requests.get(apiURL)
        return render_template("game.html", title = "TdA | Game", gamez = apiRez.json(), userData = session["user"]), 200
    return redirect(url_for("game_bp.main"))

@game_bp.route("/game/<id>")
def gaming(id):
    if "user" in session:
        apiRes = requests.get(apiURL + "/" + id)
        return render_template("board.html", title = "TdA | " + apiRes.json()["name"], gameData = apiRes.json(), userData = session["user"]), 200
    return redirect(url_for("game_bp.main"))