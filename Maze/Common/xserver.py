import sys, os, json
from action import Move, Pass
from state import State
from tile import Tile
from board import Board
from gems import Gem
from player_state import Player
from coordinate import Coordinate

sys.path.append(os.path.join(os.path.dirname(__file__), "../Server"))
from server import Server

def xserver(in_stream):
    """
    Reads json objects from stdin representing the game state and requested testing parameters.
    Outputs to stdout the reachable tiles from that Maze board state from the given coordinate.
    """
    json_objects = read_input(in_stream)
    state = json_to_state(json_objects[0])
    s = Server('localhost', int(sys.argv[1]), state)
    return return_output(s.get_game_outcome())


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

def return_output(outcome):
    winners, kicked = outcome
    winner_names = [x.get_player_api().get_name() for x in winners]
    kicked_names = [x.get_player_api().get_name() for x in kicked]
    return json.dumps([sorted(winner_names), sorted(kicked_names)])

def json_to_state(json_state):
    board = json_to_board(json_state)
    spare_tile = Tile(json_state['spare']['tilekey'], \
        [Gem(json_state['spare']['1-image']), Gem(json_state['spare']['2-image'])])
    players = json_to_players(json_state, board)
    last_action = json_to_last_action(json_state['last'])
    s = State(players=players, board=board, extra_tile=spare_tile, last_action=last_action)
    return s


def json_to_board(json_object):
    board_connectors = json_object['board']['connectors']
    board_treasures = json_object['board']['treasures']
    board_obj = []
    for row in range(len(board_connectors)):
        board_obj.append([])
        for col in range(len(board_connectors[row])):
            board_obj[row].append(Tile(board_connectors[row][col], \
                [Gem(board_treasures[row][col][0]), Gem(board_treasures[row][col][1])]))
    return Board(board=board_obj)


def json_to_players(json_object, board):
    players_data = json_object['plmt']
    players = []
    board_data = board.get_board()
    for player_data in players_data:
        home = player_data['home']
        goal = player_data['goto']
        current = player_data['current']
        players.append(Player(player_data['color'],
                              board_data[home['row#']][home['column#']],
                              board_data[goal['row#']][goal['column#']],
                              board_data[current['row#']][current['column#']]))
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

print(xserver(sys.stdin.read()))