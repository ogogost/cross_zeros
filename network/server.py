import socket
import threading

HOST = 'localhost'
PORT = 12345


def process_connection(sock, all_connections):
    while True:
        try:
            data = sock.recv(1024)
            print(data)
            decoded_data = data.decode('utf-8')
            for conn in all_connections:
                conn.sendall(data)
        except:
            print("exception occured")
            break


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()

    connections = []

    while True:
        connection, addr = server.accept()
        connections.append(connection)
        threading.Thread(target=process_connection, args=(connection, connections)).start()