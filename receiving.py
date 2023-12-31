from encryption import Enc
import os
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
class Rcv:
    def __init__(self, pub_key, priv_key):
        self.pub_key = pub_key
        self.priv_key = priv_key
        self.peer_key = None
        self.aes_key = None
        self.sending_soc = None
        self.set_message = None
        self.file = None
        self.disconnect = None

    def receive_public_key(self, key):
        key = key.split('|')[-1]
        self.peer_key = key
        print('Key received successfully!')

    def receive_aes_key(self, key):
        enc = Enc(self.pub_key, self.priv_key)
        key = enc.decrypt_message(key)
        self.aes_key = key
        print('AES key received successfully!')

    def receive_file(self, file_info):
        file, file_name, file_size = file_info.split('|')
        file_size = int(file_size)
        print('Receiving file:', file_name)
        file_name = "recived" + file_name
        cipher = AES.new(self.aes_key, AES.MODE_ECB)

        with open(file_name, 'wb') as file:
            bytes_received = 0
            while bytes_received < file_size:
                data = self.sending_soc.recv(1024)
                #data = unpad(cipher.decrypt(data),16)
                file.write(data)
                bytes_received += len(data)
                #print('Progress:', (bytes_received / file_size) * 100, '%')

        self.set_message(f"File {file_name} received successfully")

    def send_file(self, file_path):
        #_, file_path = message.split(' ')
        file_name = file_path.split('/')[-1]
        file_size = os.path.getsize(file_path)
        cipher = AES.new(self.aes_key, AES.MODE_ECB)

        data = ('FILE|' + file_name + '|' + str(file_size)).encode('utf-8')
        data = cipher.encrypt(pad(data, 16))
        self.sending_soc.send(data)

        with open(file_path, 'rb') as file:
            while True:
                data = file.read(1024)
                if not data:
                    break

                #data2 = cipher.encrypt(pad(data, 16))
                self.sending_soc.send(data)

        self.set_message(f"File {file_name} send successfully")
        self.file = None

    def receive_messages(self):
        try:
            cipher = AES.new(self.aes_key, AES.MODE_ECB)

            while True:
                try:
                    data = self.sending_soc.recv(1024)
                    data = unpad(cipher.decrypt(data), 16)
                    data= data.decode()

                    if data.startswith('FILE'):
                        self.receive_file(data)
                    elif data.startswith('DISCONNECT'):
                        self.disconnect()

                    else:
                        self.set_message("Peer: "+data)
                except ConnectionResetError:
                    print('Peer disconnected')
                    break
        except ConnectionAbortedError:
            print('Peer disconnected')

    def send_messages(self, message):
        cipher = AES.new(self.aes_key, AES.MODE_ECB)

        if self.file is not None:
            self.send_file(self.file)
        else:
            self.set_message("You:  "+message)
            message = cipher.encrypt(pad(message.encode(), 16))
            self.sending_soc.send(message)