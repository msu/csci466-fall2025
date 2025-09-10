import socket

print("server is starting!!!")

port = 9000
host = socket.gethostname()

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind( (host, port) )
serverSocket.listen(1)

connection, adrr = serverSocket.accept()

data = connection.recv(1024).decode()

print(data)

connection.send("Got it!!!!".encode())