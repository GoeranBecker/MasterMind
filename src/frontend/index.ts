const socket = new WebSocket("ws://localhost:8765");

socket.onopen = () => {
    console.log("Connected to server");
    socket.send("Hello from the browser!");
};

socket.onmessage = (event) => {
    console.log("Message from server:", event.data);
};

socket.onclose = () => {
    console.log("Disconnected from server");
};

socket.onerror = (err) => {
    console.error("Socket error:", err);
};

const button = document.getElementById("sendButton");
let counter = 1;

button.addEventListener("click", () => {
    socket.send(`Message ${counter}`);
    counter++;
})