import ssl
import base64
from socket import *


cc = socket(AF_INET, SOCK_STREAM)
cc.connect(("smtp.gmail.com", 587))
# cc.read(..)

cc.send('helo tester.com\r\n'.encode())
cc.send('starttls\r\n'.encode())
# cc.read(..) If the server responds ok to starttls
#             tls negotiation needs to happen and all
#             communication is then over the SSL socket 
#
scc = ssl.wrap_socket(cc, ssl_version=ssl.PROTOCOL_TLSv1_2)
scc.send('auth login\r\n'.encode())
# scc.read(..)

scc.send(base64.b64encode('kjh07df@gmail.com')+'\r\n'.encode())
scc.send(base64.b64encode('xkdtn6@@')+'\r\n'.encode())
