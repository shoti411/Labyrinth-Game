import sys, os, socket, threading, time
sys.path.append(os.path.join(os.path.dirname(__file__), "../Remote"))
from referee import RefereeProxy




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

        threads = []
        for player in self.players:
            time.sleep(3)
            t = threading.Thread(target=player.receive_message)
            t.start()
            threads.append(t)
        
        #for t in threads:
        #    t.join()

        while True:
            players_playing = any([p.is_running for p in self.players])
            if not players_playing:
                return