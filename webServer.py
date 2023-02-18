from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a server
socketserverHost = '192.168.20.7'
serverPort = 13331
serverSocket.bind((serverHost, serverPort))
serverSocket.listen(5)
while True:print ('Ready to serve ..')
#Establishing connection with client
connectionSocket, addr = serverSocket.accept()
print ('Received connection is: ', addr)
try:message = connectionSocket.recv(1024)
#Recieve TCP message
filename = message.split()[1]
f = open(filename[1:])
outputdata = f.read(1024)
#Open and Read file
print('outputdata: ',outputdata)
connectionSocket.sendall('\n HTTP/1.1 200 OK\r\n\r\n'.encode('utf-8'))
