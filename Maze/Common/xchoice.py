import json
import sys
from riemann import Riemann
from euclid import Euclid
from board import Board
from tile import Tile
from state import State
from player import Player


def xchoice():
    """
    Reads json objects from stdin representing the game state and requested testing parameters.
    Outputs to stdout the reachable tiles from that Maze board state from the given coordinate.
    """
    json_objects = read_input()
    turn_data = handle_json(json_objects)
    return_output(turn_data)


def read_input():
    """
    Reads input from stdin, parses well-formed and valid json objects.

    :return: <list of Json Objects>
    """

    json_str = sys.stdin.read()
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
    if turn_data == "PASS":
        print(json.dumps("PASS"))
        return
    index, direction_integer, degree, is_row, x, y = turn_data
    direction = get_direction(is_row, direction_integer)
    coordinate = position_to_object(x, y)
    print(json.dumps([index, direction, degree, coordinate]))


def position_to_object(x, y):
    return {"row#": x, "column#": y}


def handle_json(json_objects):
    board = json_to_board(json_objects[1])
    spare_tile = Tile(json_objects[1]['spare']['tilekey'])
    players = json_to_players(json_objects[1], board)

    state = State(players, board, spare_tile)
    strategy = select_strategy(json_objects[0])
    x_coord, y_coord = (json_objects[2]['row#'], json_objects[2]['column#'])

    slide_and_insert = strategy.slide_and_insert(board, spare_tile, players[0])
    if slide_and_insert == -1:
        return "PASS"
    degree, direction_integer, index, is_row = slide_and_insert
    x, y = strategy.move(board, players[0])
    return index, direction_integer, degree, is_row, x, y


def get_direction(is_row, direction):
    if is_row and direction == 1:
        return "RIGHT"
    elif is_row:
        return "LEFT"
    elif direction == 1:
        return "DOWN"
    return "UP"


def select_strategy(strategy):
    strategy_map = {
        "Euclid": Euclid(),
        "Riemann": Riemann()
    }
    return strategy_map[strategy]


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
        players.append(Player('',
                              board_data[home['row#']][home['column#']],
                              board_data[home['row#']][home['column#']],
                              [home['row#'], home['column#']]))
    return players


if __name__ == "__main__":
    xchoice()