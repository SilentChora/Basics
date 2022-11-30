from socket import *
server_port = 5003
s = socket(AF_INET,SOCK_STREAM)
s.bind(('localhost',server_port))
s.listen(1)
print ("Welcome: The server is now ready to receive")
while True:
  c, addr = s.accept()
  print("Connected to ",addr)
  sentence = c.recv(2048).decode()
  print('>> ',sentence)
  m = input(">> ")
  c.send(m.encode())
  if(m.upper() == 'BYE'):
    print("Adios....closing connection")
    c.close()
