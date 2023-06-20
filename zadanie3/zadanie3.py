import socket
import threading

sending_sock = None

def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024).decode('utf-8')
            print('Otrzymano:', data)
        except ConnectionResetError:
            print('Użytkownik rozłączony')
            break

def create_room():
    global sending_sock
    listen_ip = '0.0.0.0'
    listen_port = int(input('Podaj port nasłuchu: '))

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((listen_ip, listen_port))
    sock.listen(1)
    print('Oczekiwanie na przychodzące połączenie...')

    sending_sock, client_addr = sock.accept()
    print('Połączono z użytkownikiem:', client_addr)
    receive_thread = threading.Thread(target=receive_messages, args=(sending_sock,))
    receive_thread.start()

def join_room():
    global sending_sock
    target_ip = input('Podaj IP użytkownika: ')
    target_port = int(input('Podaj port użytkownika: '))

    #brakujący kod do uzupelnienia
    ##
    ##
    print('Połączono z użytkownikiem')
    #brakujący kod do uzupelnienia
    ##
    ##

def start_chat():
    room = input("1 - Stwórz pokój, 2 - Dołącz do pokoju: ")

    if room == "1":
        create_room()
    else:
        join_room()



start_chat()
