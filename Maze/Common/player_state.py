from gems import Gem
from tile import Tile
from coordinate import Coordinate

class Player:
    """
    Player is a representation of a player from Maze game.
    """

    def __init__(self, avatar, home, goal, coordinate):
        """
        Constructs a Player. A Player is made up of an avatar, home tile, goal treasure, and a position.
        
        :param: avatar <string>: String that represents the avatar of the player. 
        :param: home <Tile>: home represents the home tile of the player.
        :param: goal <Tile>: goal represents the target tile of the player.
        :param: coordinate  <Coordinate>: Coordinate of player
        """
        self.__avatar = avatar
        self.__home = home
        self.__goal = goal
        self.__coordinate = coordinate

        self.__check_constructor()

    def __check_constructor(self):
        if not isinstance(self.__home, type(Tile())):
            raise ValueError('Home must be of type Tile')
        if not isinstance(self.__goal, type(Tile())):
            raise ValueError('Goal must be of type Gem')
        if not(isinstance(self.__coordinate, Coordinate)):
            raise ValueError('coordinate must be an array of length 2 with integer values.')

    def get_avatar(self):
        return self.__avatar

    def get_home(self):
        return self.__home

    def get_goal(self):
        return self.__goal

    def get_coordinate(self):
        return self.__coordinate

    def set_coordinate(self, coordinate):
        self.__coordinate = coordinate
