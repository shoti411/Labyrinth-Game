import socket
import json
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__),"../Common"))
sys.path.append(os.path.join(os.path.dirname(__file__),"../Players"))
from tile import Tile
from board import Board
from coordinate import Coordinate
from player_game_state import PlayerGameState
from action import Move, Pass, Action
from player_state import Player
import time

class RefereeProxy:

    FRAME_SIZE = 1024
    VALID_FUNCTION_NAMES = ['setup', 'take-turn', 'win']

    def __init__(self, player, conn):
        self.player = player
        self.socket = conn
        self.player_mechanism = False
        self.is_running = True

    def receive_message(self):
        byte_string = self.socket.recv(self.FRAME_SIZE)
        try:
            message = self.parse_message(byte_string)
        except json.decoder.JSONDecodeError as e:
            print(e)
            self.receive_message()

        if self.__is_valid(message):
            self.__send_message(self.__call_player_functions(message))

        if message[0] == 'win':
            self.is_running = False
            return

        self.receive_message()

    def __send_message(self, message):
        self.socket.send(bytes(message, encoding='utf-8'))

    def __call_player_functions(self, msg):
        func_name = msg[0]
        send_back = 'void'
        args = msg[1]
        if func_name == 'setup':
            state, goal = self.__setup(args[0], args[1])
            self.player.setup(state, goal)
        elif func_name == 'take-turn':
            state = self.__take_turn(args[0])
            send_back = self.choice_to_json(self.player.take_turn(state))
        elif func_name == 'win':
            self.player.won(args[0])
        return send_back

    def choice_to_json(self, choice):
        if choice.is_pass():
            return 'PASS'
        index = choice.get_index()
        degree = choice.get_degree()
        coord = choice.get_coordinate()
        coord = {"row#": coord.getX(), 'column#': coord.getY()}
        direction = "DOWN" if choice.get_direction() == 1 else "UP"
        if choice.get_direction() == -1:
            direction = "RIGHT" if choice.get_direction() == 1 else "LEFT"
        return [index, direction, degree, coord]


    def __setup(self, state_json, goal_json):
        board, spare_tile, last_action = self.__parse_state(state_json)

        curr_coord = self.__parse_coordinate(state_json['plmt'][0]['current'])
        curr_tile = board.getTile(curr_coord)

        home_coord = self.__parse_coordinate(state_json['plmt'][0]['home'])
        home_tile = board.getTile(home_coord)

        goal_coord = self.__parse_coordinate(goal_json)
        goal_tile = board.getTile(goal_coord)

        self.player_mechanism = Player('', home_tile, goal_tile, curr_tile, goal_tile == home_tile)
        return PlayerGameState(board, spare_tile, self.player_mechanism, last_action), goal_coord

    def __take_turn(self, state_json):
        board, spare_tile, last_action = self.__parse_state(state_json)
        return PlayerGameState(board, spare_tile, self.player_mechanism, last_action)

    def __parse_coordinate(self, coord_json):
        return Coordinate(coord_json['row#'], coord_json['column#'])

    def __parse_state(self, json_state):
        board = self.json_to_board(json_state)
        spare_tile = Tile(json_state['spare']['tilekey'])
        last_action = self.json_to_last_action(json_state['last'])
        if last_action is None:
            last_action = False
        return board, spare_tile, last_action

    def json_to_board(self, json_object):
        #TODO add gem parsing
        board_strings = (json_object['board']['connectors'])
        board_obj = []
        for row in range(len(board_strings)):
            board_obj.append([])
            for col in range(len(board_strings[row])):
                board_obj[row].append(Tile(board_strings[row][col]))
        return Board(board=board_obj)
    
    def json_to_last_action(self, json_object):
        if not json_object:
            return Pass()
        index = json_object[0]
        if json_object[1] == "LEFT":
            is_row = True
            direction = -1
        elif json_object[1] == "RIGHT":
            is_row = True
            direction = 1
        elif json_object[1] == "UP":
            is_row = False
            direction = -1
        elif json_object[1] == "DOWN":
            is_row = False
            direction = 1
        else:
            raise ValueError("BAD JSON")
        return Move(0, direction, index, is_row, Coordinate(0, 0))


    def __is_valid(self, msg):
        if len(msg) != 2:
            return False
        if not msg[0] in self.VALID_FUNCTION_NAMES:
            return False
        if msg[0] == 'setup' and len(msg[1]) != 2:
            return False
        if msg[0] == 'take-turn' and len(msg[1]) != 1:
            return False
        if msg[0] == 'win' and len(msg[1]) != 1:
            return False
        return True

    def parse_message(self, json_string):
        print(json_string)
        json_str = json_string.decode('utf-8')
        decoder = json.JSONDecoder()
        pos = 0
        objs = []
        while pos < len(json_str):
            json_str = json_str[pos:].strip()
            print(json_str)
            if not json_str:
                break
            obj, pos = decoder.raw_decode(json_str)
            print(obj)
            objs.append(obj)
        return objs[0]
