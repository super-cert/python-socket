import socket

#총알장전

clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#s.connect(("127.0.0.1", 4444))

clientsocket.connect(("127.0.0.1", 6789))

test = """
POST /password.txt HTTP/1.1
Host: w3schools.com
name1=value1&name2=value2
"""
clientsocket.sendall(test.encode())
clientsocket.settimeout(10)
while 1:
	
	message, address = clientsocket.recvfrom(1024)
	print(message.decode())
	if not message:
		break
	
clientsocket.close()
