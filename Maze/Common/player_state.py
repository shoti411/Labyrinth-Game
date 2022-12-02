from gems import Gem
from tile import Tile
from coordinate import Coordinate
import sys
import os
import random
import re
import copy

class Player:
    """
    Player is a representation of a player from Maze game.
    """

    __acceptable_colors = ["purple", "orange", "pink", "red", "blue", "green", "yellow", "white", "black"]

    def __init__(self, avatar, home, goal, coordinate, player_api=False):
        """
        Constructs a Player. A Player is made up of an avatar, home tile, goal treasure, and a position.
        
        :param: avatar <string>: String that represents the color of the player.
        :param: home <Tile>: home represents the home tile of the player.
        :param: goal <Tile>: goal represents the target tile of the player.
        :param: coordinate  <Coordinate>: Coordinate of player
        :param: has_reached_goal <bool>: If the player has reached their goal Tile before
        """
        # TODO: check avatar is a valid color, if not, randomize.
        self.__avatar = self.__assign_color(avatar)
        self.__home = home
        self.__goal = goal
        self.__coordinate = coordinate
        self.__num_goals_reached = 0
        self.__player_api = player_api

        self.__check_constructor()

    def get_player_copy(self):
        return Player(copy.deepcopy(self.__avatar),
                      copy.deepcopy(self.__home),
                      copy.deepcopy(self.__goal),
                      copy.deepcopy(self.__coordinate),
                      copy.deepcopy(self.__has_reached_goal),
                      False)

    def __assign_color(self, color):
        if color in self.__acceptable_colors:
            return color
        if not color:
            return "#" + "%06x" % random.randint(0, 0xFFFFFF)
        color = color.upper()
        pattern = re.compile("^[A-F|\d][A-F|\d][A-F|\d][A-F|\d][A-F|\d][A-F|\d]$")
        if pattern.match(color):
            return "#" + color
        else:
            return "#" + "%06x" % random.randint(0, 0xFFFFFF)

    def __check_constructor(self):
        if not isinstance(self.__home, type(Tile())):
            raise ValueError('Home must be of type Tile')
        if not isinstance(self.__goal, type(Tile())):
            raise ValueError('Goal must be of type Tile')
        if not (isinstance(self.__coordinate, Coordinate)):
            raise ValueError('coordinate must be a Coordinate')
        # if not(isinstance(self.__player_api, PlayerAPI)) and not(isinstance(self.__player_api, bool)):
        #    raise ValueError('player_api must be False or type PlayerAPI')

    def get_avatar(self):
        return self.__avatar

    def get_home(self):
        return self.__home

    def get_goal(self):
        return self.__goal

    def set_goal(self, goal):
        if not isinstance(goal, type(Tile())):
            raise ValueError('Goal must be of type Tile')

        self.__goal = goal

    def get_coordinate(self):
        return self.__coordinate

    def get_player_api(self):
        if not self.__player_api:
            raise NotImplemented("This Player does not have a player api")
        return self.__player_api

    def set_player_api(self, player_api):
        # assert isinstance(player_api, PlayerAPI), 'Must be instance of PlayerAPI'
        self.__player_api = player_api

    def set_coordinate(self, coordinate):
        self.__coordinate = coordinate

    def get_num_goals_reached(self):
        return self.__num_goals_reached

    def reached_goal(self):
        self.__num_goals_reached += 1

