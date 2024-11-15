from flask import Flask, render_template, Blueprint, request
import requests
from ast import literal_eval

game_bp = Blueprint('game_bp', __name__, template_folder = "./templates")

@game_bp.route("/")
def main():
    return "Hello TdA", 200

@game_bp.route("/game")
def game():
    return render_template("game.html", title = "TdA"), 200

@game_bp.route("/game/<id>")
def gaming(id):
    # request.url_root + 
    apiRes = requests.get("https://50336bc6.app.deploy.tourde.app/api/v1/games/" + id)
    apiResponse = literal_eval(apiRes.text)
    return render_template("game.html", title = "TdA", gameData = apiResponse), 200