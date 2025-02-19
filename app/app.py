from flask import Flask, render_template, jsonify
from sockets.sockets import socketio
from werkzeug.middleware.proxy_fix import ProxyFix
from datetime import timedelta
from dotenv import load_dotenv
import os

from gateway.gateway import gateway_bp
from api.api import api_bp
from game.game import game_bp
from users.users import users_bp


if os.path.isfile(".env"): load_dotenv()

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1, x_proto=1, x_prefix=1)
app.url_map.strict_slashes = False
app.secret_key = "test"
app.config['SECRET_KEY'] = "test"
app.permanent_session_lifetime = timedelta(days = 1)
app.register_blueprint(gateway_bp)
app.register_blueprint(api_bp)
app.register_blueprint(game_bp)
app.register_blueprint(users_bp)
socketio.init_app(app, cors_allowed_origins="*")

print("API_SECRET env test (not actual key don' worry): " + str(os.getenv("API_SECRET")))
if __name__ == '__main__':
    socketio.run(app)
