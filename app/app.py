from flask import Flask, render_template, jsonify
import os

from gateway.gateway import gateway_bp
from api.api import api_bp
from game.game import game_bp
from users.users import users_bp

app = Flask(__name__)
app.url_map.strict_slashes = False

app.register_blueprint(gateway_bp)
app.register_blueprint(api_bp)
app.register_blueprint(game_bp)
app.register_blueprint(users_bp)

print("API_SECRET env test (not actual key don' worry): " + str(os.getenv("API_SECRET")))
if __name__ == '__main__':
    app.run(debug=True)
