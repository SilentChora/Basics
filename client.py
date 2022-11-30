from socket import *
server_name = 'localhost'
server_port = 5003
c = socket(AF_INET, SOCK_STREAM)
c.connect((server_name,server_port))

while True:
  s = input(">> ")
  c.send(s.encode())
  message = c.recv(2048)
  print (">> ", message.decode())
  if(s.lower() == 'bye'):
    print("Adios..closing connection")
    c.close()
