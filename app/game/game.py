from flask import Flask, render_template, Blueprint, request
import requests
import json

game_bp = Blueprint('game_bp', __name__, template_folder = "./templates")

@game_bp.route("/")
def main():
    return "Hello TdA", 200

@game_bp.route("/game")
def game():
    return render_template("game.html", title = "TdA"), 200

@game_bp.route("/game/<id>")
def gaming(id):
    apiRes = requests.get(request.url_root + "api/v1/games/" + id)
    apiResponse = json.loads(apiRes.text)
    return render_template("game.html", title = "TdA", gameData = apiResponse), 200