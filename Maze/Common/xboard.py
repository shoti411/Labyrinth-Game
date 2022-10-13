import json
import sys
from board import Board
from tile import Tile


def xboard():
    collected_input = sys.stdin.read()

    json_objects = []
    j = 0
    for i in range(len(collected_input)):
        try:
            input_json = json.loads(collected_input[j:i])
            j = i
            json_objects.append(input_json)
        except json.decoder.JSONDecodeError:
            continue
    handle_json(json_objects)


def handle_json(json_objects):
    board_strings = (json_objects[0]['connectors'])
    board_obj = []
    for row in range(len(board_strings)):
        board_obj.append([])
        for col in range(len(board_strings[row])):
            board_obj[row].append(Tile(board_strings[row][col]))
    board = Board(board=board_obj)
    reachable = board.get_reachable_tiles(json_objects[1]['row#'], json_objects[1]['column#'])
    return_obj = []
    for reachable_tile in reachable:
        return_obj.append({'column#': reachable_tile[1], 'row#': reachable_tile[0]})
    print(json.dumps(return_obj))


if __name__ == '__main__':
    xboard()

