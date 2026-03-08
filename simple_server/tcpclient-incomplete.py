# simple tcp client
# inspiration from www.digitalocean.com/community/tutorials/python-socket-programming-server-client

import socket

def client_program(host, port):

    # create client socket instance
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

    # connect socket to server
    client_socket.connect((host, port))
     
    # receive initial server response 
    data = client_socket.recv(1024).decode()  
    print('Received from server: ' + data)  

    # take first input
    message = input(" -> ") + '\n'  

    while message.lower().strip() != 'bye':
        # send message
        client_socket.send(message.encode())    
    
        # receive response
        data = client_socket.recv(1024).decode()   
        print('Received from server: ' + data)
        
        # again take input  
        message = input(" -> ") + '\n'  

    client_socket.close()

if __name__ == '__main__':
    host = input("Enter host: ")
    port = int(input("Enter port: "))
    client_program(host, port)
