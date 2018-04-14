from socket import *
import threading

LOCALHOST = '0.0.0.0'
BUFFER_SIZE = 1024

def main():

    class ChatListener(threading.Thread):

        def __init__(self):
            threading.Thread.__init__(self)
            self.port = 8080

        def run(self):
            listen_socket = socket(AF_INET, SOCK_STREAM)

            try:
                listen_socket.bind((LOCALHOST, self.port))
                listen_socket.listen(1)

            except:
                print("Could not connct on address {}".format(LOCALHOST))
                Exception


            connection, address = listen_socket.accept()
            print("\nEstablished connection with: ", address)

            while True:

                try:
                    message = connection.recv(BUFFER_SIZE)
                    if message:
                        new_data = message.decode()
                        print("Them: {}".format(new_data))

                except:
                    print("Did not connect LISTENER")
                    Exception

    class ChatSender(threading.Thread):

        def __init__(self):
            threading.Thread.__init__(self)
            self.address = 'spice'
            self.port = 9090

        def run(self):
            send_socket = socket(AF_INET, SOCK_STREAM)
            try:
                send_socket.connect((self.address, self.port))

            except:
                print("Connection possibly failed on address {} and port {}".format(self.address, self.port))
                send_socket.close()

            while True:
                message = input("You: \n")

                if message.lower() == "quit":
                    break
                else:
                    try:
                        send_socket.sendall(str(message).encode())
                    except:
                        print("Did not accept SENDER")
                        Exception

    # ip_listen = input("Please enter the address you would like to listen on: ")
    # LOCALHOST = ip_listen
    #port_listen = int(input("Please enter the port you would like to listen on: "))
    chat_listener = ChatListener()
    # chat_listener.port = port_listen
    chat_listener.start()

    ready = input("Press enter to connect")
    #ip_send = input("Please enter the address you would like to connect on: ")
    #port_sender = int(input("Please enter the port you would like to connect on: "))
    chat_sender = ChatSender()
    # chat_sender.address = ip_send
    # chat_sender.port = port_sender
    chat_sender.start()


if __name__ == "__main__":
    main()
