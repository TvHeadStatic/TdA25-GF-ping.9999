from flask import Flask, render_template, jsonify
import os

from api.api import api_bp
from game.game import game_bp

app = Flask(__name__)

app.register_blueprint(api_bp)
app.register_blueprint(game_bp)

if __name__ == '__main__':
    print("m: " + str(os.getenv("FOO")))
    app.run(debug=True)
