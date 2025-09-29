import socket
import pickle
import sys

class Packet():


    def __init__(self,sequence_number,message):
        self.sequence_number = sequence_number
        self.message = message
    
    def set_message(self,new_message):
        self.message = new_message
    
    def get_message(self):
        return self.message

    def get_sequence(self):
        return self.sequence_number

def main():


    port = 6001
    host = socket.gethostname()
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind( (host,port) )

    print("Server is listening")

    serverSocket.listen(1)


    connection,addr = serverSocket.accept()
    while True:
        
        data = connection.recv(1024)
        ob = pickle.loads(data)
        print(ob.get_message())
        print(ob.get_sequence())
        print("")
        if ob.get_message() == "FIN":
            break

    print("Server done")







if __name__ == "__main__":
    main()