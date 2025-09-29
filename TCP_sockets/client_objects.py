import socket
import pickle
import sys
import time

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


    packet_list = []
    for i in range(3):

        ob = Packet(i+1,"")

        packet_list.append(ob)

    
    packet_list[0].set_message("This is packet 1")
    packet_list[1].set_message("This is packet 2")
    packet_list[2].set_message("This is packet 3")


    packet_list.append(Packet((i+2),"FIN"))

    port = 6001
    host = socket.gethostname()
    clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    clientSocket.connect( (host,port) )
    for each_packet in packet_list:

        data = pickle.dumps(each_packet)
        print("Sending",each_packet.get_sequence())
        clientSocket.send(data)
        time.sleep(1)       
        print("")
    

    print("Client done")






if __name__ == "__main__":
    main()