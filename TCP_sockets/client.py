import socket 

port = 9000
host = socket.gethostname()

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect( (host, port) )

clientSocket.send("hello!!!".encode())

response = clientSocket.recv(1024).decode()
print(response)