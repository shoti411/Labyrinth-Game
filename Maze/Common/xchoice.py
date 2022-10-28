import json
import sys
from riemann import Riemann
from euclid import Euclid
from board import Board
from tile import Tile
from player_game_state import PlayerGameState
from player_state import Player
from coordinate import Coordinate
from action import Move, Pass

def xchoice(in_stream):
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
    if turn_data == "PASS":
        print(json.dumps("PASS"))
        return
    index, direction_integer, degree, is_row, x, y = turn_data
    direction = get_direction(is_row, direction_integer)
    coordinate = position_to_object(x, y)
    return json.dumps([index, direction, degree, coordinate])


def position_to_object(x, y):
    return {"row#": x, "column#": y}


def handle_json(json_objects):
    board = json_to_board(json_objects[1])
    spare_tile = Tile(json_objects[1]['spare']['tilekey'])
    players = json_to_players(json_objects[1], board)
    last_action = json_to_last_action(json_objects[1]['last'])

    state = PlayerGameState(board, spare_tile, players[0], last_action)
    strategy = select_strategy(json_objects[0])
    x_coord, y_coord = (json_objects[2]['row#'], json_objects[2]['column#'])
    players[0].set_coordinate(Coordinate(x_coord, y_coord))

    move = strategy.evaluate_move(state)
    if move.is_pass():
        return "PASS"
    degrees, direction_integer, index, is_row, coordinate = move.get_move()
    x, y = coordinate.getX(), coordinate.getY()
    return index, direction_integer, degrees, is_row, x, y


def get_direction(is_row, direction):
    if is_row and direction == 1:
        return "RIGHT"
    elif is_row:
        return "LEFT"
    elif direction == 1:
        return "DOWN"
    return "UP"


def select_strategy(strategy):
    # TODO: fix this
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
                              Coordinate(home['row#'], home['column#'])))
    return players

def json_to_last_action(json_object) :
    if not json_object:
        return Pass()
    index = json_object[0]
    if json_object[1] is "LEFT":
        is_row = True
        direction = -1
    elif json_object[1] is "RIGHT":
        is_row = True
        direction = 1
    elif json_object[1] is "UP":
        is_row = False
        direction = -1
    elif json_object[1] is "DOWN":
        is_row = False
        direction = 1
    else:
        raise ValueError("BAD JSON")
    return Move(0, direction, index, is_row, Coordinate(0,0))



if __name__ == "__main__":
    print(xchoice(sys.stdin.read()))
    """
    for i in range(5):
        file_name = f'./Tests/{i}-in.json'
        f = open(file_name, 'r', encoding='utf-8')
        f_out = open(f'./Tests/{i}-out.json', 'w')
        f_out.write(xchoice(f.read()))
        f_out.close()
        f.close()
    """
