from flask import Flask, render_template, request
from flask_socketio import SocketIO


app = Flask(__name__, template_folder="../../templates", static_folder="../../static")
app.config["SECRET_KEY"] = "ThisIsAGoodSecretIndeed"
socketio = SocketIO(app)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("user_name")
        
        if not name:
            pass
        return render_template("index.html", user_name = name)
    return render_template("index.html")
    

@app.route("/create_room")
def create_room():
    return render_template("create_room.html")


@socketio.on("message")
def handleWSMessage(msg):
    socketio.emit("message", {"msg": msg}, to=request.sid)
    print(msg)


@socketio.on("connect")
def handleWSConnect():
    socketio.emit("message", {"msg": "Hello from server!"}, to=request.sid)


if __name__ == "__main__":
    socketio.run(app, debug = True)