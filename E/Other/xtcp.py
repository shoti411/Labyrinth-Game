import sys
import socket

if __name__ == "__main__":
    port = int(12345)
    server_address = ('127.0.0.1', port)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(server_address)
        s.listen()
        conn, addr = s.accept()
        data = ''
        while True:
            data += str(conn.recv(1024))
            if not data:
                break
