import socket
import base64
import ssl

msg = "\r\nI love hacking"
endmsg = "\r\n.\r\n"

# Choose a mail server
mailserver = 'smtp.gmail.com'

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# port number may change accoding to the mail server
clientSocket.connect((mailserver,587))
recv = clientSocket.recv(1024)

#print (recv.decode())

if recv[:3].decode() != '220':
	print ('220 reply not received from server')
	exit(1)
# Send HELO command and print server response

#heloCommand = "HELO gmail.com\r\n"
heloCommand = "HELO gmail.com\r\n"
clientSocket.send(heloCommand.encode())
recvfirst = clientSocket.recv(1024)
#print(recvfirst.decode())
if recvfirst[:3].decode() != '250':
	print ('250 reply not received frmo server.')

# Send MAIL FROM command and print server response
mailfrom = "EHLO Alice\r\n"

clientSocket.send(mailfrom.encode())
recvsecond = clientSocket.recv(1024)
#print(recvsecond.decode())
if recvsecond[:3].decode() != '250':
	print ('250 reply not received frmo server.')

#mailfrom = "MAIL FROM :<woclwjstk@gmail.com>\r\n"

AuthFrom = "STARTTLS\r\n"

clientSocket.send(AuthFrom.encode())
recvsecond = clientSocket.recv(1024)
#print(recvsecond.decode())
if recvsecond[:3].decode() != '220':
	print ('220 reply not received frmo server.')

##############################################

tlssocket = ssl.wrap_socket(clientSocket)

username = "kjh07df@gmail.com"
password = "xkdtn6@@"
base64_str = ("\x00"+username+"\x00"+password).encode()
base64_str = base64.b64encode(base64_str)


authMsg = "AUTH PLAIN ".encode()+base64_str+"\r\n".encode()


tlssocket.send(authMsg)

recvsecond = tlssocket.recv(1024)
print(recvsecond.decode())
if recvsecond[:3].decode() != '235':
	print ('235 reply not received frmo server.')
	raise Exception

###################login success#######################

tlssocket.send("MAIL from:<woclwjstk@naver.com>\r\n".encode())
recvsecond = tlssocket.recv(1024)
print(recvsecond.decode())

if recvsecond[:3].decode() != '250':
	print ('250 reply not received frmo server.')
	raise Exception


# SEND RCPT TO command and print server response

rcptto = 'RCPT TO:<kjh07df@gmail.com>\r\n'
tlssocket.send(rcptto.encode())
recvthird = tlssocket.recv(1024)
print(recvthird.decode())
if recvthird[:3].decode() != '250':
	print ('250 reply not received frmo server.')
	raise Exception

# SEND DATA cmmand and print server response

data = 'DATA\r\n'
tlssocket.send(data.encode())
recvfourth = tlssocket.recv(1024)
print (recvfourth.decode())
if recvfourth[:3].decode() != '354':
	print ('354 reply not received from server')

#Send message data.

tlssocket.send('SUBJECT: Greeting To you!\r\n'.encode())
tlssocket.send('bye'.encode())
tlssocket.send(msg.encode())

tlssocket.send(endmsg.encode())
recv5 = tlssocket.recv(1024)
print(recv5.decode())
if recv5[:3].decode() != '250':
	print ('250 reply not received from server')
	raise Exception

# Send QUIT command

quitCommand = 'QUIT\r\n'
tlssocket.send(quitCommand.encode())
recv6 = tlssocket.recv(1024)
print(recv6.decode())
if recv6[:3].decode() != '221':
	print ('221 reply not received from server')
	raise Exception

