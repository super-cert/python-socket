import socket

serversocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

serversocket.bind(('127.0.0.1',4444))

#serversocket.listen(10) only tcp
i = 0
while True:
	i+=1
	data, addr = serversocket.recvfrom(1024)
	print (addr, ' : ', data)
	if(i>10):
		break


print(addr,' : ' ,msg.decode())
