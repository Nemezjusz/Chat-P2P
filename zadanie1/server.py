import socket
import threading

def handle_client(client_socket, client_address):
    # Obsługa połączenia z klientem
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                # Przekazanie wiadomości do wszystkich klientów
                for client in connected_clients:
                    if client != client_socket:
                        client.sendall(message.encode('utf-8'))
            else:
                # Zamknięcie połączenia, gdy klient się rozłączy
                client_socket.close()
                connected_clients.remove(client_socket)
                print(f'Klient {client_address} rozłączony.')
                break
        except Exception as e:
            print(f'Błąd obsługi klienta {client_address}: {e}')
            break

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 1234))
    server_socket.listen(5)
    print('Serwer czatu uruchomiony. Nasłuchiwanie na porcie 1234...')

    while True:
        client_socket, client_address = server_socket.accept()
        connected_clients.append(client_socket)
        print(f'Nowe połączenie od klienta {client_address}.')
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

# Inicjalizacja listy podłączonych klientów
connected_clients = []

# Uruchomienie serwera
start_server()


