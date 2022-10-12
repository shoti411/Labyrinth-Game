from tile import Tile
from board import Board
from player import Player
from directions import Direction


class State:

    def __init__(self, players, board=None, extra_tile=None):
        # players is a list of players, s.t. players[0] is currently active.
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

    def rotate_extra_tile(self, degrees):
        self.extra_tile.rotate(degrees)

    def active_can_reach_tile(self, x, y):
        curr_x, curr_y = self.players[0].get_position()
        return (x, y) in self.board.get_reachable_tiles(curr_x, curr_y)

    def active_on_goal_tile(self):
        curr_x, curr_y = self.players[0].get_position()
        curr_tile = self.board.get_board()[curr_x][curr_y]
        goal_tile = self.players[0].get_goal()
        return curr_tile == goal_tile

    def kick_active(self):
        if len(self.players) > 1:
            self.players = self.players[1:]
        elif len(self.players) == 1:
            self.players = []

    def shift(self, index, direction, is_row):
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

