from tile import Tile
from board import Board
from player import Player
from directions import Direction


class State:
    """
    State is the representation of the game state of Maze game.
    
    This game state comprises three essential pieces of knowledge: 
        the current state of the board; the spare tile; and the players.
        
    State has the functionality to:
        rotate spare tiles.\n
        Shift rows or columns.\n
        check if the active player can reach a tile.\n
        check if the active player is a goal tile.\n
        Kick active player.
    """
    def __init__(self, players, board=False, extra_tile=False):
        """
        Constructs State. A State is built up of players, a board, and an extra_tile.

        :param: players <list(Player)>: players represents the list of players in the Maze game.
                                        This list also represents the order of moves in the game. 
                                            S.t players[0] represents the currently active player.
        :param: board <Board>: board is default False and will be a randomized board of 7x7.
        :param: extra_tile <Tile>: extra_tile is default False and will be a randomized Tile.
        """
        self.players = players
        self.extra_tile = extra_tile
        if not extra_tile:
            self.extra_tile = Tile()
        self.board = board
        if not board:
            self.board = Board()

        self.__check_valid_constructor()

    def __check_valid_constructor(self):
        if not isinstance(self.extra_tile, type(Tile())):
            raise ValueError('Spare tile must be of type Tile.')
        if not isinstance(self.board, Board):
            raise ValueError('Board must be of type Board.')
        if not all([isinstance(x, Player) for x in self.players]):
            raise ValueError('Players must be of type Player.')

    def get_players(self):
        return self.players

    def get_extra_tile(self):
        return self.extra_tile

    def move_active_player(self, x, y):
        """
        Moves the active player to the new location.

        :param: x (int): int representing the row location of the move.
        :param: y (int): int representing the col location of the move.
        """
        if self.active_can_reach_tile(x,y):
            self.players[0].set_position(x,y)
        else:
            raise ValueError('The given move is unreachable or unvalid.')

    def rotate_extra_tile(self, degrees):
        """
        Rotates the tile based on a given number of degrees
        
        :param: degrees (int): degrees is an int that represents the number of degrees to rotate by. 
                               degrees can be positive or negative but must be a multiple of 90.
        """
        self.extra_tile.rotate(degrees)

    def active_can_reach_tile(self, x, y):
        """
        Checks if the Tile on board at coordinates x and y is reachable from the active player.
        If given an invalid location this will return False as the player is not at that location.

        :param: x <int>: x represents the row coordinate of the board. 0 represents the top row.
        :param: y <int>: y represents the column coordiante of the board. 0 represents the left row.
        
        :return: <bool>: True or False depending on if the player can reach the Tile.
        """
        curr_x, curr_y = self.players[0].get_position()
        return (x, y) in self.board.get_reachable_tiles(curr_x, curr_y)

    def active_on_goal_tile(self):
        """
        Check if the active players position is at a goal tile.

        :return: <bool>: True or False depending on if the players position is at a goal tile.
        """
        curr_x, curr_y = self.players[0].get_position()
        curr_tile = self.board.get_board()[curr_x][curr_y]
        goal_treasure = self.players[0].get_goal()
        print(curr_tile.get_gems())
        return goal_treasure in curr_tile.get_gems()

    def kick_active(self):
        """
        Kicks active player from the game.
        """
        if len(self.players) > 1:
            self.players = self.players[1:]
        elif len(self.players) == 1:
            self.players = []

    def shift(self, index, direction, is_row):
        """
        Shifts a given moveable row or column in a given direction. 
        Knocking off the Tile at the end of the shifted direction and making it the extra tile. 
        The old extra tile will be inserted at the start of the shifted direction.

        A players position will move with a shifted Tile. If a player is on the new extra tile, move it to the old extra tile.

        :param: index <int>: index of the row or column to be shifted. index must be an even number.
        :param: direction <int>: direction represents whether it is being shifted forward or backward.\n
                                 direction can be either 1 or -1.\n
                                 1 represents we are shifting forward. row shifts to the right, column shifts down.\n
                                 -1 represents we are shifting backwards. row shifts to the left, column shifts up.
        :param: is_row <bool>: True or False depending on if the index is for a row or column.
        """
        if not isinstance(is_row, bool):
            raise ValueError('is_row must be a boolean value.')

        if is_row:
            self.extra_tile = self.board.shift_row(index, direction, self.get_extra_tile())
        else:
            self.extra_tile = self.board.shift_column(index, direction, self.get_extra_tile())

        for player in self.players:

            if player.get_position()[0] == index and is_row:
                new_y = int((player.get_position()[1] + direction) % len(self.board.get_board()[index]))
                player.set_position(player.get_position()[0], new_y)

            elif player.get_position()[1] == index and not is_row:
                new_x = int((player.get_position()[0] + direction) % len(self.board.get_board()))
                player.set_position(new_x, player.get_position()[1])

