from flask_socketio import SocketIO, send, emit, join_room, leave_room

messages = []

socketio = SocketIO()

@socketio.on('join_room')
def join_room(data):
    print('received message: ' + data["data"])

@socketio.on('send_message')
def send_message(data):
    messages.append(data["text"])
    print(data["text"])
    emit("receive", data["text"], broadcast=True, include_self=True)