

from socket import * 
from codecs import decode 
from chatrecords import ChatRecord
from time import ctime
from threading import Thread



class ClientHandler(Thread):

	def __init__(self,client,record):
		Thread.__init__(self)
		self._client = client 
		self._record = record

	def run(self):
		self._client.send('Behave your ass well ') 
		self._name = self._client.recv(BUFSIZE)
		self._client.send(str(self._record))
		while True:
			message = self._client.recv(BUFSIZE)
			if not message:
				print("Client Disconnected !")
				self._client.close()
				break 
			else:
				message = self._name + ' ' + ctime() + '\n\n' + '<<'+self._name +'>>' ':' + message 
				self._record.add(message)
				self._client.send(str(self._record))



HOST = input(">> Host to use:")
PORT = int(input(">> Port:"))
ADDRESS = (HOST,PORT)
BUFSIZE = 2024
record = ChatRecord()
server = socket(AF_INET,SOCK_STREAM)
server.bind((ADDRESS))
server.listen(5)
print("[STARTING] Served Started at {}:{}".format(HOST,PORT))

while True:
	print("Waiting for connections ...")

	client,address = server.accept()
	print(">> Connected from : {}".format(address))
	handler = ClientHandler(client,record)
	handler.start()
