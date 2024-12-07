from flask import Flask, render_template, Blueprint, request
import requests
from ast import literal_eval

game_bp = Blueprint('game_bp', __name__, template_folder = "./templates", static_folder="static", static_url_path="/")

apiURL = "https://50336bc6.app.deploy.tourde.app/api/v1/games"

@game_bp.route("/")
def main():
    return render_template("index.html", title = "TdA | Home"), 200

@game_bp.route("/game")
def game():
    apiRez = requests.get(apiURL)
    return render_template("game.html", title = "TdA | Game", gamez = apiRez.json()), 200

@game_bp.route("/game/<id>")
def gaming(id):
    # "http://" + request.url_root + "api/v1/games/"
    apiRes = requests.get(apiURL + "/" + id)
    return render_template("board.html", title = "TdA | " + apiRes.json()["name"], gameData = apiRes.json()), 200