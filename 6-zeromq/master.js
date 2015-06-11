var express = require("express");
var zmq = require("zmq");


var backAddr = 'tcp://127.0.0.1:8001';
var frontAddr = 'tcp://127.0.0.1:8002';

function loadBalancer() {
  var workers = []

  var backSvr = zmq.socket('router')
  backSvr.identity = 'backSvr' + process.pid
  backSvr.bind(backAddr, function(err) {
    if (err) throw err;

    backSvr.on('message', function() {
      workers.push(arguments[0])
      console.log("WORKER CONNECTED")
      if (arguments[2] != 'READY') {
        frontSvr.send([arguments[2], arguments[3], arguments[4]])
      }
    })
  })

  var frontSvr = zmq.socket('router');
  frontSvr.identity = 'frontSvr' + process.pid;
  frontSvr.bind(frontAddr, function(err) {
    if (err) throw err;

    frontSvr.on('message', function() {
      var args = Array.apply(null, arguments);

      var interval = setInterval(function() {
        if (workers.length > 0) {
          backSvr.send([workers.shift(), '', args[0], '', args[2]])
          clearInterval(interval)
        }
      }, 10);
    });
  });
}


function httpServer() {
  var app = express();

  app.all("*", function(req, res) {
    var sock = zmq.socket('req');
    sock.connect(frontAddr);
    sock.send(req.originalUrl);

    sock.on('message', function(data) {
      res.format({
        html: function() {
          res.send(data);
        }
      })
      sock.close();
    });
  });

  app.listen(8000);
}


loadBalancer();
httpServer();