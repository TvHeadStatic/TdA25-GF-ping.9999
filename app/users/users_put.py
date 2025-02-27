from flask import Flask, jsonify, session
import uuid
import hashlib
import random
import datetime

from db.db_manager import db_manager

def users_put(id, req):
    dbMan = db_manager()

    if ("password" in req):
        if (req["password"] != "" and req["password"].isspace() and req["password"] != None):
            methodQuery = "UPDATE users SET password = %s, salt = %s WHERE uuid LIKE %s"
            salt = hex(random.randrange(0, 2**24))
            newPassword = hashlib.sha256(f"{req['password']}{salt}".encode()).hexdigest()
            dbMan.cursor.execute(methodQuery, [newPassword, salt, id])
    if ("username" in req):
        print("tvoje mama")
        if (req["username"] != "" and not req["username"].isspace() and req["username"] != None):
            if "user" in session:
                session["user"]["username"] = req["username"]
            methodQuery = "UPDATE users SET username = %s WHERE uuid LIKE %s"
            dbMan.cursor.execute(methodQuery, [req["username"], id])
            dbMan.conn.commit()
            dbMan.conn.commit()
    if ("elo" in req):
        if (req["elo"] != "" and req["elo"] != None):
            methodQuery = "UPDATE users SET elo = %s WHERE uuid LIKE %s"
            dbMan.cursor.execute(methodQuery, [req["elo"], id])
            dbMan.conn.commit()
    if ("wins" in req):
        if (req["wins"] != "" and not req["wins"].isspace() and req["wins"] != None):
            methodQuery = "UPDATE users SET wins = %s WHERE uuid LIKE %s"
            dbMan.cursor.execute(methodQuery, [req["wins"], id])
            dbMan.conn.commit()
    if ("draws" in req):
        if (req["draws"] != "" and not req["draws"].isspace() and req["draws"] != None):
            methodQuery = "UPDATE users SET draws = %s WHERE uuid LIKE %s"
            dbMan.cursor.execute(methodQuery, [req["draws"], id])
            dbMan.conn.commit()
    if ("losses" in req):
        if (req["losses"] != "" and not req["losses"].isspace() and req["losses"] != None):
            methodQuery = "UPDATE users SET losses = %s WHERE uuid LIKE %s"
            dbMan.cursor.execute(methodQuery, [req["losses"], id])
            dbMan.conn.commit()
    if ("email" in req):
        if (req["email"] != "" and not req["email"].isspace() and req["email"] != None):
            if "user" in session:
                session["user"]["email"] = req["email"]
            methodQuery = "UPDATE users SET email = %s WHERE uuid LIKE %s"
            dbMan.cursor.execute(methodQuery, [req["email"], id])
            dbMan.conn.commit()

    methodQuery = "SELECT users.uuid, users.createdAt, users.username, users.elo, users.wins, users.draws, users.losses FROM users WHERE uuid LIKE %s"
    dbMan.cursor.execute(methodQuery, [id])
    result = dbMan.cursor.fetchone()
    dbMan.free()

    return jsonify(result), 200