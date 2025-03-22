from flask_socketio import SocketIO, send, emit, join_room, leave_room

messages = []

socketio = SocketIO()

@socketio.on('join_room')
def join_me(data):
    username = data['username']
    room = data['room']
    join_room(room)
    print(username + "joined room " + room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    print(username + "joined room " + room)

@socketio.on('send_message')
def send_message(data):
    messages.append(data["text"])
    print(data["text"])
    emit("receive", data["text"], broadcast=True, include_self=True)