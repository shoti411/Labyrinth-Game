from state import State
from board import Board
from tile import Tile
from player_state import Player
import json
import random
from coordinate import Coordinate
import string
from gems import Gem
import itertools

strategies = ['Riemann', 'Euclid']


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
    gems = tile.get_gems()
    return {'1-image': gems[0].value, '2-image': gems[1].value, 'tilekey': tile.get_path_code()}


def player_to_json(player, board, referee_player=False):
    assert isinstance(player, Player)
    player_data = {}
    coords = player.get_coordinate()
    x = coords.getX()
    y = coords.getY()
    player_data['color'] = ("%06x" % random.randint(0, 0xFFFFFF)).upper()
    player_data['current'] = format_coordinate(x, y)

    if referee_player:
        goal_coords = board.find_tile_coordinate_by_tile(player.get_goal())
        player_data['goto'] = format_coordinate(goal_coords.getX(),  goal_coords.getY())
    home_coords = board.find_tile_coordinate_by_tile(player.get_home())
    player_data['home'] = format_coordinate(home_coords.getX(), home_coords.getY())
    return player_data


def last_action_to_json(state):
    last_action = state.get_last_action()
    if not last_action or last_action.is_pass():
        return None
    direction_int = last_action.get_direction()
    if last_action.get_isrow():
        direction = 'LEFT' if direction_int == -1 else 'RIGHT'
    else:
        direction = 'UP' if direction_int == -1 else 'DOWN'
    last_action = [last_action.get_index(), direction]
    return last_action


def state_to_json(state, referee_state=False):
    assert isinstance(state, State)
    # TODO: randomize last move?
    state_json = {
        'board': board_to_json(state.get_board()),
        'last': last_action_to_json(state),
        'plmt': [player_to_json(p, state.get_board(), referee_player=referee_state) for p in state.get_players()],
        'spare': tile_to_json(state.get_extra_tile())
    }
    return state_json


def format_xstate_test_case(s, index, direction, degree):
    json_string = ''
    json_string += json.dumps(state_to_json(s), ensure_ascii=False) + '\n'
    json_string += json.dumps(index) + '\n'
    json_string += json.dumps(direction) + '\n'
    json_string += json.dumps(degree) + '\n'
    return json_string


def format_coordinate(x, y):
    return {"column#": y, "row#": x}


def random_player_spec():
    name_characters = string.ascii_letters + string.digits
    name = "".join(random.choices(name_characters, k=random.randint(1, 20)))
    return [name, random.choice(strategies)]


def random_player_spec_json(amount):
    player_spec = []
    for i in range(amount):
        player_spec.append(random_player_spec())
    return json.dumps(player_spec)


def format_xchoice_test_case(s, strategy, x, y, referee_state=False):
    json_string = ''
    json_string += json.dumps(strategy) + "\n"
    json_string += json.dumps(state_to_json(s), ensure_ascii=False) + '\n'
    json_string += json.dumps(format_coordinate(x, y)) + '\n'
    return json_string


def format_xgame_test_case(s):
    assert isinstance(s, State)
    json_string = ''
    num_players = len(s.get_players())
    json_string += random_player_spec_json(num_players) + '\n'
    json_string += json.dumps(state_to_json(s, True)) + '\n'
    return json_string


def make_tests(amount, num_players=4, fp=None):
    for i in range(amount):
        test_board = []
        gems = [x for x in Gem]
        all_gem_combos = []
        for subset in itertools.combinations(gems, 2):
            all_gem_combos.append(subset)

        for rows in range(7):
            test_board.append([])
            for cols in range(7):
                gems = random.choice(all_gem_combos)
                test_board[rows].append(Tile(gems=gems))
                all_gem_combos.remove(gems)

        b = Board(board=test_board)
        players = []
        selectable_indexes = [1, 3, 5]
        valid_posns = list(itertools.combinations(selectable_indexes + selectable_indexes, 2))
        for player in range(num_players):
            home = random.choice(valid_posns)
            valid_posns.remove(home)
            goal = random.choice(valid_posns)
            valid_posns.remove(goal)
            p = Player('', b.get_board()[home[0]][home[1]],
                       b.get_board()[goal[0]][goal[1]],
                       Coordinate(home[0], home[1]))
            players.append(p)
        s = State(players, b, Tile())
        test_case = format_xgame_test_case(s)

        if fp is not None:
            file = open(f'{fp}/{i}-in.json', 'w', encoding='utf-8')
            file.write(test_case)
            file.close()
        else:
            print(test_case)


make_tests(1, fp='./Tests')
