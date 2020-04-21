from socket import *
from threading import Thread
from SocketServer import ThreadingMixIn

serverName = 'localhost'
serverPort = 9999
bufSize = 1024

class SingleThread(Thread):

	def __init__(self, ip, port, sock):
		Thread.__init__(self)
		self.ip = ip
		self.port = port
		self.sock = sock
		print "New thread started for "+ip+":"+str(port)

	def run(self):
		mess = conn.recv(bufSize).decode()
		#print(mess)

		filename = 'file.txt'
		f = open(filename, 'rb')
		while True:
			data = f.read(bufSize)
			while (data):
				self.sock.send(data)
				data = f.read(bufSize)
			if not data:
				f.close()
				self.sock.close()
				break
		print("File sent")

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind((serverName, serverPort))
threads = []

while True:
	serverSocket.listen(1)
	print("The server is ready to receive")
	(conn, (ip, port)) = serverSocket.accept()
	print "Got a connection from ", (ip, port)

	newThr = SingleThread(ip, port, conn)
	newThr.start()
	threads.append(newThr)

for t in threads:
	t.join()
#serverSocket.close()
