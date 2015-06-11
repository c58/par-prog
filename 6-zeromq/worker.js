var express = require("express");
var zmq = require("zmq");


var backAddr = 'tcp://127.0.0.1:8001';
var frontAddr = 'tcp://127.0.0.1:8002';

var sock = zmq.socket('req');
sock.identity = "worker" + process.pid
sock.connect(backAddr)
sock.send('READY')

sock.on('message', function() {
  console.log("client -> " + sock.identity);
  var args = Array.apply(null, arguments)
  var html = "<h3>Welcome to '"+args[2]+"' page</h3>";
  sock.send([arguments[0], '', html])
})