from tile import Tile
from board import Board
from player import Player
import copy 


class Strategy:
    def slide_and_insert(self, board, extra_tile, player):
        raise NotImplemented('slide_and_insert not implemented.')

    def move(self, board, extra_tile, player):
        raise NotImplemented('move not implemented.')

    def check_state(self, board, extra_tile, player):
        if not isinstance(board, Board):
            raise ValueError('Given board must be of type board.')
        if not isinstance(extra_tile, Tile):
            raise ValueError('extra_tile must be of type Tile.')
        if not isinstance(player, Player):
            raise ValueError('player must be of type Player.')

        


class Riemann(Strategy):

    def slide_and_insert(self, board, extra_tile, player):
        self.check_state(board, extra_tile, player)

        tiles = board.get_board()
        for row in tiles:
            for tile in row:
                try:
                    for i in len(tiles):
                        for degree in [0, 90, 180, 270]:
                            test_board = copy.deepcopy(board)
                            test_board.shift_row(i, 1, extra_tile.rotate(degree))
                            x, y = player.get_position()
                            reachable = test_board.get_reachable_tiles(x, y)
                            if any([player.get_goal() in test_board.get_board()[x[0]][x[1]].get_gems() for x in reachable]):
                                return i, 1, True, degree 
                    ...
                except IndexError as e:
                    ...





    def __check_configurations(self, tiles, extra_tile, player):
        for row in tiles:
            for tile in row:
                

    # check configuration
        # for all tiles
            # check slide_insert

    # checks scenario
        # can reach

    # can reach

    # board.getboard()
        # for i 
            # for j
                # for r
                    # left right
                        # for rotation
                            # goal tile ?
                            # i,j tile?
                # for c 
                    # up down
                        # for rotation
                            # goal tile ?
                            # i,j tile?

        # list of possible goal tiles
            # enumeration of row-column order: starting from top-left
        # try all slides from each enumeration
            # start from all rows from left to right then columns from up to down.
        # for each slide try all possible rotation of the extra tile

        # loop through each enumeration 
            # all slides 
                # all rotations
                    # check if goal tile is reachable
                    # check if enumeration tile is reachable
                    # if so then stop and move to reachable

    def move(self, board, extra_tile, player):
        ...

        # if we can reach goal tile then do that

        


#class Euclid(Strategy):


if __name__ == '__main__':
    ...