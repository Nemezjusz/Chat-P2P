import socket
import threading
import os
from encryption import Enc
from receiving import Rcv
import rsa
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad

class Chat:
    def __init__(self,rcv,enc):
        self.rcv = rcv
        self.enc = enc
        self.my_sock= None
        self.set_status = None
        self.set_peer_ip = None
        self.set_port = None

    def start_chat_await(self):
        listen_ip = '0.0.0.0'
        listen_port = 888  # int(input('Enter listening port: '))
        self.set_port(str(listen_port))

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((listen_ip, listen_port))
        self.my_sock = sock
        await_thread = threading.Thread(target=self.await_connection)
        await_thread.start()

    def await_connection(self):
        self.my_sock.listen(1)
        print('Waiting for incoming connection...')
        self.set_status("Awaiting")
        self.start_chat()

    def start_chat(self):
        sending_sock, client_addr = self.my_sock.accept()
        self.rcv.sending_soc = sending_sock
        print('Connected to peer:', client_addr[0])

        self.set_status("Connected")
        self.set_peer_ip(str(client_addr[0]))

        aes_key = get_random_bytes(16)
        self.rcv.aes_key = aes_key

        while True:
            data = sending_sock.recv(1024).decode('utf-8')
            if data.startswith('KEY'):
                self.rcv.receive_public_key(data)
                break

        n, e = str(self.rcv.peer_key).split(",")
        encrypted_key = self.enc.encrypt_message(aes_key, rsa.PublicKey(int(n), int(e)))
        self.enc.send_aes_key(sending_sock, encrypted_key)

        receive_thread = threading.Thread(target=self.rcv.receive_messages)
        receive_thread.start()

    def start_chat_connect(self):

        target_ip = '192.168.0.18'  # input('Enter peer IP: ')
        target_port = 888  # int(input('Enter peer port: '))

        sending_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sending_sock.connect((target_ip, target_port))
        self.rcv.sending_soc = sending_sock
        print('Connected to peer')

        self.set_status("Connected")
        self.set_peer_ip(str(target_ip))
        self.set_port(str(target_port))

        self.enc.send_public_key(sending_sock)
        while True:
            data = sending_sock.recv(1024)
            self.rcv.receive_aes_key(data)
            break

        receive_thread = threading.Thread(target=self.rcv.receive_messages)
        receive_thread.start()

    def disconnect(self):
        self.rcv.sending_soc.close()
        self.rcv.sending_soc = None
        self.set_status("Disconnected")