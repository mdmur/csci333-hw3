from socket import *
import Tkinter as tk

#window = tk.Tk()
#greeting = tk.Label(text="Hello, Tkinter")

host = 'localhost'
serverPort = 9999
bufSize = 1024

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((host, serverPort))

clientSocket.send("My list of files")

with open('new_file', 'wb') as f:
	print 'File opened'
	while True:
		data = clientSocket.recv(bufSize)
		print('data = %s', (data))
		if not data:
			f.close()
			print 'File closed'
			break
		f.write(data)

print('Successfully got the file')
clientSocket.close()
print('Connection closed')


