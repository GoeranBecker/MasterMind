from flask import Flask, render_template, request
from flask_socketio import SocketIO


app = Flask(__name__, template_folder="../../templates", static_folder="../../static")
socketio = SocketIO(app)


@app.route("/")
def home():
    return render_template("base.html")


@socketio.on("message")
def handleWSMessage(msg):
    socketio.emit("message", {"msg": msg}, to=request.sid)
    print(msg)


@socketio.on("connect")
def handleWSConnect():
    socketio.emit("message", {"msg": "Hello from server!"}, to=request.sid)


if __name__ == "__main__":
    socketio.run(app, debug = True)