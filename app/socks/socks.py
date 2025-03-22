from flask_socketio import SocketIO, send, emit, join_room, leave_room

rooms = {
    "test0": False,
    "test1": False
}

socketio = SocketIO()

@socketio.on('create_room')
def create_me(data):
    username = data['username']
    room = data['room']
    rooms.append(room)
    join_room(room)
    print(username + " joined room " + room)

@socketio.on('join_room')
def join_me(data):
    username = data['username']
    room = data['room']
    if room not in rooms:
        emit("bring_back")
        return
    if rooms[room]:
        emit("bring_back")
        return
    join_room(room)
    print(username + " joined room " + room)

@socketio.on('leave_room')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    print(username + " leaved room " + room)

@socketio.on('send_message')
def send_message(data):
    username = data['username']
    room = data['room']
    if room not in rooms: return
    join_room(room)
    print(data["text"])
    emit("receive", data['username'] + "> " + data["text"], broadcast=True, include_self=True, to=room)