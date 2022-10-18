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

    DEGREES = [0, 90, 180, 270]
    DIRECTIONS = [-1, 1]

    def check_col_shift(self, target_x, target_y, player, board, extra_tile):
        for col_index in len(board.get_board()[0]):
            re = self.check_direction(target_x, target_y, player, board, extra_tile, col_index, False)
            if re != -1:
                degree, direction = re
                return degree, direction, col_index, False
        return -1

    def check_row_shift(self, target_x, target_y, player, board, extra_tile):
        for row_index in len(board.get_board()):
            re = self.check_direction(target_x, target_y, player, board, extra_tile, row_index, True)
            if re != -1:
                degree, direction = re
                return degree, direction, row_index, True
        return -1
    
    def check_direction(self, target_x, target_y, player, board, extra_tile, index, isrow):
        x, y = player.get_position()
        for direction in self.DIRECTIONS:
            degree = self.check_degrees(target_x, target_y, player, board, extra_tile, index, direction, isrow)
            if degree != -1:
                return degree, direction
        return -1

    def check_degrees(self, target_x, target_y, player, board, extra_tile, index, direction, isrow):
        for degree in self.DEGREES:
            board_copy = copy.deepcopy(board)
            tile_copy = copy.deepcopy(extra_tile)
            if isrow:
                board_copy.shift_row(index, direction, tile_copy.rotate(degree))
            else:
                board_copy.shift_col(index, direction, tile_copy.rotate(degree))
            x, y = player.get_position()
            reachable = board_copy.get_reachable_tiles(x, y)
            if target_x == -1 and target_y == -1:
                target_x, target_y = board.find_tile_position_by_tile(tile_copy) 
            if (target_x, target_y) in reachable:
                return degree
        return -1
            
    def check_goal_reachable(self, board, extra_tile, player):
        goal_position = board.find_tile_position_by_tile(player.get_goal())
        target_x, target_y = -1, -1 # TODO define -1, -1
        if goal_position != -1:
            target_x, target_y = goal_position

        re = self.check_row_shift(target_x, target_y, player, board, extra_tile)
        if re == -1:
            return self.check_col_shift(target_x, target_y, player, board, extra_tile)
        return re

    def check_alternative_reachables(self, board, extra_tile, player):
        for r in range(len(board)):
            for c in range(len(board[r])):
                re = self.check_row_shift(r, c, player, board, extra_tile)
                if re == -1:
                    re = self.check_col_shift(r, c, player, board, extra_tile)
                if re != -1:
                    return re
        return -1


    def slide_and_insert(self, board, extra_tile, player):
        self.check_state(board, extra_tile, player)

        re = self.check_goal_reachable(board, extra_tile, player)
        if re == -1:
            return self.check_alternative_reachables(board, extra_tile, player)
        return re

    def check_move_goal_reachable(board, extra_tile, player):
        x, y = player.get_position()
        goal_x, goal_y = board.find_tile_position_by_tile(player.get_goal())
        reachable = board.get_reachable_tiles(x, y)
        if (goal_x, goal_y) in reachable:
            return goal_x, goal_y
        return -1

    def check_move_goal_reachable(board, extra_tile, player):
        x, y = player.get_position()
        reachable = board.get_reachable_tiles(x, y)
        for r in range(len(board)):
            for c in range(len(board[r])):
                if (r, c) in reachable:
                    return r, c
        return x, y
                

    def move(self, board, extra_tile, player):
        self.check_state(board, extra_tile, player)

        re = self.check_move_goal_reachable(board, extra_tile, player)
        if re == -1:
            return self.check_move_alternative_reachable(board, extra_tile, player)
        return re

        


#class Euclid(Strategy):


if __name__ == '__main__':
    ...