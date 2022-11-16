import sys
import os
import socket
import threading
import random

sys.path.append(os.path.join(os.path.dirname(__file__), "../Server"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../Client"))

from server import Server

for player in range(5):
    open_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    open_socket.connect(('localhost', 888))
    name = ("%06x" % random.randint(0, 0xFFFFFF)).upper()
    open_socket.send(bytes(f'{name}', encoding='utf-8'))
