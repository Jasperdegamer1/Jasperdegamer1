// server.js
const express = require("express");
const http = require("http");
const { Server } = require("socket.io");
const path = require("path");

const app = express();
const server = http.createServer(app);
const io = new Server(server);

const PORT = 3000;
const HOST = '0.0.0.0';

// Statische bestanden bedienen vanuit de 'public' folder
app.use(express.static(path.join(__dirname, "public")));

io.on("connection", (socket) => {
    console.log("Een gebruiker is verbonden");

    // Luister naar inkomende berichten van een client
    socket.on("chatMessage", (data) => {
        // Stuur het bericht naar alle verbonden clients
        io.emit("chatMessage", data);
    });

    // Log ontkoppelingen
    socket.on("disconnect", () => {
        console.log("Een gebruiker is verbroken");
    });
});

// Start de server
server.listen(PORT, HOST, () => {
    console.log(`Server is actief op http://${HOST}:${PORT}`);
});
