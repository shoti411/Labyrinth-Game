from tile import Tile
from board import Board
from player_state import Player
from coordinate import Coordinate 
import copy

class Strategy:
    """
    Strategy represents an interface of the required functionality of a Strategy subclass. 
    This class is not intended to be instantiated.
    """

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

        raise NotImplemented('slide_and_insert not implemented.')

    def move(self, board, player):
        """
        move takes in a board, and player. It evaluates this game state and determines what 
        the location to move to is.

        move will return the x, y coordinates of the players current location if it is unable to reach any other tile.

        :param: board <Board>: Maze game scenario board
        :param: player <Player>: Active player of Maze game scenario

        :return: (x, y): <(int, int)>:\n
            x: represents the x coordinate to move to.
            y: represents the y coordinate to move to.
        """
        
        raise NotImplemented('move not implemented.')

        


class AbstractStrategy(Strategy):
    """
    AbstractStrategy is a abstract class for the interface Strategy. This class is not intended to be instantiated.

    AbstractStrategy requires that get_enumerated_tiles be implemented by subclasses.
    """

    # DEGREES: <list(int)> Represents valid degree values to rotate a Tile by.
    DEGREES = [0, 90, 180, 270]
    # DIRECTIONS: <list(int)> Represents valid directions for sliding a row or column by.
    DIRECTIONS = [-1, 1]


    def get_enumerated_tiles(self, board, player):  
        """
        Creates a priority queue of the boards Tiles. 
        The priority of each Tile is based on the class implementing this method.

        :param: board <Board>: Maze game scenario board
        :param: player <Player>: Active player of Maze game scenario

        :return: <PriorityQueue>
        """

        raise NotImplemented('enumeration not implemented.')


    def slide_and_insert(self, board, extra_tile, player):
        self.check_state(board, player, extra_tile)
        enumerated_tiles = self.get_enumerated_tiles(board, player)
        if enumerated_tiles.empty():
            return -1
        return self.check_slide_insert(enumerated_tiles, board, player, extra_tile)


    def move(self, board, player):
        self.check_state(board, player)
        enumerated_tiles = self.get_enumerated_tiles(board, player)
        return self.check_move(enumerated_tiles, board, player)


    def check_slide_insert(self, enumerated_tiles, board, player, extra_tile):
        """
        Check if the player can reach any of the enumerated_tiles. Checks in order of the enumerated_tiles priority queue. 
        Retuns the slide and insert move that allows for it to reach the highest priority Tile. 
        Prioritizes the top row down to the bottom row.
        Prioritizes the left col across to the right col.
        Prioritizes shifting the direction -1 or 1
        Prioritizes degrees in order [0, 90, 180, 270]

        :param: enumerated_tiles <PriorityQueue(Coordinate)>: Priority queue of the boards Tiles coordinates.
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
        while not enumerated_tiles.empty():
            _, coordinate = enumerated_tiles.get()
            re = self.check_row_shift(coordinate, player, board, extra_tile)
            if re == -1:
                re = self.check_col_shift(coordinate, player, board, extra_tile)
            if re != -1:
                return re
        return -1

    def check_col_shift(self, coordinate, player, board, extra_tile):
        """
        Checks if there exists a column shift which will allow the player to reach a given position.
        Prioritizes the left col across to the right col.
        Prioritizes shifting the direction -1 or 1
        Prioritizes degrees in order [0, 90, 180, 270]

        :param: coordinate <Coordinate>: target coordinate.
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
            re = self.check_direction(coordinate, player, board, extra_tile, col_index, False)
            if re != -1:
                degree, direction = re
                return degree, direction, col_index, False
        return -1


    def check_row_shift(self, coordinate, player, board, extra_tile):
        """
        Checks if there exists a row shift which will allow the player to reach a given position.
        Prioritizes the top row down to the bottom row.
        Prioritizes shifting the direction -1 or 1
        Prioritizes degrees in order [0, 90, 180, 270]

        :param: coordinate <Coordinate>: target coordinate.
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
            re = self.check_direction(coordinate, player, board, extra_tile, row_index, True)
            if re != -1:
                degree, direction = re
                return degree, direction, row_index, True
        return -1
    

    def check_direction(self, coordinate, player, board, extra_tile, index, isrow):
        """
        Checks if shifting a given row or column and rotation of the extra_tile which will allow the player to reach a given position.
        Prioritizes shifting the direction -1 or 1
        Prioritizes degrees in order [0, 90, 180, 270]

        :param: coordinate <Coordinate>: target coordinate.
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
            degree = self.check_degrees(coordinate, player, board, extra_tile, index, direction, isrow)
            if degree != -1:
                return degree, direction
        return -1


    def check_degrees(self, coordinate, player, board, extra_tile, index, direction, isrow):
        """
        Checks if any rotation of the extra_tile which will allow the player to reach a given position.
        Prioritizes degrees in order [0, 90, 180, 270]

        :param: coordinate <Coordinate>: target coordinate.
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

            updated_player_coordinate = self.update_position(player.get_position(), index, direction, isrow, board)
            
            goal_tile = board.getTile(coordinate)
            updated_coordinate = board_copy.find_tile_coordinate_by_tile(goal_tile)
            reachable = board_copy.get_reachable_tiles(updated_player_coordinate)

            if updated_coordinate in reachable:
                return degree
        return -1


    def update_position(self, coordinate, index, direction, isrow, board):
        """
        Move the coordiante if it is affected by a slide performed with (index, direction, isrow) on board.
        If coordinate is knocked off then wrap coordinate to the newly inserted location.

        :param: coordinate <Coordinate>: Coordinate of Tile
        :param: index <int>: index of the row or column to shift
        :param: direction <int>: direction to shift the row or column by
        :param: isrow <bool>: True or False representing if the index is for a row or column.
        :param: board <Board>: Maze game scenario board

        :return: <Coordinate>: representing the updated position
        """
        x = coordinate.getX()
        y = coordinate.getY()
        if x == index and isrow:
            y = (y + direction) % len(board.get_board()[index])
        if y == index and not isrow:
            x = (x + direction) % len(board.get_board())
        return Coordinate(x, y)

    def check_move(self, enumerated_tiles, board, player):
        """
        Check if the player can reach any of the enumerated_tiles. Checks in order of the enumerated_tiles priority queue. 
        
        Will return -1 if the player can not move to a new tile.

        :param: enumerated_tiles <PriorityQueue(Tile)>: Priority queue of the boards Tiles.
        :param: board <Board>: Maze game scenario board
        :param: player <Player>: Active player of Maze game scenario

        :return: <Coordinate>:
        """

        reachable = board.get_reachable_tiles(player.get_position())
        while not enumerated_tiles.empty():
            _, coordinate = enumerated_tiles.get()
            if coordinate in reachable:
                return coordinate
        return -1
    

    def check_state(self, board, player, extra_tile=False):
        if not isinstance(board, Board):
            raise ValueError('Given board must be of type board.')
        if not (isinstance(extra_tile, Tile) or (not extra_tile)):
            raise ValueError('extra_tile must be of type Tile.')
        if not isinstance(player, Player):
            raise ValueError('player must be of type Player.')

                

    



