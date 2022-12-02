import sys, os, time, socket

sys.path.append(os.path.join(os.path.dirname(__file__), "../Referee"))
from referee import Referee
from observer import Observer
sys.path.append(os.path.join(os.path.dirname(__file__), "../Remote"))
from player import RemotePlayerAPI


class Server:

    FRAME_SIZE = 1024
    TIMEOUT_FOR_PLAYERS = 20

    def __init__(self, hostname, port, state=False):
        self.hostname = hostname
        self.port = port
        self.socket = self.boot_server()
        self.player_list = []
        self.game_outcome = self.listen_for_players(state)

    def get_game_outcome(self):
        return self.game_outcome

    def boot_server(self):
        open_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (self.hostname, self.port)
        open_socket.bind(server_address)
        return open_socket

    def listen_for_players(self, state):

        self.__waiting_period()

        if len(self.player_list) < 2:
            self.__waiting_period()

        if len(self.player_list) < 2:
            print('print not connecting')
            return [], []
        else:
            return self.start_game(state)            

    def __waiting_period(self):
        t = time.time()
        while time.time() < t + self.TIMEOUT_FOR_PLAYERS and len(self.player_list) < 6:
            self.socket.listen()
            time_left = t + self.TIMEOUT_FOR_PLAYERS - time.time()
            self.socket.settimeout(time_left)
            try:
                connection, address = self.socket.accept()
                self.socket.settimeout(2)
                name = connection.recv(self.FRAME_SIZE).decode('utf-8')
                self.player_list.append(RemotePlayerAPI(name, connection, address))
            except socket.timeout:
                continue

    def start_game(self, state):
        #obs = Observer()
        ref = Referee()#observer=obs)
        if state:
            self.__add_apis_to_state(state)
            return ref.pickup_from_state(state)
        return ref.run(self.player_list)

    def __add_apis_to_state(self, state):
        for i, p in enumerate(state.get_players()):
            p.set_player_api(self.player_list[i])