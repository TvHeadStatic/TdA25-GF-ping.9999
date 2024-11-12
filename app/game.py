from flask import Flask, render_template, Blueprint

game_bp = Blueprint('game_bp', __name__, template_folder = "../HTML/templates")

@game_bp.route("/game")
def game():
    return render_template("game.html", title = "TdA"), 200