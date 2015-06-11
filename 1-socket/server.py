import socket

HOST = ''
PORT = 9876
ADDR = (HOST,PORT)
BUFSIZE = 4096

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(ADDR)
serv.listen(5)

binary_file_path = "file.zip"
bytes = open(binary_file_path).read()

print 'listening ...'

while True:
  conn, addr = serv.accept()
  print 'client connected ... ', addr
  conn.send(bytes)
  conn.close()
  print 'client disconnected'