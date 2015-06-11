import socket
import sys, time
sys.path.append("movie")
from protobuf_pb2 import Movie

HOST = 'localhost'
PORT = 9876
ADDR = (HOST,PORT)
BUFSIZE = 4096

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

mov = Movie()
mov.ParseFromString(client.recv(BUFSIZE))
print mov

client.close()