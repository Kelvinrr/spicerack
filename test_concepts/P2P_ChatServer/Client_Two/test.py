import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname()
print(host)
