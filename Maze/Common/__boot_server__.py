import sys
import os
import socket
import threading

sys.path.append(os.path.join(os.path.dirname(__file__), "../Server"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../Client"))

from server import Server


s = Server('localhost', 888)