from tile import Tile


class Player:

    def __init__(self, avatar, home, goal, position):
        self.__avatar = avatar
        self.__home = home
        self.__goal = goal
        self.__position = position

        self.__check_constructor()

    def __check_constructor(self):
        if not isinstance(self.__home, type(Tile())):
            raise ValueError('Home must be of type Tile')
        if not isinstance(self.__goal, type(Tile())):
            raise ValueError('Goal must be of type Tile')
        if not(len(self.__position) == 2
               and isinstance(self.__position[0], int)
               and isinstance(self.__position[1], int)):
            raise ValueError('Position must be an array of length 2 with integer values.')

    def get_avatar(self):
        return self.__avatar

    def get_home(self):
        return self.__home

    def get_goal(self):
        return self.__goal

    def get_position(self):
        return self.__position

    def set_position(self, x, y):
        self.__position = (x, y)
