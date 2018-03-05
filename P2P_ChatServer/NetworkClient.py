from socket import *
import _thread
import time

#holds instances of both a ChatListener and ChatSender
class Client():
    def __init__(self, my_ip, my_port):
        #create a listener
        self.my_ip = my_ip
        self.my_port = my_port
        self.chat_listener = ChatListener(self.my_ip, self.my_port)
        #creates a thread to call the method that connects to all available connections
        #_thread.start_new_thread(self.connect, ())

    def connect(self, address):
        #loop through connections in dictionary from configuration file
        #this dictionary is in ChatListener
        # for connection in self.chat_listener.availableConnections.keys():
        # self.chat_sender = ChatSender(connection, self.chat_listener.availableConnections[connection][1])
        self.chat_sender = ChatSender(address, self.chat_listener.availableConnections[connection][1])
        self.chat_sender.sendMessage()


class ChatListener():

    def __init__(self, host, port):
        #read in configuration file here
        #parsing section
        #self.availableConnections = {'192.168.1.109': ('Daniel', 50044), '192.168.1.111':('Daniel1', 30043)}
        self.availableConnections = {'192.168.0.100': ('Daniel', 50044)}
        self.activeConnectionsDict = {}
        self.connection_num = 0
        self.myIP = host
        self.myPort = port
        self.activeSenderFlag = 0

        #create listening socket
        #create a thread to listen for incoming connections
        self.port = port
        self.host = host
        self.listen_socket = socket(AF_INET, SOCK_STREAM)
        self.listen_socket.bind((self.myIP, self.myPort))
        self.listen_socket.listen(5)

        _thread.start_new_thread(self.listenConnections, ())

    #continue to listen for incoming connections from inside execution thread
    def listenConnections(self):
        while True:
            clientsocket, clientaddress = self.listen_socket.accept()
            print("Client connected from %s:%s" % clientaddress)
            _thread.start_new_thread(self.receive, (clientsocket, clientaddress))
            _thread.start_new_thread(self.addClient, (clientaddress[0], clientaddress[1]))

    #receive and display messages from active connections
    def receive(self, clientsocket, clientaddress):
        while True:
            message = clientsocket.recv(1024)
            if message.decode() != '':
                print(clientaddress[0] + ': ' + message.decode())
                #print(self.availableConnections[clientaddress][0][0] + ': ' + message.decode())

    #creates a sending connection with the client who just connected to you
    def addClient(self, address, port):
        not_connected = True
        while not_connected:
            if self.activeSenderFlag == 0:
                clientSendSocket = socket(AF_INET, SOCK_STREAM)
                clientSendSocket.connect((address, self.availableConnections[address][1]))
                print("Connected to client on " + address)
                self.activeSenderFlag = 1
                self.activeConnectionsDict[address] = clientSendSocket
                self.connection_num += 1
                not_connected = False
                _thread.start_new_thread(self.sendMessage, (address, port))
            else:
                pass

    #sends messages to the client which connected to you
    #shouldn't be a loop through all active connections, should take in specific connection for each message
    def sendMessage(self, address, port):
        while True:
            message = input("")
            if message != '':
                if message == 'quit' or message == 'QUIT':
                    print("Connection closed.")
                    self.activeConnectionsDict[address].close()
                    self.activeSenderFlag = 0
                else:
                    self.activeConnectionsDict[address].send(str(message).encode())

class ChatSender():

    #initialize socket and connection to message receiver
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.send_socket = socket(AF_INET, SOCK_STREAM)
        self.send_socket.connect((self.address, self.port))
        print("Connected to " + str(self.address) + " in sender class")

    #send message to ip and port above
    def sendMessage(self):
        while True:
            message = input("")
            if message == 'End Connection':
                self.send_socket.close()
                break
            elif message != '':
                self.send_socket.sendall(str(message).encode())

#main method to run the network
def main():

    #chat_listener = ChatListener('192.168.1.110', 40050)
    #chat_sender = ChatSender('192.168.1.109', 30012)
    client = Client('192.168.0.103', 40050)

    while True:
        pass


if __name__ == "__main__":
    main()
