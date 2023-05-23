import socket
import threading
import os
from encryption import Enc
from receiving import Rcv
import rsa

def send_file(sock, message):
    _, file_path = message.split(' ')
    file_name = file_path.split('/')[-1]
    file_size = os.path.getsize(file_path)

    sock.send(('FILE|' + file_name + '|' + str(file_size)).encode('utf-8'))

    with open(file_path, 'rb') as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            sock.send(data)

    print('File sent successfully!')


def start_chat():
    room = input("1 - Stwórz pokój, 2 - Dołącz do pokju: ")
    (pub_key, priv_key) = rsa.newkeys(512)
    enc = Enc(pub_key, priv_key)
    rcv = Rcv(pub_key, priv_key)

    if room == "1":
        listen_ip = '0.0.0.0'
        listen_port = 777  # int(input('Enter listening port: '))

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((listen_ip, listen_port))
        sock.listen(1)
        print('Waiting for incoming connection...')

        sending_sock, client_addr = sock.accept()
        print('Connected to peer:', client_addr)
        receive_thread = threading.Thread(target=rcv.receive_messages, args=(sending_sock,))
        receive_thread.start()

    else:
        target_ip = '192.168.0.18' #input('Enter peer IP: ')
        target_port = 777  # int(input('Enter peer port: '))

        sending_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sending_sock.connect((target_ip, target_port))
        print('Connected to peer')

        receive_thread = threading.Thread(target=rcv.receive_messages, args=(sending_sock,))
        receive_thread.start()

    enc.send_key(sending_sock)

    while True:
        message = input()
        message_encoded = message.encode('utf-8')

        if message.startswith('SEND'):
            send_file(sending_sock, message)
        else:
            n, e = str(rcv.peer_key).split(",")
            enc_message = enc.encrypt_message(message_encoded, rsa.PublicKey(int(n), int(e)))
            sending_sock.send(enc_message)


start_chat()