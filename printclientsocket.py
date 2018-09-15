import socket
import sys, time


host = '127.0.0.1'
port = 4444

timeout= 1

#Create UDP client socket
#Note the use of SOCK_DGRAM for UDP datagram packet

clientsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#Set socket timeout as 1 second

clientsocket.settimeout(timeout)

port = int(port)

ptime = 0

while ptime < 10:
	ptime+=1 

	# Format the message to be sent
	data = "Ping " + str(ptime) + " " + time.asctime()
	try:
		RTTb = time.time() # 이때시간값 저장
		clientsocket.sendto(data.encode(),((host, port)))

		# Receive the server response
		message, address = clientsocket.recvfrom(1024)

		RTTa = time.time()

		# Display the server response as an output

		print ("Reply from " + address[0] + " : " +message)

		print ("RTT : " + str(RTTa-RTTb))

	except socket.timeout as e:
		continue
	except Exception as e:
		print(e)

		print ("Request time out.")
		continue
clientsocket.close()