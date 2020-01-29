import socket
import threading

from PyQt5.QtWidgets import QApplication

from network.simple_pyqt import PyQtWindow

HOST = 'localhost'
# HOST = 'aud21-prep'
PORT = 12345


def receive_data(sock, window):
    while True:
        data = sock.recv(1024)
        print(data)
        window.add_input(data.decode('utf-8'))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    app = QApplication([])
    window = PyQtWindow(lambda x: client.sendall(x))
    threading.Thread(target=receive_data, args=(client, window)).start()
    window.show()
    app.exec_()