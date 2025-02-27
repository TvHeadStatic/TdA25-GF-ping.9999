from flask import Flask, jsonify, session
import uuid
import hashlib
import random
import datetime

from db.db_manager import db_manager

def users_put(id, req):
    dbMan = db_manager()

    if (req["password"] != "" or req["password"] != None):
        methodQuery = "UPDATE users SET password = %s, salt = %s WHERE uuid LIKE %s"
        salt = hex(random.randrange(0, 2**24))
        newPassword = hashlib.sha256(f"{req['password']}{salt}".encode()).hexdigest()
        dbMan.cursor.execute(methodQuery, [newPassword, salt])
    if (req["username"] != "" or req["username"] != None):
        methodQuery = "UPDATE users SET username = %s WHERE uuid LIKE %s"
        dbMan.cursor.execute(methodQuery, [req["username"]])
    if (req["elo"] != "" or req["elo"] != None):
        methodQuery = "UPDATE users SET elo = %s WHERE uuid LIKE %s"
        dbMan.cursor.execute(methodQuery, [req["elo"]])
    if (req["wins"] != "" or req["wins"] != None):
        methodQuery = "UPDATE users SET wins = %s WHERE uuid LIKE %s"
        dbMan.cursor.execute(methodQuery, [req["wins"]])
    if (req["draws"] != "" or req["draws"] != None):
        methodQuery = "UPDATE users SET draws = %s WHERE uuid LIKE %s"
        dbMan.cursor.execute(methodQuery, [req["draws"]])
    if (req["losses"] != "" or req["losses"] != None):
        methodQuery = "UPDATE users SET losses = %s WHERE uuid LIKE %s"
        dbMan.cursor.execute(methodQuery, [req["losses"]])
    if (req["email"] != "" or req["email"] != None):
        methodQuery = "UPDATE users SET email = %s WHERE uuid LIKE %s"
        dbMan.cursor.execute(methodQuery, [req["email"]])

    methodQuery = "SELECT users.uuid, users.createdAt, users.username, users.elo, users.wins, users.draws, users.losses FROM users WHERE uuid LIKE %s"
    dbMan.cursor.execute(methodQuery, [id])
    result = dbMan.cursor.fetchone()
    dbMan.free()

    if "user" in session:
        if req["email"] != None: session["user"]["email"] = req["email"]
        if req["username"] != None: session["user"]["username"] = req["username"]

    return jsonify(result), 200