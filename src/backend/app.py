from flask import Flask, render_template, redirect, url_for
import websockets as ws
import asyncio
from threading import Thread


app = Flask(__name__, template_folder="../../templates", static_folder="../../static")


@app.route("/")
def home():
    return render_template("base.html")



async def handler(websocket):
    await websocket.send("Hello from asyncio server!")

    async for message in websocket:
        print(f"Received: {message}")
        await websocket.send(f"Echo: {message}")


async def main():
    async with ws.serve(handler, "localhost", 8765):
            print("Asyncio WebSocket server running on ws://localhost:8765")
            await asyncio.Future()

def startWs():
    asyncio.run(main())

def startFlask():
    app.run(debug = True, use_reloader=False)


if __name__ == "__main__":
    ws_thread = Thread(target=startWs, daemon=True)
    ws_thread.start()
    app.run(debug = True)