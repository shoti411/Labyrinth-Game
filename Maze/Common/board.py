from tile import Tile
from directions import Direction
from coordinate import Coordinate
import copy


class Board:
    """
    Data representation of the game board of maze.

    Supports:
        Shifting columns and rows while inputting a given Tile.
        Checking reachable tiles from any given position.
    """

    def __init__(self, board):
        """
        Constructs a new Board with a given list of list of Tiles.

        :param: board (list(list(Tile))): Represents a game board made of individual Tile.
                board is represented by: board[x][y], where x is row, and y is column
                                         board[0][0] is the top left corner of the board.
        """
        self.__check_board(board)
        self.__board = board

    def __check_board(self, board):
        """
        Verify a board is valid. All rows are equal length, all positions are Tile objects,\
             and length of rows and columns are Natural numbers.  

        :param: board (list(list(Tile))): Represents a game board made of individual Tile.
        """

        if not board or not isinstance(board, list):
            raise ValueError('Board is an invalid board.')

        row_length = len(board[-1])
        for row in board:
            if len(row) != row_length:
                raise ValueError('Board is an invalid board. A board must have equal column lengths.')
            for tile in row:
                if not isinstance(tile, type(Tile())):
                    raise ValueError('Board is an invalid board. A board must have all spaces filled with Tiles.')

    def get_board(self):
        return copy.deepcopy(self.__board)

    def find_tile_coordinate_by_tile(self, tile):
        """
        Finds the coordinate of a given Tile.

        :param: tile <Tile>: Tile to find coordinate of.

        :return: <Coordiante>
        """

        for r in range(len(self.__board)):
            for c in range(len(self.__board[r])):
                if tile == self.__board[r][c]:
                    return Coordinate(r, c)
        return Coordinate(-1, -1)

    def getTile(self, coordinate):
        """
        Returns Tile at coordiante 
        
        :param: coordinate <Coordinate>: Coordinate must have a positive x and y
        """
        if coordinate.getX() < 0 or coordinate.getY() < 0:
            raise ValueError('Coordinate must have a positive x and y')
        return self.__board[coordinate.getX()][coordinate.getY()]


    def shift_column(self, index, direction, extra_tile):
        """
        Slides a columns in a given direction. Takes a Tile piece off the end. Adds a given Tile at the other end.

        :param: index (int): Column index to shift. index must be a even number.
        :param: direction (int): -1 or 1 representing moving down or up respectively. 
        :param: extra_tile (Tile): new Insertable Tile

        :returns: (Tile): Tile that has been taken off the end.
        """

        self.__shifting_board_error_check(index, direction, extra_tile, row=False)

        col = [row[index] for row in self.__board]
        if direction == 1:
            new_extra_tile, col = self.__shift_tile_list_backward(col, extra_tile)
        elif direction == -1:
            new_extra_tile, col = self.__shift_tile_list_forward(col, extra_tile)

        for i, row in enumerate(self.__board):
            row[index] = col[i]
        return new_extra_tile

    def shift_row(self, index, direction, extra_tile):
        """
        Slides a row in a given direction. Takes a Tile piece off the end. Adds a given Tile at the other end.

        :param: index (int): Row index to shift. index must be an even number.
        :param: direction (int): -1 or 1 representing moving left or right respectively. 
        :param: extra_tile (Tile): new Insertable Tile

        :returns: (Tile): Tile that has been taken off the end.
        """

        self.__shifting_board_error_check(index, direction, extra_tile)

        row = self.__board[index]
        if direction == 1:
            new_extra_tile, row = self.__shift_tile_list_backward(row, extra_tile)
        elif direction == -1:
            new_extra_tile, row = self.__shift_tile_list_forward(row, extra_tile)
        self.__board[index] = row
        return new_extra_tile

    def __shift_tile_list_forward(self, tiles, extra_tile):
        """
        Drops the last tile and adds a new one at the start.

        :param: tiles (list(Tile))
        :param: extra_tile (Tile)

        :return: (Tile, list(Tile))
        """
        new_extra_tile = tiles[0]
        tiles = tiles[1:]
        tiles.append(extra_tile)
        return new_extra_tile, tiles

    def __shift_tile_list_backward(self, tiles, extra_tile):
        """
        Drops the first tile and adds a new one at the end.

        :param: tiles (list(Tile))
        :param: extra_tile (Tile)

        :return: (Tile, list(Tile))
        """
        new_extra_tile = tiles[-1]
        tiles = tiles[:-1]
        tiles.insert(0, extra_tile)
        return new_extra_tile, tiles

    def __shifting_board_error_check(self, index, direction, extra_tile, row=True):
        """
        Checks that the parameters for shifting a row or column are valid.\
        
        :param: index (int): index of row or column to shift. index must be an even number. 
        :param: direction (int): -1 or 1 representing moving left or right respectively. 
        :param: extra_tile (Tile): new Insertable Tile
        :param: row (bool): Defaults True. Represents whether we are checking for a row or column.  
        """

        if row and (index < 0 or index > len(self.__board)):
            raise IndexError('Cannot shift undefined row.')
        elif not row and (index < 0 or index > len(self.__board[0])):
            raise IndexError('Cannot shift undefined column.')

        if index % 2 != 0:
            raise IndexError('Indices must be even.')

        if direction not in [-1, 1]:
            raise ValueError('Direction must be either -1 or 1')

        if not isinstance(extra_tile, Tile):
            raise ValueError('extra_tile must be a type Tile object')

    def get_reachable_tiles(self, coordinate):
        """
        Check the reachable Tiles from a Tile at a given coordinate.

        :param: coordiante (Coordinate)

        :return: (list(Coordinate)): List of reachable Coordinates
        """

        if coordinate.getX() not in range(len(self.__board)) or coordinate.getY() not in range(len(self.__board[0])):
            raise ValueError('Cannot check reachable tiles from invalid index.')
        return self.__get_reachable_tiles_recurse(coordinate, [])

    def __get_reachable_tiles_recurse(self, coordinate, visited):
        if coordinate.getX() not in range(len(self.__board)) or coordinate.getY() not in range(len(self.__board[0])):
            return visited
        visited.append(coordinate)

        connections = self.__connections(coordinate)
        for connection in connections:
            if connection not in visited:
                visited = visited + self.__get_reachable_tiles_recurse(connection, visited)

        unique_visited = []
        for coordinate in visited:
            if coordinate not in unique_visited:
                unique_visited.append(coordinate)


        return unique_visited

    def __connections(self, coordinate):
        """
        Checks and returns which of the surroundomg Tiles from a given coordinate are connected.

        :param: coordiante (Coordinate)
        
        :return: (list(Direction)): List of reachable directions
        """

        x = coordinate.getX()
        y = coordinate.getY()
        connections = []
        directions = self.getTile(coordinate).get_paths()

        if x > 0 and Direction.UP in directions and Direction.DOWN in self.__board[x - 1][y].get_paths():
            connections.append(Coordinate(x - 1, y))
        if x < len(self.__board) - 1 and Direction.DOWN in directions \
                and Direction.UP in self.__board[x + 1][y].get_paths():
            connections.append(Coordinate(x + 1, y))
        if y > 0 and Direction.LEFT in directions and Direction.RIGHT in self.__board[x][y - 1].get_paths():
            connections.append(Coordinate(x, y - 1))
        if y < len(self.__board[0]) - 1 and Direction.RIGHT in directions and Direction.LEFT in self.__board[x][
            y + 1].get_paths():
            connections.append(Coordinate(x, y + 1))

        return connections

    def __str__(self):
        return_string = ''
        for row in self.__board:
            for tile in row:
                return_string += '[' + str(tile) + ']'
            return_string += '\n'

        return return_string[:-1]
