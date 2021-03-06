#Script: networking_server.py
#Author: Mahalakshmi Subramanian
#Anita Borg - Python Certification Course

#DESCRIPTION: A python script to create server and connect with client by establishing socket connection
#             on same host and port. Using recv(), the encrypted messages upto 1024 bytes are received

''' Sample data
Client sends: Jlkqv Mvqelk
Server sends back:Received: Jlkqv Mvqelk
Translation: monty python
'''

import socket
import CeasarCipherFunction as cc

#create server socket object and connect it with client
my_socket=socket.socket()
my_socket.connect(('localhost',4000))

#receive message from client with max 1024 bytes
received_msg=my_socket.recv(1024)

#This block is to receive encrypted messages from client,decode them and
#return decrypted messages using my_ceasar_decryption function until client keeps sending the message

while received_msg:
    encrypted_text=received_msg.decode()
    print("Received:",encrypted_text)
    print("Translation:",cc.my_ceasar_decryption(encrypted_text)+"\n")
    received_msg = my_socket.recv(1024)

my_socket.close()