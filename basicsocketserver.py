import socket

host = '127.0.0.1'
port = 4444

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
serversocket.bind((host,port))
serversocket.listen(1)

connection, addr = serversocket.accept()  #연결되면?
msg = connection.recv(1024)

print(msg.decode())
connection.close()






