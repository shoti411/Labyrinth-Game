from action import Pass, Move
from queue import PriorityQueue
from coordinate import Coordinate
from player_game_state import PlayerGameState


class Strategy:
    """
    Strategy represents an interface of the required functionality of a Strategy subclass. 
    This class is not intended to be instantiated.
    """

    def evaluate_move(self, state):
        """
        Evaluates a PlayerGameState determines what the best row or column to slide is and the best Coordinate to move to. 

        :param: state <PlayerGameState>: Knowledge the player has about the game state

        :return: <Move>:
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

    def get_enumerated_tiles(self, state):  
        """
        Creates a priority queue of the boards Tiles. 
        The priority of each Tile is based on the class implementing this method.

        :param: state <PlayerGameState>: Knowledge the player has about the game state

        :return: <PriorityQueue>
        """

        raise NotImplemented('enumeration not implemented.')

    def enumerate_on_priority(self, state, priority_function):
        board = state.get_board()
        player = state.get_player()
        enumerated_tiles = PriorityQueue()
        goal_position = board.find_tile_coordinate_by_tile(player.get_goal())
        enumerated_tiles.put((-1, goal_position))
        for r in range(len(board.get_board())):
            row_length = len(board.get_board()[r])
            for c in range(row_length):
                if Coordinate(r, c) != player.get_coordinate() and Coordinate(r, c) != goal_position:
                    priority = priority_function(r, c)
                    enumerated_tiles.put((priority, Coordinate(r, c)))
        return enumerated_tiles

    def evaluate_move(self, state):
        re = self.slide_and_insert(state)
        print(re)
        if not re:
            return Pass()
        (degree, coordinate), direction, index, is_row = re
        print(coordinate)
        return Move(degree, direction, index, is_row, coordinate)

    def slide_and_insert(self, state):
        """
        Evaluates a PlayerGameState determines what the best row or column to slide is
        
        slide_and_insert will return -1 if it is impossible to reach any other tile regardless of the move done.

        :param: state <PlayerGameState>: Knowledge the player has about the game state

        :return: (degree, direction, index, isrow): <(int, int, int, bool)>:\n
            degree: represents the degrees to rotate the extra_tile by.
            direction: represents the direction to shift the row or column by.\n
                -1 represents left or up\n
                1 represents right or down
            index: represents the row or column index to shift
            isrow: True or False for if the index is for a row or a column.
        """
        self.check_state(state)
        enumerated_tiles = self.get_enumerated_tiles(state)
        if enumerated_tiles.empty():
            return False
        return self.check_slide_insert(enumerated_tiles, state)

    def check_slide_insert(self, enumerated_tiles, state):
        """
        Check if the player can reach any of the enumerated_tiles. Checks in order of the enumerated_tiles priority queue. 
        Retuns the slide and insert move that allows for it to reach the highest priority Tile. 
        Prioritizes the top row down to the bottom row.
        Prioritizes the left col across to the right col.
        Prioritizes shifting the direction -1 or 1
        Prioritizes degrees in order [0, 90, 180, 270]

        :param: state <PlayerGameState>: Knowledge the player has about the game state

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
            re = self.check_row_shift(coordinate, state)
            if not re:
                re = self.check_col_shift(coordinate, state)
            if re:
                return re
        return False

    def check_col_shift(self, coordinate, state):
        """
        Checks if there exists a column shift which will allow the player to reach a given position.
        Prioritizes the left col across to the right col.
        Prioritizes shifting the direction -1 or 1
        Prioritizes degrees in order [0, 90, 180, 270]

        :param: state <PlayerGameState>: Knowledge the player has about the game state

        :return: (degree, direction, index, isrow) <(int, int, int, bool)>
            degree: represents the degrees to rotate the extra_tile by.
            direction: represents the direction to shift the column by.\n
                -1 represents up\n
                1 represents down
            index: represents the column index to shift
            isrow: True or False for if the index is for a row or a column.
                    This will always return False
        """
        for col_index in state.get_board().get_moveable_columns():
            re = self.check_direction(coordinate, state, col_index, False)
            if re:
                degree, direction = re
                return degree, direction, col_index, False
        return False


    def check_row_shift(self, coordinate, state):
        """
        Checks if there exists a row shift which will allow the player to reach a given position.
        Prioritizes the top row down to the bottom row.
        Prioritizes shifting the direction -1 or 1
        Prioritizes degrees in order [0, 90, 180, 270]

        :param: coordinate <Coordinate>: target coordinate.
        :param: state <PlayerGameState>: Knowledge the player has about the game state

        :return: (degree, direction, index, isrow) <(int, int, int, bool)>
            degree: represents the degrees to rotate the extra_tile by.
            direction: represents the direction to shift the row by.\n
                -1 represents left\n
                1 represents down
            index: represents the row index to shift
            isrow: True or False for if the index is for a row or a column.
                    This will always return True
        """

        for row_index in state.get_board().get_moveable_rows():
            re = self.check_direction(coordinate, state, row_index, True)
            if re:
                degree, direction = re
                return degree, direction, row_index, True
        return False
    

    def check_direction(self, coordinate, state, index, isrow):
        """
        Checks if shifting a given row or column and rotation of the extra_tile which will allow the player to reach a given position.
        Prioritizes shifting the direction -1 or 1
        Prioritizes degrees in order [0, 90, 180, 270]

        :param: coordinate <Coordinate>: target coordinate.
        :param: state <PlayerGameState>: Knowledge the player has about the game state
        :param: index <int>: index of the row or column to shift
        :param: isrow <bool>: True or False representing if the index is for a row or column.

        :return: (degree, direction) <(int, int)>
            degree: represents the degrees to rotate the extra_tile by.
            direction: represents the direction to shift the row or column by.\n
                -1 represents up\n
                1 represents down
        """

        for direction in self.DIRECTIONS:
            if not Move(0, direction, index, isrow, Coordinate(0,0)).does_undo(state.get_last_action()):
                degree = self.check_degrees(coordinate, state, index, direction, isrow)
                if degree:
                    return degree, direction
        return False


    def check_degrees(self, coordinate, state, index, direction, isrow):
        """
        Checks if any rotation of the extra_tile which will allow the player to reach a given position.
        Prioritizes degrees in order [0, 90, 180, 270]

        :param: coordinate <Coordinate>: target coordinate.
        :param: state <PlayerGameState>: Knowledge the player has about the game state
        :param: index <int>: index of the row or column to shift
        :param: direction <int>: direction to shift the row or column by
        :param: isrow <bool>: True or False representing if the index is for a row or column.

        :return: (degree) <int>
            degree: represents the degrees to rotate the extra_tile by.
        """
        
        for degree in self.DEGREES:

            board_copy = state.get_board()
            tile_copy = state.get_extra_tile()
            player = state.get_player()

            tile_copy.rotate(degree)
            if isrow:
                board_copy.shift_row(index, direction, tile_copy)
            else:
                board_copy.shift_column(index, direction, tile_copy)

            updated_player_coordinate = self.update_position(player.get_coordinate(), index, direction, isrow, state.get_board())
            goal_tile = state.get_board().getTile(coordinate)
            updated_coordinate = board_copy.find_tile_coordinate_by_tile(goal_tile)
            if board_copy.coordinate_is_reachable_from(updated_coordinate, updated_player_coordinate):
                return degree, updated_coordinate
        return False


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


    def check_state(self, state):
        if not isinstance(state, PlayerGameState):
            raise ValueError('Given state must be of type PlayerGameState.')

                

    



