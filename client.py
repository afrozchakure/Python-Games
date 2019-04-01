import socket
import sys
import time

### init ###

s = socket.socket()
host = input(str("Please enter the hostname of the server:"))  # This gives the name of the host that is send to server.py
port = 8081
s.connect((host, port))  # connecting the host to port
print("Connected to chat server")  # It prints this if it is successful


# Here we are writing the code that will accept the message and display it to us

while(1):  # Since we need them to communicate endlessly we need the code in endless loop or a while() loop
    incoming_message = s.recv(1024) # "recv" is shortform for "receive"
    incoming_message = incoming_message.decode()# We need to decode the message because the we receive an encoded message
    print("Server:", incoming_message)
    print("")

    # This is to send messages to the server.py
    message = input(str(">>"))  # It is the symbol for entering a message
    message = message.encode()  # To change the message into bytes (it only supports bytes), we are overwriting the variable with its byte form
    s.send(message)  # Sending the message to the client
    print("Message has been sent...")
    print("")