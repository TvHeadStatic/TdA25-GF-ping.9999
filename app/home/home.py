from flask import Flask, render_template, jsonify, Blueprint, request
from socks.socks import rooms, history

home_bp = Blueprint('home_bp', __name__, template_folder='templates')

@home_bp.route("/")
def home():
    finalPage = "home.html"
    if "darkmode" in request.args:
        finalPage = "darkmode/homedark.html"
    return render_template(finalPage) 

@home_bp.route("/login")
def aaaa():
    return render_template("login.html") 

@home_bp.route("/features")
def features():
    return render_template("features.html")

@home_bp.route("/manager")
def manager():
    finalPage = "managerstuff.html"
    if "darkmode" in request.args:
        finalPage = "darkmode/managerstuffdark.html"
    return render_template(finalPage, elementsuwu = rooms, chronicals=history)

