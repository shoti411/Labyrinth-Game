import sys, os, time, socket

sys.path.append(os.path.join(os.path.dirname(__file__), "../Referee"))
from referee import Referee
from observer import Observer
sys.path.append(os.path.join(os.path.dirname(__file__), "../Remote"))
from player import RemotePlayerAPI

'''A server class used to host a game of labyrinth with multiple remote players.'''
class Server:

    FRAME_SIZE = 1024
    TIMEOUT_FOR_PLAYERS = 20

    '''A state may be passed in to begin a game from any point.  If this is false, a new game will be started with the
    connected players.  A referee may also be passed in in order to allow for the tracking of multiple goals (the referee contains
    this information).'''
    def __init__(self, hostname, port, referee=False, state=False):
        self.hostname = hostname
        self.port = port
        self.socket = self.boot_server()
        self.player_list = []
        if not referee:
            referee = Referee()
        self.game_outcome = self.listen_for_players(referee, state)

    def get_game_outcome(self):
        return self.game_outcome

    '''Sets up the socket connection which clients will use to connect.'''
    def boot_server(self):
        open_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (self.hostname, self.port)
        open_socket.bind(server_address)
        return open_socket

    '''Listens for players to connect to the server during the waiting period (two if necessary) and starts a game
    with the connected players.  Will use a state if it was passed into the class.'''
    def listen_for_players(self, referee, state):

        self.__waiting_period()

        if len(self.player_list) < 2:
            self.__waiting_period()

        if len(self.player_list) < 2:
            print('print not connecting')
            return [], []
        else:
            return self.start_game(referee, state)            

    '''Wait for players to connect for a predetermined amount of time and associate each connected player with a 
    RemotePlayerAPI to be used to play the game.'''
    def __waiting_period(self):
        t = time.time()
        while time.time() < t + self.TIMEOUT_FOR_PLAYERS and len(self.player_list) < 6:
            self.socket.listen()
            time_left = t + self.TIMEOUT_FOR_PLAYERS - time.time()
            self.socket.settimeout(time_left)
            try:
                connection, address = self.socket.accept()
                self.socket.settimeout(2) #seconds
                name = connection.recv(self.FRAME_SIZE).decode('utf-8')
                self.player_list.append(RemotePlayerAPI(name, connection, address))
            except socket.timeout:
                continue

    '''Start the game either from a given state or from scratch.  If started from a given state, associate the corresponding
    players in the game state with the RemotePlayerAPIs created for each connected player.'''
    def start_game(self, referee, state):
        if state:
            self.__add_apis_to_state(state)
            return referee.pickup_from_state(state)
        return referee.run(self.player_list)

    '''For each player in the state, associate them with a RemotePlayerAPI created for each player connection.'''
    def __add_apis_to_state(self, state):
        for i, p in enumerate(state.get_players()):
            p.set_player_api(self.player_list[i])