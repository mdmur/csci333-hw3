from socket import *
import os
import Tkinter as tk

#window = tk.Tk()
#greeting = tk.Label(text="Hello, Tkinter")

host = 'localhost'
serverPort = 9999
bufSize = 1024

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((host, serverPort))

myIP = gethostbyname(host)
myPort = clientSocket.getsockname()[1]

clientSocket.send("HELLO")
mess = clientSocket.recv(bufSize).decode()
print(mess)

i = 0
entries = os.listdir('cl1/')
for entry in entries:
	name, ext = os.path.splitext(entry)
	size = os.path.getsize('cl1/'+entry)
	time = os.path.getmtime('cl1/'+entry)
	clientSocket.send("<"+name+", "+ext+", "+str(size)+", "+str(time)+", "+str(myIP)+", "+str(myPort)+">\n")

"""with open('new_file', 'wb') as f:
	print 'File opened'
	while True:
		data = clientSocket.recv(bufSize)
		print('data = %s', (data))
		if not data:
			f.close()
			print 'File closed'
			break
		f.write(data)

print('Successfully got the file')"""
clientSocket.close()
print('Connection closed')


