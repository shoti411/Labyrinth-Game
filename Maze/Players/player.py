import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"../Common"))

from board import Board
from tile import Tile
from riemann import Riemann
from euclid import Euclid
from socket import socket
import json
from action import Pass, Move
from coordinate import Coordinate
import time

class PlayerAPI:
    """ This class should not be instantiated """
    def propose_board(self, rows, columns):
        raise NotImplemented('propose_board not implemented')

    def setup(self, game_state, goal_position):
        raise NotImplemented('setup not implemented')

    def take_turn(self, game_state):
        raise NotImplemented('take_turn not implemented')

    def won(self, w):
        raise NotImplemented('won not implemented')


class RemotePlayerAPI(PlayerAPI):
    """ Proxy playerAPI class. Communicates in json objects to a tcp socket. """

    FRAME_SIZE = 1024
    TIMEOUT = 15

    def __init__(self, name, connection, address):
        assert isinstance(connection, socket), 'Connection must be a TCP socket.'
        self.name = name
        self.address = address
        self.connection = connection


    def get_name(self):
        return self.name

    def send_message(self, msg):
        print(f'SENDING: {msg}')
        self.connection.sendall(bytes(json.dumps(msg), encoding='utf-8'))

    def propose_board(self, rows, columns):
        raise NotImplemented('propose_board not implemented')

    def setup(self, game_state, goal_position):
        json_state = False
        if game_state:
            json_state = game_state.to_json_notation()
        self.send_message(['setup', [json_state, goal_position.to_json_notation()]])
        return self.listen_for_response()

    def take_turn(self, game_state):
        # TODO: verify inputs are valid and well-formed
        # CANNOT TRUST CLIENTS
        self.send_message(['take-turn', [game_state.to_json_notation()]])
        choice = self.listen_for_response()
        if isinstance(choice, str) and choice == 'PASS':
            return Pass()
        elif isinstance(choice, list) and len(choice) == 4:
            is_row = choice[1] in ('LEFT', 'RIGHT')
            direction = 1 if choice[1] in ('DOWN', 'RIGHT') else -1
            return Move(choice[2],
                        direction,
                        choice[0],
                        is_row,
                        Coordinate(choice[3]['row#'], choice[3]['column#']))

    def won(self, w):
        self.send_message(['win', [w]])
        return self.listen_for_response()

    def listen_for_response(self):
        # TODO: ADD TIMEOUT ERRORS
        self.connection.settimeout(self.TIMEOUT)
        response = self.connection.recv(self.FRAME_SIZE)
        return self.__parse_message(response)

    def __parse_message(self, json_string):
        json_str = json_string.decode('utf-8')
        print(json_str)
        if json_str == 'void':
            return
        decoder = json.JSONDecoder()
        pos = 0
        objs = []
        while pos < len(json_str):
            json_str = json_str[pos:].strip()
            if not json_str:
                break
            obj, pos = decoder.raw_decode(json_str)
            objs.append(obj)
        return objs[0]


class LocalPlayerAPI(PlayerAPI):

    def __init__(self, name, strategy='Riemann'):
        self.name = name
        self.strategy = self.get_strategy(strategy)
        self.game_state = False
        self.goal_position = False

    def get_strategy(self, strategy):
        if strategy == 'Riemann':
            return Riemann()
        elif strategy == 'Euclid':
            return Euclid()

        raise ValueError(f'{strategy} does not exist')

    def get_name(self):
        return self.name

    def propose_board(self, rows, columns):
        board = []
        for i in range(rows):
            board.append([])
            for j in range(columns):
                board[i].append(Tile())
        return board

    def setup(self, game_state, goal_position):
        if game_state:
            self.game_state = game_state
        self.goal_position = goal_position

    def take_turn(self, game_state):
        self.game_state = game_state
        return self.strategy.evaluate_move(self.game_state)

    def won(self, w):
        return w


class BadPlayerAPI(LocalPlayerAPI):

    def __init__(self, name, error_function, error_count, strategy='Riemann'):
        """ :param: error_function <String>: represents the name of the function that will fail """
        assert 7 >= error_count >= 1, 'Error count must be a natural num between 1-7'
        super().__init__(name, strategy)
        self.error_function = error_function
        self.error_count = error_count

    def won(self, w):
        if self.error_function == 'win':
            self.error_count -= 1
            if self.error_count == 0:
                raise TimeoutError('win timed out.')
        else:
            return super().won(w)

    def take_turn(self, game_state):
        if self.error_function == 'takeTurn':
            self.error_count -= 1
            if self.error_count == 0:
                raise TimeoutError('take timed out.')
        else:
            return super().take_turn(game_state)

    def setup(self, game_state, goal_position):
        print('CALLED')
        if self.error_function == 'setUp':
            self.error_count -= 1
            if self.error_count == 0:
                raise TimeoutError('setup timed out.')
        else:
            return super().setup(game_state, goal_position)

