import socket

# CLIENT
host = socket.gethostname()
recv_port = 9000

connection = (host, recv_port)

#UDP Socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.bind( connection )

message = input("Enter a string to reverse")

print("Sending to server",message)

send_host = socket.gethostname()
send_port = 8000
send = (send_host, send_port)

clientSocket.sendto(message.encode(), send )

response = clientSocket.recvfrom(1024)
print(response[0].decode())
