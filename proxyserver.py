import socket
import sys
'''
if len(sys.argv) <= 1:
	print (' 하나더 입력하시게 ')
	sys.exit(2)
'''
tcpServerSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#tcpServerSocket.bind((sys.argv[1],8888))
tcpServerSocket.bind(('',8888))
tcpServerSocket.listen(10)



#Strat receiving data from the client
print ("Ready to server..")

tcpClientSocket, addr = tcpServerSocket.accept()
print("Receiving success" , " : " , addr)

message = tcpClientSocket.recv(1024) ## 사실상 connection
print(message)

# Extract the filename from the given message

print(message.split()[1])

filename = message.split()[1].decode().partition("/")[2]
print(filename)
fileExist = "false"
filetouse = "/" + filename
print(filetouse)

try:
	#Check if the file exist in the cache
	f = open(filetouse[1:],"r")
	outputdata = f.readlines()
	fileExist = "true"
	# ProxyServer finds a cache hit and generates a response message
	tcpClientSocket.send("HTTP/1.0 200 OK\r\n".encode())
	tcpClientSocket.send("Content-Type:text/html\r\n".encode())
	for i in range(0, len(outputdata)):
		tcpClientSocket.send(outputdata[i].encode())
	print("Read frmo Cache")

	# Error handling for file not found in cache
except IOError:

	if fileExist == "false":
		# Create a socket on the proxyserver
		c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		hostn = filename.replace("www.","",1)
		try:
			# Connect to the socket to port 80
			c.connect((hostn,3333))
			# Create a temporary file on this socket and ask port 80 for the file requested by the cient
			fileobj = c.makefile('r',0)
			fileobj.write("GET " + "http://" + filename + " HTTP/1.0\r\n")

			print("fileobj is : " + fileobj)
			buff = fileobj.readlines()
			tmpFile = open("./ " + filename, "wb")
			for line in buff:
				tmpFile.write(line)
				tcpClientSocket.send(line)
		except e:
			print("illegal request")
	else:

		#HTTP response message for file not found
		tcpClientSocket.send("HTTP/1.0 404 sendError\r\n".encode())
		tcpClientSocket.send("Content-Type:text/html\r\n".encode())
	tcpClientSocket.close()
tcpServerSocket.close()





