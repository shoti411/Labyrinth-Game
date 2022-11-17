import sys, os, time, threading

sys.path.append(os.path.join(os.path.dirname(__file__), "../Common"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../Referee"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../Players"))

import socket
from referee import Referee
from player import RemotePlayerAPI


class Server:

    #TODO make something to close down the server if all connections close
    FRAME_SIZE = 1024
    TIMEOUT_FOR_PLAYERS = 5

    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.socket = self.boot_server()
        self.player_list = []

        self.listen_for_players()

    def boot_server(self):
        open_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (self.hostname, self.port)
        open_socket.bind(server_address)            
        open_socket.listen(6)
        return open_socket

    def listen_for_players(self):

        self.__waiting_period()

        if len(self.player_list) < 2:
            self.__waiting_period()
        
        self.socket.close()

        try:
            return self.start_game()
        except ValueError:
            return [[], []]

    def __waiting_period(self):
        t = time.time()
        while time.time() < t + self.TIMEOUT_FOR_PLAYERS and len(self.player_list) < 6:
            time_left = t + self.TIMEOUT_FOR_PLAYERS - time.time()
            self.socket.settimeout(time_left)
            try:
                print(time_left)
                connection, address = self.socket.accept()
                self.socket.settimeout(2)
                name = connection.recv(self.FRAME_SIZE).decode('utf-8')
                print(name)
                self.player_list.append(RemotePlayerAPI(name, connection, address))
                threading.Thread(target=self.client_thread, args=[connection]).start()
            except socket.timeout:
                continue
        print('finished waiting period')

    def start_game(self):
        if len(self.player_list) < 2:
            raise ValueError('Must have at least 2 players to run a game of Labyrinth.')
        ref = Referee()
        return ref.run(self.player_list)

    #set up a new thread so that we can have multiple clients connected
    #to this server
    def client_thread(self, conn):

        while True:
            data = conn.recv(self.FRAME_SIZE)
            if not data:
                break

        conn.close
