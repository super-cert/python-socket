import socket

#SOCK_STREAM is used for TCP

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverPort = 6789

serverSocket.bind(("", serverPort))

serverSocket.listen(1)


while 1:
		
	print ("Ready to next Battle")

	# Set up a new connection from the client

	connectionSocket, addr= serverSocket.accept() #스리핸드새이킹 ack
	#connection으로 맺어짐 
	try :

		message = connectionSocket.recv(1024)

		filename = message.split()[1]
		
		f = open(filename[1:])
		outputdata = f.read()
		print(outputdata)
		connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

		connectionSocket.send(outputdata.encode())
		#for i in range(0, len(outputdata)):
		#	connectionSocket.send(outputdata[i].encode())
		connectionSocket.send("\r\n".encode())
		print("hi")
		connectionSocket.close()

	#except IOError:
	except de:
		connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
		connectionSocket.close()

serverSocket.close()