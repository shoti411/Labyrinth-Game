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
from gems import Gem, get_gem_by_string

class RefereeProxy:

    FRAME_SIZE = 100000
    VALID_FUNCTION_NAMES = ['setup', 'take-turn', 'win']

    def __init__(self, player, conn):
        self.player = player
        self.socket = conn
        self.player_mechanism = False
        self.is_running = True

    def receive_message(self):
        byte_string = self.socket.recv(self.FRAME_SIZE)
        if byte_string == b'':
            return
        try:
            message = self.parse_message(byte_string)
        except json.decoder.JSONDecodeError as e:
            self.receive_message()

        if self.__is_valid(message):
            self.__send_message(self.__call_player_functions(message))

        if message[0] == 'win':
            self.is_running = False
            return

        self.receive_message()

    def __send_message(self, message):
        #print(f'SENDING {message}')
        self.socket.send(bytes(message, encoding='utf-8'))

    def __call_player_functions(self, msg):
        func_name = msg[0]
        send_back = 'void'
        args = msg[1]
        if func_name == 'setup':
            if not args[0]:
                self.player.setup(args[0], self.__parse_coordinate(args[1]))
                self.player_mechanism.reached_goal()
                self.player_mechanism.set_goal(self.player_mechanism.get_home())
            else:
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
        if choice.get_isrow():
            direction = "RIGHT" if choice.get_direction() == 1 else "LEFT"
        return json.dumps([index, direction, degree, coord])


    def __setup(self, state_json, goal_json):
        board, spare_tile, last_action = self.__parse_state(state_json)

        curr_coord = self.__parse_coordinate(state_json['plmt'][0]['current'])

        home_coord = self.__parse_coordinate(state_json['plmt'][0]['home'])
        home_tile = board.getTile(home_coord)

        goal_coord = self.__parse_coordinate(goal_json)
        goal_tile = board.getTile(goal_coord)
        self.player_mechanism = Player('', home_tile, goal_tile, curr_coord, goal_tile == home_tile)
        return PlayerGameState(board, spare_tile, self.player_mechanism, last_action), goal_coord

    def __take_turn(self, state_json):
        # TODO: UPDATE POSITION
        board, spare_tile, last_action = self.__parse_state(state_json)
        my_data = state_json['plmt'][0]
        my_position = my_data['current']
        self.player_mechanism.set_coordinate(self.__parse_coordinate(my_position))
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
        board_strings = (json_object['board']['connectors'])
        gems = json_object['board']['treasures']
        board_obj = []
        for row in range(len(board_strings)):
            board_obj.append([])
            for col in range(len(board_strings[row])):
                board_obj[row].append(Tile(board_strings[row][col],
                                           gems=[get_gem_by_string(gems[row][col][0]),
                                                 get_gem_by_string(gems[row][col][1])]))
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
        json_str = json_string.decode('utf-8')
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