import json
import sys
from board import Board
from tile import Tile


def xboard():
    """
    Reads json objects from stdin representing Maze board state and coordinate input for reachable tile. 
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
    return json_objects

def handle_json(json_objects):
    """
    Parses json objects into our data representation of a Maze Board and input for checking reachable tiles from given coordinates.

    :param: json_objects <list of Json Objects>: List of well-formed and valid json objects.

    :return: <list(tuple(int, int))>: List of coordinates of x,y represents the row and column of reachable tiles.
    """

    board_strings = (json_objects[0]['connectors'])
    board_obj = []
    for row in range(len(board_strings)):
        board_obj.append([])
        for col in range(len(board_strings[row])):
            board_obj[row].append(Tile(board_strings[row][col]))
    board = Board(board=board_obj)
    return board.get_reachable_tiles(json_objects[1]['row#'], json_objects[1]['column#'])
    

def return_output(reachable):
    """
    Converts list of tuple(int,int) into Coordinate objects to be dumped to stdout.
    """

    return_obj = []
    for reachable_tile in reachable:
        return_obj.append({'column#': reachable_tile[1], 'row#': reachable_tile[0]})
    print(json.dumps(return_obj))

if __name__ == '__main__':
    xboard()

