from tile import Tile
from board import Board
from player import Player


class Strategy:
    def slide_and_insert(self, board, extra_tile, player):
        raise NotImplemented('slide_and_insert not implemented.')

    def move(self, board, extra_tile, player):
        raise NotImplemented('move not implemented.')

    def check_state(self, board, player, extra_tile=False):
        if not isinstance(board, Board):
            raise ValueError('Given board must be of type board.')
        if not (isinstance(extra_tile, Tile) or (not extra_tile)):
            raise ValueError('extra_tile must be of type Tile.')
        if not isinstance(player, Player):
            raise ValueError('player must be of type Player.')



                

    


class Euclid(Strategy):
    def slide_and_insert(self, board, extra_tile, player):
        raise NotImplemented('slide_and_insert not implemented.')

    def move(self, board, extra_tile, player):
        raise NotImplemented('move not implemented.')
