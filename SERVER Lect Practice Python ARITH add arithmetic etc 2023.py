'''
SERVER Lect Practice Python ARITH add arithmetic etc 2023
'''
from socket import *

def doOP(a,b,c):
#A-operator (1-add ie B + C, 2-subtract ie B-C, 3-divide ie B/C, 4-multiply ie B*C)    
 match a: 
  case 1:
    return b+c;

  case 2:
    return b-c;

  case 3:
    return b//c;

  case 4:
    return b*c;



serverPort = 12023

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))

serverSocket.listen(1)
print ("SERVER Lect Practice Python ARITH add arithmetic etc 2023 is ready to receive... ")
connectionSocket, addr = serverSocket.accept()
#addr is client that is connecting and connectionSocket is auxilliary socket at server
for i in range(0, 6):
    data = connectionSocket.recv(1024)
    print ("Received from Client: ", data.decode())

    val=int(data.decode("utf-8").strip())
    operator = val//100;
    print ("Operator is : ", str(operator))
    op1 = (val//10)%10;
    print ("Operand 1 is : ", str(op1))
    op2 = val%10;
    print ("Operand 2 is : ", str(op2))
    ans=doOP(operator, op1,op2)
    send_data=str(ans)
    message=send_data.encode('utf-8')

    connectionSocket.send(message)

    print ("Sent back to Client: ", message.decode())


connectionSocket.close()

"""
SERVER Lect Practice Python ARITH add arithmetic etc 2023 is ready to receive... 
Received from Client:  124
Operator is :  1
Operand 1 is :  2
Operand 2 is :  4
Sent back to Client:  6
Received from Client:  456
Operator is :  4
Operand 1 is :  5
Operand 2 is :  6
Sent back to Client:  30
Received from Client:  284
Operator is :  2
Operand 1 is :  8
Operand 2 is :  4
Sent back to Client:  4
Received from Client:  384
Operator is :  3
Operand 1 is :  8
Operand 2 is :  4
Sent back to Client:  2
Received from Client:  444
Operator is :  4
Operand 1 is :  4
Operand 2 is :  4
Sent back to Client:  16
Received from Client:  296
Operator is :  2
Operand 1 is :  9
Operand 2 is :  6
Sent back to Client:  3            
"""

