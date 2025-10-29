import socket

#SERVER
host = socket.gethostname()
recv_port = 8000

connection = (host, recv_port)

#define a UDP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSocket.bind(connection)

print("Waiting for data...")
while(True):

    data = serverSocket.recvfrom(1024)
    #data[0] = message
    #data[1] = remote socket connection
    conn = data[1]
    
    print("String recieved",data[0])

    message = list(data[0].decode())

    message.reverse()

    message = "".join(message)

    serverSocket.sendto(message.encode(), conn)
