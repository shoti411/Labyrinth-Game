import json
import sys
from board import Board
from tile import Tile
from state import State
from player_state import Player


def xstate():
    """
    Reads json objects from stdin representing the game state and requested testing parameters.
    Outputs to stdout the reachable tiles from that Maze board state from the given coordinate.
    """
    json_objects = read_input()
    reachable = handle_json(json_objects)
    return_output(reachable)


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


def handle_json(json_objects):
    """
    Parses json objects into our data representation of a Maze State. Uses parameters (degree rotation, spare tile,
    and index, and direction) to make a 'shift' move and then read the reachable tiles.

    :param: json_objects <list of Json Objects>: List of well-formed and valid json objects.

    :return: <list(tuple(int, int))>: List of coordinates of x,y represents the row and column of reachable tiles.
    """
    board = json_to_board(json_objects)
    spare_tile = Tile(json_objects[0]['spare']['tilekey'])
    players = json_to_players(json_objects, board)
    state = State(players, board, spare_tile)
    index, direction, is_row, degree = json_to_move_parameters(json_objects)

    state.rotate_extra_tile(degree)
    state.shift(index, direction, is_row)
    x, y = state.get_players()[0].get_position()
    return sort_reachable(board.get_reachable_tiles(x, y))


def json_to_board(json_objects):
    board_strings = (json_objects[0]['board']['connectors'])
    board_obj = []
    for row in range(len(board_strings)):
        board_obj.append([])
        for col in range(len(board_strings[row])):
            board_obj[row].append(Tile(board_strings[row][col]))
    return Board(board=board_obj)


def json_to_players(json_objects, board):
    players_data = json_objects[0]['plmt']
    players = []
    board_data = board.get_board()
    for player_data in players_data:
        home = player_data['home']
        players.append(Player('',
                              board_data[home['row#']][home['column#']],
                              board_data[home['row#']][home['column#']],
                              [home['row#'], home['column#']]))
    return players


def json_to_move_parameters(json_objects):
    index = json_objects[1]
    direction = 1 if json_objects[2] in ["DOWN", "RIGHT"] else -1
    is_row = json_objects[2] in ['LEFT', 'RIGHT']
    degree = json_objects[3]
    return index, direction, is_row, degree


def sort_reachable(positions):
    return sorted(positions, key=lambda x: (x[0], x[1]))


def return_output(reachable):
    """
    Converts list of tuple(int,int) into Coordinate objects to be dumped to stdout.
    """
    return_obj = []
    for reachable_tile in reachable:
        return_obj.append({'column#': reachable_tile[1], 'row#': reachable_tile[0]})
    print(json.dumps(return_obj))


if __name__ == '__main__':
    xstate()

