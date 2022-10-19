from tile import Tile
from board import Board
from player import Player
from strategy import Strategy
import copy

class Riemann(Strategy):
    """
    Riemann is a Strategy for Maze game that interprets a board, player, and extra_tile to find what it thinks is the next best move.

    Riemann works by first testing every possible move and seeing if it can reach the goal the state.
    If it cannot then it will try to reach the top-most left-most position that it can reach. 
    """

    # DEGREES: <list(int)> Represents valid degree values to rotate a Tile by.
    DEGREES = [0, 90, 180, 270]
    # DIRECTIONS: <list(int)> Represents valid directions for sliding a row or column by.
    DIRECTIONS = [-1, 1]


    def slide_and_insert(self, board, extra_tile, player):
        """
        slide_and_insert takes in a board, extra_tile, and player. It evaluates this game state and determines what 
        the best row or column to slide is. 
        
        slide_and_insert will return -1 if it is impossible to reach any other tile regardless of the move done.

        :param: board <Board>: Maze game scenario board
        :param: extra_tile <Tile>: extra tile of Maze game scenario
        :param: player <Player>: Active player of Maze game scenario

        :return: (degree, direction, index, isrow): <(int, int, int, bool)>:\n
            degree: represents the degrees to rotate the extra_tile by.
            direction: represents the direction to shift the row or column by.\n
                -1 represents left or up\n
                1 represents right or down
            index: represents the row or column index to shift
            isrow: True or False for if the index is for a row or a column.
        """

        self.check_state(board, player, extra_tile)

        re = self.check_goal_reachable(board, extra_tile, player)
        if re == -1:
            return self.check_alternative_reachables(board, extra_tile, player)
        return re


    def move(self, board, player):
        """
        move takes in a board, and player. It evaluates this game state and determines what 
        the location to move to is.

        move will return the x, y coordinates of the players current location if it is unable to reach any other tile.

        :param: board <Board>: Maze game scenario board
        :param: extra_tile <Tile>: extra tile of Maze game scenario
        :param: player <Player>: Active player of Maze game scenario

        :return: (x, y): <(int, int)>:\n
            x: represents the x coordinate to move to.
            y: represents the y coordinate to move to.
        """

        self.check_state(board, player)

        re = self.check_move_goal_reachable(board, player)
        if re == -1:
            return self.check_move_alternative_reachable(board, player)
        return re


    def check_goal_reachable(self, board, extra_tile, player):
        """
        Checks if there exists a row or column shift which will allow the player to reach their goal position.

        :param: board <Board>: Maze game scenario board
        :param: extra_tile <Tile>: extra tile of Maze game scenario
        :param: player <Player>: Active player of Maze game scenario

        :return: (degree, direction, index, isrow) <(int, int, int, bool)>
            degree: represents the degrees to rotate the extra_tile by.
            direction: represents the direction to shift the column by.\n
                -1 represents up\n
                1 represents down
            index: represents the column index to shift
            isrow: True or False for if the index is for a row or a column.
                    This will always return False
        """

        goal_position = board.find_tile_position_by_tile(player.get_goal())
        target_x, target_y = -1, -1 # TODO define -1, -1
        if goal_position != -1:
            target_x, target_y = goal_position

        re = self.check_row_shift(target_x, target_y, player, board, extra_tile)
        if re == -1:
            return self.check_col_shift(target_x, target_y, player, board, extra_tile)
        return re


    def check_alternative_reachables(self, board, extra_tile, player):
        """
        Checks if there exists a row or column shift which will allow the player to reach the top-most left-most position.

        :param: board <Board>: Maze game scenario board
        :param: extra_tile <Tile>: extra tile of Maze game scenario
        :param: player <Player>: Active player of Maze game scenario

        :return: (degree, direction, index, isrow) <(int, int, int, bool)>
            degree: represents the degrees to rotate the extra_tile by.
            direction: represents the direction to shift the column by.\n
                -1 represents up\n
                1 represents down
            index: represents the column index to shift
            isrow: True or False for if the index is for a row or a column.
                    This will always return False
        """

        for r in range(len(board.get_board())):
            for c in range(len(board.get_board()[r])):
                if (r, c) != player.get_position():
                    re = self.check_row_shift(r, c, player, board, extra_tile)
                    if re == -1:
                        re = self.check_col_shift(r, c, player, board, extra_tile)
                    if re != -1:
                        return re
        return -1


    def check_col_shift(self, target_x, target_y, player, board, extra_tile):
        """
        Checks if there exists a column shift which will allow the player to reach a given position.

        :param: target_x <int>: target x position to reach 
        :param: target_y <int>: target y position to reach
        :param: player <Player>: Active player of Maze game scenario
        :param: board <Board>: Maze game scenario board
        :param: extra_tile <Tile>: extra tile of Maze game scenario

        :return: (degree, direction, index, isrow) <(int, int, int, bool)>
            degree: represents the degrees to rotate the extra_tile by.
            direction: represents the direction to shift the column by.\n
                -1 represents up\n
                1 represents down
            index: represents the column index to shift
            isrow: True or False for if the index is for a row or a column.
                    This will always return False
        """
        for col_index in range(len(board.get_board()[0]))[::2]:
            re = self.check_direction(target_x, target_y, player, board, extra_tile, col_index, False)
            if re != -1:
                degree, direction = re
                return degree, direction, col_index, False
        return -1


    def check_row_shift(self, target_x, target_y, player, board, extra_tile):
        """
        Checks if there exists a row shift which will allow the player to reach a given position.

        :param: target_x <int>: target x position to reach 
        :param: target_y <int>: target y position to reach
        :param: player <Player>: Active player of Maze game scenario
        :param: board <Board>: Maze game scenario board
        :param: extra_tile <Tile>: extra tile of Maze game scenario

        :return: (degree, direction, index, isrow) <(int, int, int, bool)>
            degree: represents the degrees to rotate the extra_tile by.
            direction: represents the direction to shift the row by.\n
                -1 represents left\n
                1 represents down
            index: represents the row index to shift
            isrow: True or False for if the index is for a row or a column.
                    This will always return True
        """

        for row_index in range(len(board.get_board()))[::2]:
            re = self.check_direction(target_x, target_y, player, board, extra_tile, row_index, True)
            if re != -1:
                degree, direction = re
                return degree, direction, row_index, True
        return -1
    

    def check_direction(self, target_x, target_y, player, board, extra_tile, index, isrow):
        """
        Checks if shifting a given row or column and rotation of the extra_tile which will allow the player to reach a given position.

        :param: target_x <int>: target x position to reach 
        :param: target_y <int>: target y position to reach
        :param: player <Player>: Active player of Maze game scenario
        :param: board <Board>: Maze game scenario board
        :param: extra_tile <Tile>: extra tile of Maze game scenario
        :param: index <int>: index of the row or column to shift
        :param: isrow <bool>: True or False representing if the index is for a row or column.

        :return: (degree, direction) <(int, int)>
            degree: represents the degrees to rotate the extra_tile by.
            direction: represents the direction to shift the row or column by.\n
                -1 represents up\n
                1 represents down
        """

        for direction in self.DIRECTIONS:
            degree = self.check_degrees(target_x, target_y, player, board, extra_tile, index, direction, isrow)
            if degree != -1:
                return degree, direction
        return -1


    def check_degrees(self, target_x, target_y, player, board, extra_tile, index, direction, isrow):
        """
        Checks if any rotation of the extra_tile which will allow the player to reach a given position.

        :param: target_x <int>: target x position to reach 
        :param: target_y <int>: target y position to reach
        :param: player <Player>: Active player of Maze game scenario
        :param: board <Board>: Maze game scenario board
        :param: extra_tile <Tile>: extra tile of Maze game scenario
        :param: index <int>: index of the row or column to shift
        :param: direction <int>: direction to shift the row or column by
        :param: isrow <bool>: True or False representing if the index is for a row or column.

        :return: (degree) <int>
            degree: represents the degrees to rotate the extra_tile by.
        """
        for degree in self.DEGREES:
            board_copy = copy.deepcopy(board)
            tile_copy = copy.deepcopy(extra_tile)
            tile_copy.rotate(degree)
            if isrow:
                board_copy.shift_row(index, direction, tile_copy)
            else:
                board_copy.shift_column(index, direction, tile_copy)
            x, y = player.get_position()
            updated_x, updated_y = self.update_position(x, y, index, direction, isrow, board)
            reachable = board_copy.get_reachable_tiles(updated_x, updated_y)
            if target_x == -1 and target_y == -1:
                target_x, target_y = board.find_tile_position_by_tile(tile_copy) 
            updated_target_x, updated_target_y = self.update_position(target_x, target_y, index, direction, isrow, board)
            if (updated_target_x, updated_target_y) in reachable:
                return degree
        return -1


    def update_position(self, x, y, index, direction, isrow, board):
        if x == index and isrow:
            y = (y + direction) % len(board.get_board()[index])
        if y == index and not isrow:
            x = (x + direction) % len(board.get_board())
        return x, y


    def check_move_goal_reachable(self, board, player):
        """
        Takes in a board, and player. Checks if the players goal tile is reachable

        Will return -1 if the goal tile is not reachable.

        :param: board <Board>: Maze game scenario board
        :param: player <Player>: Active player of Maze game scenario

        :return: (x, y): <(int, int)>:\n
            x: represents the x coordinate to move to.
            y: represents the y coordinate to move to.
        """

        x, y = player.get_position()
        goal_x, goal_y = board.find_tile_position_by_tile(player.get_goal())
        reachable = board.get_reachable_tiles(x, y)
        if (goal_x, goal_y) in reachable:
            return goal_x, goal_y
        return -1


    def check_move_alternative_reachable(self, board, player):
        """
        Takes in a board, and player. Returns the top-most left-most position it can move too.

        Will return -1 if there is no tile to move to.

        :param: board <Board>: Maze game scenario board
        :param: player <Player>: Active player of Maze game scenario

        :return: (x, y): <(int, int)>:\n
            x: represents the x coordinate to move to.
            y: represents the y coordinate to move to.
        """
        x, y = player.get_position()
        reachable = board.get_reachable_tiles(x, y)
        for r in range(len(board.get_board())):
            for c in range(len(board.get_board()[r])):
                if (r, c) in reachable:
                    return r, c
        return x, y