import socket

tcpClientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

tcpClientSocket.connect(('127.0.0.1',8888))

test = """
POST /test.txt HTTP/1.1
Host: w3schools.com
name1=value1&name2=value2
"""

tcpClientSocket.sendall(test.encode())
tcpClientSocket.settimeout(10)

while 1:				

	message, address = tcpClientSocket.recvfrom(1024)
	print(message.decode(),end='')
	if not message:
		break
	

tcpClientSocket.close()