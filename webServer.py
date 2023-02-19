# import socket module
from socket import *
# import socket

import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a sever socket to bind to an IP and listen for one connection

# Fill in start
IP = '127.0.0.1'
PORT = 13331
serverSocket.bind((IP, PORT))
serverSocket.listen(1)
# Fill in end

while True:
    # Establish the connection
    print('The server is ready to receive')

    # Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()
    # Fill in start #Fill in end

    # If an exception occurs during the execution of try clause
    # the rest of the clause is skipped
    # If the exception type matches the word after except
    # the except clause is executed
    try:
        # Receives the request message from the client (bytes and the message will need to be decoded)
        message = connectionSocket.recv(1024)  # Fill in start #Fill in end

        # Extract the path of the requested object from the message

        # The path is the second part of HTTP header, identified by [1]
        filename = message.split()[1]

        # Because the extracted path of the HTTP request includes
        # a character '\', we read the path from the second character
        f = open(filename[1:])

        # Store the entire contents read of the requested file in a temporary buffer

        # Fill in start
        outputdata = f.read()
        # Fill in end

        # Send one HTTP header line into socket

        # Fill in start
        connectionSocket.send('HTTP/1.1 200 OK\n\n'.encode())
        # Fill in end

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        # Close the client connection socket
        connectionSocket.close()

    except IOError:
        # Send HTTP response message for file not found (http type and status code) - you will need to encode this
        # Send the HTTP message too you will need to encode this

        # Fill in start
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n'.encode())
        # Fill in end

        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data