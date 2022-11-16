import sys
import os
import socket

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
            self.players.append(RefereeProxy(player, open_socket))
