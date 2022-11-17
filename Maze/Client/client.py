import sys, os, socket, threading

sys.path.append(os.path.join(os.path.dirname(__file__), "../Referee"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../Players"))

from referee_proxy import RefereeProxy
from player import LocalPlayerAPI


class Client:
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.players = []

    def connect_players(self, players):
        for player in players:
            open_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            open_socket.connect((self.hostname, self.port))
            open_socket.send(bytes(f'{player.get_name()}', encoding='utf-8'))
            ref_prox = RefereeProxy(player, open_socket)
            ref_prox.receive_message()
            self.players.append(RefereeProxy(player, open_socket))
            print(self.players)

        for player in self.players:
            threading.Thread(target=player.receive_message).start()

        while True:
            players_playing = any([p.is_running for p in self.players])
            if not players_playing:
                return
