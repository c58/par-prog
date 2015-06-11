import socket
import sys, time
sys.path.append("movie")
from protobuf_pb2 import Movie

HOST = ''
PORT = 9876
ADDR = (HOST,PORT)

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(ADDR)
serv.listen(5)
print 'listening ...'

while True:
  conn, addr = serv.accept()
  print 'client connected ... ', addr

  mov = Movie()
  mov.name = "Martian"
  mov.year = 2015
  mov.actors.append("Matt Damon")
  mov.actors.append("Jessica Chastain")
  mov.genre = Movie.FANTASY

  conn.send(mov.SerializeToString())
  conn.close()
  print 'client disconnected'