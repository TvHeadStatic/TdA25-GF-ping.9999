from flask_socketio import SocketIO, send, emit, join_room, leave_room
from random import randrange

rooms = {
    "test0": {
        "started": False,
        "employees": {},
        "presented": [],
        "presenting": ""
    },
    "test1": {
        "started": False,
        "employees": {},
        "presented": [],
        "presenting": ""
    }
}

history = [
    {
        "name": "noway",
        "data": {
            "a": 1,
            "b": 10
        }
    }
]

socketio = SocketIO()

@socketio.on('create_room')
def create_me():
    room = str(randrange(100000,999999))
    rooms[room] = {
        "started": False,
        "employees": {},
        "presented": [],
        "presenting": ""
    }

@socketio.on('vote_on')
def votinginging(data):
    room = data['room']
    rooms[room]['employees'][rooms[room]['presenting']] += data["points"]
    print(rooms)

@socketio.on('suggestion_name')
def suggestion_name(data):
    username = data['username']
    room = data['room']
    join_room(room)
    emit("update_suggestion_name", { "suggestion": data["suggestion"] }, broadcast=True, include_self=True, to=room)

@socketio.on('do_next')
def next_in_line_pls(data):
    room = data['room']
    if room not in rooms: return
    if not rooms[room]['started']:
        rooms[room]['started'] = True
    if rooms[room]['presenting'] != "":
        rooms[room]['presented'].append(rooms[room]['presenting'])
    if len(rooms[room]['employees']) >= 1:
        for x in rooms[room]['employees']:
            if x in rooms[room]['presented']: continue
            rooms[room]['presenting'] = x
            break
    else:
        print("noone")
    join_room(room)
    still = False
    for x in rooms[room]['employees']:
        if x not in rooms[room]['presented']:
            still = True
    if not still:
        history.append({ "name": room, "data": {k: v for k, v in sorted(rooms[room]['employees'].items(), key=lambda item: item[1])}})
        emit("show_results", { "data": rooms[room] }, broadcast=True, include_self=True, to=room)
        print("history")
        del rooms[room]
        print(history)
        return
    emit("change_person", { "name": rooms[room]['presenting'] }, broadcast=True, include_self=True, to=room)

@socketio.on('join_room')
def join_me(data):
    username = data['username']
    room = data['room']
    if room not in rooms:
        emit("bring_back")
        return
    if rooms[room]['started']:
        emit("bring_back")
        return
    join_room(room)
    rooms[room]['employees'][username] = 0
    print(username + " joined room " + room)

@socketio.on('leave_room')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    print(username + " left room " + room)

@socketio.on('send_message')
def send_message(data):
    username = data['username']
    room = data['room']
    if room not in rooms: return
    join_room(room)
    emit("receive", data['username'] + "> " + data["text"], broadcast=True, include_self=True, to=room)