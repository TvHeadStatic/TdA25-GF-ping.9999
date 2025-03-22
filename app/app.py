from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
from werkzeug.middleware.proxy_fix import ProxyFix
from datetime import timedelta
from dotenv import load_dotenv
import os

from home.home import home_bp

if os.path.isfile(".env"): load_dotenv()

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1, x_proto=1, x_prefix=1)
app.url_map.strict_slashes = False
app.secret_key = "test"
app.config['SECRET_KEY'] = "test"
app.permanent_session_lifetime = timedelta(days = 1)
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

app.register_blueprint(home_bp)

@socketio.on('message')
def handle_message(data):
    print('received message: ' + data["data"])

@socketio.on('send_message')
def send_message(data):
    messages.append(data["text"])
    print(data["text"])
    emit("receive", data["text"], broadcast=True, include_self=True)

print("API_SECRET env test (not actual key don' worry): " + str(os.getenv("API_SECRET")))
if __name__ == '__main__':
    socketio.run(app, debug=True)
