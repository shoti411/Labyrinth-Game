import sys
import socket

if __name__ == "__main__":
    port = int(12345)
    server_address = ('localhost', port)
    socket.create_connection(server_address)

