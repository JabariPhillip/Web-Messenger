'''
Lect Practice PythonARITH_Client2023_ABC add arithmetic etc
123 means Find 2+3
456 means Find 5*6
284 means Find 8-4 

'''
from socket import *
from array import *

print ("The LECT ARITH Client is started... ")

numarr = [124,456,284,384,444,296]
print("Contents of numarr"+"\n")
for i in range(0, len(numarr)):
    print(numarr[i])

serverName = "localhost"
serverPort = 12023

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName,serverPort))
print(str(clientSocket))
for i in range(0, len(numarr)):
   print("Preparing to send " + str(numarr[i])+" to server"+"\n")
   send_data = str(numarr[i])
   message=send_data.encode('utf-8')
   clientSocket.send(message)
   print ("Sent ", send_data, " to server")
   result = clientSocket.recv(2024)
   print ("Received back from Server: ", result.decode()+"\n")
clientSocket.close()
'''
The LECT ARITH Client is started... 
Contents of numarr

124
456
284
384
444
296
<socket.socket fd=128, family=2, type=1, proto=0, laddr=('127.0.0.1', 50026), raddr=('127.0.0.1', 12023)>
Preparing to send 124 to server

Sent  124  to server
Received back from Server:  6

Preparing to send 456 to server

Sent  456  to server
Received back from Server:  30

Preparing to send 284 to server

Sent  284  to server
Received back from Server:  4

Preparing to send 384 to server

Sent  384  to server
Received back from Server:  2

Preparing to send 444 to server

Sent  444  to server
Received back from Server:  16

Preparing to send 296 to server

Sent  296  to server
Received back from Server:  3

'''
