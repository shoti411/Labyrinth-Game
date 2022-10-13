import copy
import random

from directions import Direction

class Tile:
    """ 
    Represents a tile in a board game with possible paths to UP, DOWN, LEFT, and/or RIGHT."""

    __acceptable_paths = ['│', '─', '┐', '└', '┌', '┘', '┬', '├', '┴', '┤', '┼']
    __rotation_mapping = [['│', '─'], ['┐', '┌', '└', '┘'], ['┬', '├', '┴', '┤'], ['┼']]

    def __init__(self, path_code=False):
        """
        Constructs a Tile. By default, path_code False and is random.

        :param: path_code (string): A acceptable string.
            A string is acceptable if it is one of ['│', '─', '┐', '└', '┌', '┘', '┬', '├', '┴', '┤', '┼'].
        """

        if not path_code:
            path_code = random.choice(self.__acceptable_paths)
        if path_code not in self.__acceptable_paths:
            raise ValueError(f'Given path_code must be in: {self.__acceptable_paths}')
        self.__path_code = path_code

    def get_path_code(self):
        return copy.deepcopy(self.__path_code)

    def get_paths(self):
        """
        Converts and returns the path_code as a list of Direction.

        :return: directions (list(Direction)): Paths from this tile.
        """

        directions = []
        if self.__path_code in ['│', '└', '┘', '├', '┴', '┤', '┼']:
            directions.append(Direction.UP)
        if self.__path_code in ['│', '┐', '┌', '┬', '├',  '┤', '┼']:
            directions.append(Direction.DOWN)
        if self.__path_code in ['─', '┐', '┘', '┬', '┴', '┤', '┼']:
            directions.append(Direction.LEFT)
        if self.__path_code in ['─',  '└', '┌', '┬', '├', '┴',  '┼']:
            directions.append(Direction.RIGHT)
        return directions

    def rotate(self, degrees):
        """ Rotates the tile based on a given number of degrees
        
        :param: degrees (int): degrees is an int that represents the number of degrees to rotate by. 
                               degrees can be positive or negative but must be a multiple of 90.
        """
        if degrees % 90 != 0:
            raise ValueError('Degrees must be a multiple of 90.')
        degrees = degrees % 360
        rotation_steps = int(degrees / 90)
        for rotation_map in self.__rotation_mapping:
            if self.get_path_code() in rotation_map:
                index = rotation_map.index(self.get_path_code())
                self.__path_code = rotation_map[(index + rotation_steps) % len(rotation_map)]

    def __str__(self):
        return self.__path_code

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.get_path_code() == self.__path_code
