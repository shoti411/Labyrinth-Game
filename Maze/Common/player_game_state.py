import copy

class PlayerGameState:
    """ 
    This class is to represent the knowledge a Player is given about a game. 
    This breaks down to the board, extra tile and their own player information.
    """

    def __init__(self, board, extra_tile, player):
        """
        :param: board <Board>: Maze game scenario board
        :param: extra_tile <Tile>: extra tile of Maze game scenario
        :param: player <Player>: Active player of Maze game scenario
        """

        self.__board = board
        self.__extra_tile = extra_tile
        self.__player = player

    def get_board(self):
        return copy.deepcopy(self.__board)

    def get_extra_tile(self):
        return copy.deepcopy(self.__extra_tile)

    def get_player(self):
        return copy.deepcopy(self.__player)