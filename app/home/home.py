from flask import Flask, render_template, jsonify, Blueprint
from socks.socks import messages

home_bp = Blueprint('home_bp', __name__, template_folder='templates')

@home_bp.route("/")
def home():
    return render_template("home.html", heynow=messages)

@home_bp.route("/features")
def features():
    return render_template("features.html")