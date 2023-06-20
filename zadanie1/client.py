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
    # Tutaj połącz się z socketem

    
    # # Wątek do odbierania wiadomości od serwera (odkomentuj)
    # receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    # receive_thread.start()
    
    # Tutaj wprowadz wysyłanie wiadomości



# Uruchomienie klienta
start_client()
