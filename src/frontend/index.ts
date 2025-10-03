import type { Socket } from "socket.io-client";

declare const io: {
  (url?: string, opts?: any): Socket;
};

const socket = io();

socket.on("connect", () => {
    console.log("Connected:", socket.id);
    socket.send("Hello from browser!");
});

socket.on("message", (msg) => {
    console.log(msg.msg)
})

const button = document.getElementById("buttonSend");
let counter = 1;

button.addEventListener("click", () => {
    socket.send(`Message ${counter}`);
    counter ++;
});