import socket
import threading


def receive_messages(client_socket):
    # Odbieranie wiadomości od serwera i wyświetlanie ich
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except Exception as e:
            print(f'Błąd odbierania wiadomości: {e}')
            break


def start_client():
    # client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client_socket.connect(('localhost', 1234))

    # print('Połączono z serwerem czatu.')
    #
    # # Wątek do odbierania wiadomości od serwera
    # receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    # receive_thread.start()
    #
    # # Wysyłanie wiadomości do serwera
    # while True:
    #     message = input()
    #     client_socket.sendall(message.encode('utf-8'))
    return


# Uruchomienie klienta
start_client()