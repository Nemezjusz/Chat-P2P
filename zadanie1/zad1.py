import socket
import threading
import os


def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024).decode('utf-8')
            print('Received:', data)
        except ConnectionResetError:
            print('Peer disconnected')
            break



def start_chat():
    room = input("1 - Stwórz pokój, 2 - Dołącz do pokju: ")

    if room == "1":
        listen_ip = '0.0.0.0'
        listen_port = int(input('Enter listening port: '))

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((listen_ip, listen_port))
        sock.listen(1)
        print('Waiting for incoming connection...')

        sending_sock, client_addr = sock.accept()
        print('Connected to peer:', client_addr)
        receive_thread = threading.Thread(target=receive_messages, args=(sending_sock,))
        receive_thread.start()

    else:
        target_ip = input('Enter peer IP: ')
        target_port = int(input('Enter peer port: '))

        sending_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sending_sock.connect((target_ip, target_port))
        print('Connected to peer')

        receive_thread = threading.Thread(target=receive_messages, args=(sending_sock,))
        receive_thread.start()

    while True:
        message = input()

        #tutaj uzupełnij kod aby wiadomości były przesyłane (jedna linijka tak naprawde)



start_chat()