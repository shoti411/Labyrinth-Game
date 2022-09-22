import sys
import json
import socket

import xjson

if __name__ == "__main__":
    # connection
    server_address = ('login-students.ccs.neu.edu', int(sys.argv[1]))

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(server_address)
        s.listen()
        conn, addr = s.accept()

        # Grab input
        data = ''
        while True:
            input_line = conn.recv(1024).decode('ascii')
            if not input_line:
                break 
            data += input_line
            
        # Process input
        processed_data = xjson.xjson(data)
        conn.send(bytes(json.dumps(processed_data, ensure_ascii=False), 'utf-8'))

    # Open connection
    # Grab Input
    # process input
    # shut down