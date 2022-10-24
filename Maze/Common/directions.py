from enum import Enum
from re import X

class Direction(Enum):
    """
    Represents the path connections of a Tile.
    """

    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
