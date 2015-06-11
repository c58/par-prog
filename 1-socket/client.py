import socket

HOST = 'localhost'
PORT = 9876
ADDR = (HOST,PORT)
BUFSIZE = 4096

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

myfile = open('received_file.zip', 'w')
while True:
  data = client.recv(BUFSIZE)
  if not data: break
  myfile.write(data)
  print 'writing file ....'

myfile.close()
client.close()