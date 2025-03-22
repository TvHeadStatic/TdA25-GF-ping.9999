from flask import Flask, render_template, jsonify, Blueprint
from socks.socks import rooms

home_bp = Blueprint('home_bp', __name__, template_folder='templates')

@home_bp.route("/")
def home():
    return render_template("home.html")

@home_bp.route("/features")
def features():
    return render_template("features.html")

@home_bp.route("/manager")
def manager():
    return render_template("managerstuff.html",  elementsuwu=rooms)

@home_bp.route("/testing")
def testing():
    return render_template("placeholder.html")
