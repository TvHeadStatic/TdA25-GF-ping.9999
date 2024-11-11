from flask import Flask, render_template, jsonify

from api import api_bp
from game import game_bp

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello TdA", 200

app.register_blueprint(api_bp)
app.register_blueprint(game_bp)

if __name__ == '__main__':
    app.run(debug=True)
