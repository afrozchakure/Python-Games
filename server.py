# We need to make the program on a local
import socket
import sys
import time

## end of import ##

### init ###

s = socket.socket()
host = socket.gethostname()  # It gets the local host name of your device
print(host)
print("Server will start on host:", host)  # prints the local host name of your device
port = 8081
s.bind((host, port))  # we need to bind the socket with host before we start getting incoming connections
print("")
print("Server done binding to host and port successfully")  # Creating a message
print("")

print("Server is waiting for incoming connections")
print("")

s.listen(1)  # Inside the bracket we give the number of connections we are looking to expect
conn, addr = s.accept()
# The first variable "conn" is assigned to the socket itself which is the physical socket coming from the client
# And "addr" is assigned to the IP address of the client that is going to be connecting
# print(addr)  # It prints the IP address or the host name of the program that is connected to us
print(addr, "Has connected to server and is now online...")
print("")

# Now we have connected the server and the client with each other we need to start sending packets to each other


# Sending a message
while(1):
    message = input(str(">>"))  # It is the symbol for entering a message
    message = message.encode()  # To change the message into bytes (it only supports bytes), we are overwriting the variable with its byte form
    conn.send(message)  # Sending the message to the client
    print("Message has been sent...")
    print("")

    # We are going to receive data from the client side
    incoming_message = conn.recv(1024)  # "recv" is shortform for "receive"
    incoming_message = incoming_message.decode()  # We need to decode the message because the we receive an encoded message
    print("Client:", incoming_message)
    print("")

###
