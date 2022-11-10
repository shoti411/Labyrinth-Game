import json
import sys
from riemann import Riemann
from euclid import Euclid
from board import Board
from tile import Tile
from player_state import Player
from coordinate import Coordinate
from action import Move, Pass
from state import State
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../Players"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../Referee"))
from player import PlayerAPI, BadPlayerAPI
from referee import Referee


def xgame(in_stream):
    """
    Reads json objects from stdin representing the game state and requested testing parameters.
    Outputs to stdout the reachable tiles from that Maze board state from the given coordinate.
    """
    json_objects = read_input(in_stream)
    turn_data = handle_json(json_objects)
    return return_output(turn_data)


def read_input(json_str):
    """
    Reads input from json_str, parses well-formed and valid json objects.

    :return: <list of Json Objects>
    """
    decoder = json.JSONDecoder()
    pos = 0
    objs = []
    while pos < len(json_str):
        json_str = json_str[pos:].strip()
        if not json_str:
            break
        obj, pos = decoder.raw_decode(json_str)
        objs.append(obj)
    return objs


def return_output(turn_data):
    ref = Referee()
    winners, kicked = ref.pickup_from_state(state=turn_data)
    winner_names = [x.get_player_api().get_name() for x in winners]
    kicked_names = [x.get_player_api().get_name() for x in kicked]
    return json.dumps([sorted(winner_names), sorted(kicked_names)])

def get_strategy(strategy_string):
    if strategy_string == 'Riemann':
        return Riemann()
    elif strategy_string == 'Euclid':
        return Euclid
    raise ValueError(f'No such strategy: {strategy_string}')

def handle_json(json_objects):
    board = json_to_board(json_objects[1])
    spare_tile = Tile(json_objects[1]['spare']['tilekey'])
    players = json_to_players(json_objects[1], board)

    for i in range(len(players)):
        player_api = PlayerAPI(json_objects[0][i][0], json_objects[0][i][1])
        if len(json_objects[0][i]) == 3:
            player_api = BadPlayerAPI(json_objects[0][i][0], json_objects[0][i][2], json_objects[0][i][1])
        players[i].set_player_api(player_api)

    last_action = json_to_last_action(json_objects[1]['last'])
    if last_action is None:
        last_action = False
    s = State(players, board, extra_tile=spare_tile, last_action=last_action)
    return s

def position_to_object(x, y):
    return {"row#": x, "column#": y}


def json_to_board(json_object):
    board_strings = (json_object['board']['connectors'])
    board_obj = []
    for row in range(len(board_strings)):
        board_obj.append([])
        for col in range(len(board_strings[row])):
            board_obj[row].append(Tile(board_strings[row][col]))
    return Board(board=board_obj)


def json_to_players(json_object, board):
    players_data = json_object['plmt']
    players = []
    board_data = board.get_board()
    for player_data in players_data:
        home = player_data['home']
        goal = player_data['goto']
        players.append(Player(player_data['color'],
                              board_data[home['row#']][home['column#']],
                              board_data[goal['row#']][goal['column#']],
                              Coordinate(home['row#'], home['column#'])))
    return players

def json_to_last_action(json_object):
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


if __name__ == "__main__":
    print(xgame(sys.stdin.read()))

    """
    for i in range(3):
        file_name = f'./Tests/ForStudents/{i}-in.json'
        f = open(file_name, 'r', encoding='utf-8')
        print(xgame(f.read()))
        continue
        f_out = open(f'./Tests/{i}-out.json', 'w')
        f_out.write(xgame(f.read()))
        f_out.close()
        f.close()
    """