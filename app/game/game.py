from flask import Flask, render_template, Blueprint, request
import requests
from ast import literal_eval

game_bp = Blueprint('game_bp', __name__, template_folder = "./templates", static_folder="static", static_url_path="/")

@game_bp.route("/")
def main():
    return render_template("index.html", title = "TdA"), 200

@game_bp.route("/game")
def game():
    return render_template("game.html", title = "TdA"), 200

@game_bp.route("/game/<id>")
def gaming(id):
    # "http://" + request.url_root + "api/v1/games/"
    apiRes = requests.get("https://50336bc6.app.deploy.tourde.app/api/v1/games/" + id)
    return render_template("board.html", title = "TdA", gameData = apiRes.json()), 200