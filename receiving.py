from encryption import Enc

class Rcv():
    def __init__(self, pub_key, priv_key):
        self.pub_key = pub_key
        self.priv_key = priv_key
        self.peer_key = None

    def receive_key(self, key):
        peer_key = key.split('|')[-1]
        self.peer_key = peer_key
        print('Key received successfully!')

    def receive_file(self, sock, file_info):
        file, file_name, file_size = file_info.split('|')
        file_size = int(file_size)
        print('Receiving file:', file_name)
        file_name = "recived" + file_name
        with open(file_name, 'wb') as file:
            bytes_received = 0
            while bytes_received < file_size:
                data = sock.recv(1024)
                file.write(data)
                bytes_received += len(data)
                #print('Progress:', (bytes_received / file_size) * 100, '%')

        print('File received successfully!')

    def receive_messages(self, sock):
        enc = Enc(self.pub_key, self.priv_key)
        while True:
            data = sock.recv(1024).decode('utf-8')
            if data.startswith('KEY'):
                self.receive_key(data)
                break

        while True:
            try:
                data = sock.recv(1024)

                try:
                    data = data.decode('utf-8')
                except UnicodeDecodeError:
                    data = enc.decrypt_message(data)
                    data = data.decode('utf-8')

                if data.startswith('FILE'):
                    self.receive_file(sock, data)
                else:
                    print('Received:', data)

            except ConnectionResetError:
                print('Peer disconnected')
                break

