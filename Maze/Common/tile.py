import copy
import random


class Tile:
    """ Represents a tile in a board game with possible paths to UP, DOWN, LEFT, and RIGHT """

    __acceptable_paths = ['│', '─', '┐', '└', '┌', '┘', '┬', '├', '┴', '┤', '┼']

    def __init__(self, path_code=None):
        if path_code is None:
            path_code = random.choice(self.__acceptable_paths)
        if path_code not in self.__acceptable_paths:
            raise ValueError(f'Given path_code must be in: {self.__acceptable_paths}')
        self.__path_code = path_code

    def get_path_code(self):
        return copy.deepcopy(self.__path_code)

    def get_paths(self):
        directions = []
        ['│', '─', '┐', '└', '┌', '┘', '┬', '├', '┴', '┤', '┼']
        if self.__path_code in ['│', '└','┘', '├', '┴', '┤', '┼']:
            directions.append('UP')
        if self.__path_code in ['│', '┐', '┌', '┬', '├',  '┤', '┼']:
            directions.append('DOWN')
        if self.__path_code in ['─', '┐', '┘', '┬', '┴', '┤', '┼']:
            directions.append('LEFT')
        if self.__path_code in ['─',  '└', '┌', '┬', '├', '┴',  '┼']:
            directions.append('RIGHT')
        return directions

    def __str__(self):
        return self.__path_code

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.get_path_code() == self.__path_code
