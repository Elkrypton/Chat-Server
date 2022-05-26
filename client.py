

from socket import *
from codecs import decode 



HOST = input(">> Host/IP:")
PORT = int(input(">> Port:"))
BUFSIZE = 2045
ADDRESS = (HOST,PORT)
CODE ='ascii'
server = socket(AF_INET,SOCK_STREAM)
server.connect((ADDRESS))
print(decode(server.recv(BUFSIZE),CODE))
name = raw_input("Enter your name :")
server.send(name) 

while True:
	record = decode(server.recv(BUFSIZE),CODE)
	if not record:
		continue
		print(record)
		message = raw_input('> ')

	if not message or message == "":
		print(record)
		message = raw_input("> ")


	server.send(message + '\n')
server.close()
