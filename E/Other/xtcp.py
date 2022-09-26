import sys
import json
import socket
import xjson


# The maximum number of bytes the connection will read at a time.
PACKET_SIZE = 1024

# The IP hostname for our tcp server
HOSTNAME = 'login-students.ccs.neu.edu'


def connect_tcp():
    """
    Creates a server socket that listens for a client connection. Once a connection is requested,
    this function accepts and returns the connection and server socket.

    :return: connection  (socket) : the socket object that has been bound to the accepted connection
             open_socket (socket) : the server socket object
    """
    open_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = (HOSTNAME, int(sys.argv[1]))
    open_socket.bind(server_address)
    open_socket.listen()

    connection, address = open_socket.accept()
    return connection, open_socket


def collect_input(connection):
    """
    Accepts a connected socket and decodes all bytes that are being received. Ends when input stream
    closes.

    :param: connection (socket) : socket object that has been bound to an accepted connection
    :return: input_data (string) : decoded bytes from a connection socket
    """
    input_data = ''
    while True:
        input_line = connection.recv(PACKET_SIZE).decode('ascii')
        if not input_line:
            break
        input_data += input_line
    return input_data


def xtcp():
    """
    Creates a TCP server socket, waits for a single client connection and accepts, consumes series of JSON values until
    connection is closed, then delivers corresponding acceptable strings as JSON object to the output side of client
    TCP connection. Shuts down.

    Program takes 1 command line argument, [10000-60000] representing the port number.
    """
    conn, host = connect_tcp()
    data = collect_input(connection=conn)
    processed_data = xjson.xjson(data)
    conn.send(bytes(json.dumps(processed_data, ensure_ascii=False), 'utf-8'))
    host.close()


if __name__ == "__main__":
    xtcp()
