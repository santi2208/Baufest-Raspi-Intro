var express = require('express');
var app = express();
const bodyParser = require("body-parser");
var server = require('http').Server(app);
var io = require('socket.io')(server);

var team1 = {}
var team2 = {}
var team3 = {}
var team4 = {}
var team5 = {}
var team6 = {}
var team7 = {}
var team8 = {}
var team9 = {}
var team10 = {}

app.use(express.static(__dirname + "/../public"));
app.use(bodyParser.json());

app.post('/achievements', function(req, res) {
  console.log(req.body)
  switch(req.body[0][0]){
    case 1:
        team1 = req.body;
    break;
    case 2:
      team2 = req.body;
    break;
    case 3:
      team3 = req.body;
    break;
    case 4:
      team4 = req.body;
    break;
    case 5:
      team5 = req.body;
    break;
    case 6:
      team6 = req.body;
    break;
    case 7:
      team7 = req.body;
    break;
    case 9:
      team8 = req.body;
    break;
    case 9:
      team9 = req.body;
    break;
    case 10:
      team7 = req.body;
    break;
  }
  teams = [team1, team2, team3, team4, team5, team6, team7, team8, team9, team10];
  io.sockets.emit('teams', teams);
  res.status(200).jsonp('');
});

io.on('connection', function(socket) {
  console.log('Alguien se ha conectado con Sockets');
  teams = [team1,team2];
  socket.emit('teams', teams);
});

server.listen(8888, function() {
  console.log("Servidor corriendo en http://localhost:8888");
});