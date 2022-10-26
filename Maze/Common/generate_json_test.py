from state import State
from board import Board
from tile import Tile
from player_state import Player
import json
import random

def board_to_json(board):
    assert isinstance(board, Board)
    connectors = []
    treasures = []
    board_obj = board.get_board()
    for row in range(len(board_obj)):
        connectors.append([])
        treasures.append([])
        for col in range(len(board_obj[row])):
            connectors[row].append(board_obj[row][col].get_path_code())
            treasures[row].append([g.value for g in board_obj[row][col].get_gems()])
    return {'connectors': connectors, 'treasures': treasures}


def tile_to_json(tile):
    assert isinstance(tile, Tile)
    return {'tilekey': tile.get_path_code()}


def player_to_json(player, board):
    assert isinstance(player, Player)
    player_data = {}
    x, y = player.get_position()
    player_data['current'] = {'row#': x, 'column#': y}
    h_x, h_y = board.find_tile_position_by_tile(player.get_home())
    player_data['home'] = {'row#': h_x, 'column#': h_y}
    return player_data


def state_to_json(state):
    assert isinstance(state, State)
    state_json = {
        'board': board_to_json(state.get_board()),
        'spare': tile_to_json(state.get_extra_tile()),
        'plmt': [player_to_json(p, state.get_board()) for p in state.get_players()],
        'last': None
    }
    return state_json


def format_xstate_test_case(s, index, direction, degree):
    json_string = ''
    json_string += json.dumps(state_to_json(s), ensure_ascii=False) + '\n'
    json_string += json.dumps(index) + '\n'
    json_string += json.dumps(direction) + '\n'
    json_string += json.dumps(degree) + '\n'
    return json_string


def format_xchoice_test_case(s, strategy, x, y):
    json_string = ''
    json_string += json.dumps(strategy) + "\n"
    json_string += json.dumps(state_to_json(s), ensure_ascii=False) + '\n'
    json_string += json.dumps(format_coordinate(x, y)) + '\n'
    return json_string


def format_coordinate(x, y):
    return {"row#": x, "column#": y}


def make_tests(amount, fp):
    for i in range(amount):
        test_board = [[Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
                      [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
                      [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
                      [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
                      [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
                      [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
                      [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()]]
        b = Board(board=test_board)
        p = Player('', b.get_board()[random.choice(range(7))][random.choice(range(7))],
                   b.get_board()[random.choice(range(7))][random.choice(range(7))],
                   (random.choice(range(7)), random.choice(range(7))))
        s = State([p], b, Tile())
        test_case = format_xchoice_test_case(s,
                                             random.choice(["Euclid", "Riemann"]),
                                             random.randint(0, len(test_board)),
                                             random.randint(0, len(test_board)))
        file = open(f'{fp}/{i}-in.json', 'w', encoding='utf-8')
        file.write(test_case)
        file.close()



make_tests(5, './Tests')
