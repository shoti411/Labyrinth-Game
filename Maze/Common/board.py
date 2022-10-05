from tile import Tile
import copy
"""

sliding a designated row or column in one or the other direction;

inserting a tile into the spot that is left open by a slide;

determining which tiles are reachable from a designated tile.

"""


class Board:

    def __init__(self, rows=7, cols=7, board=None, extra_tile=None):
        if rows < 0 or cols < 0:
            raise ValueError(f'Provided rows and columns must be non-negative. Given: [{rows}, {cols}]')

        self.__extra_tile = extra_tile
        if extra_tile is None:
            self.__extra_tile = Tile()

        self.__board = board
        if board is None:
            self.__board = self.__create_board(rows, cols)

    def __create_board(self, rows, cols):
        board = []
        if cols == 0 or rows == 0:
            return board

        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(Tile())
            board.append(row)
        return board

    def get_board(self):
        return copy.deepcopy(self.__board)

    def get_extra_tile(self):
        return copy.deepcopy(self.__extra_tile)

    def shift_column(self, index, direction):
        if index < 0 or index > len(self.__board[0]):
            raise IndexError('Cannot shift undefined column.')
        if direction not in [-1, 1]:
            raise ValueError('Direction must be either -1 or 1')

        col = [row[index] for row in self.__board]
        if direction == 1:
            new_extra_tile = col[-1]
            col = col[:-1]
            col.insert(0, self.__extra_tile)
        elif direction == -1:
            new_extra_tile = col[0]
            col = col[1:]
            col.append(self.__extra_tile)

        for i, row in enumerate(self.__board):
            row[index] = col[i]

        self.__extra_tile = new_extra_tile
        return self.__board

    def shift_row(self, index, direction):
        if index < 0 or index > len(self.__board):
            raise IndexError('Cannot shift undefined row.')
        if direction not in [-1, 1]:
            raise ValueError('Direction must be either -1 or 1')

        row = self.__board[index]
        if direction == 1:
            new_extra_tile = row[-1]
            row = row[:-1]
            row.insert(0, self.__extra_tile)
        elif direction == -1:
            new_extra_tile = row[0]
            row = row[1:]
            row.append(self.__extra_tile)
        self.__board[index] = row
        self.__extra_tile = new_extra_tile

    def get_reachable_tiles(self, x, y):
        if x not in range(len(self.__board)) or y not in range(len(self.__board[0])):
            raise ValueError('Cannot check reachable tiles from invalid index.')
        return self.__get_reachable_tiles_recurse(x, y, [])

    def __get_reachable_tiles_recurse(self, x, y, visited):
        if x not in range(len(self.__board)) or y not in range(len(self.__board[0])):
            return visited
        visited.append((x, y))

        this_tile = self.__board[x][y]
        directions = this_tile.get_paths()

        if x > 0 and 'UP' in directions and 'DOWN' in self.__board[x - 1][y].get_paths() and (x - 1, y) not in visited:
            visited = visited + self.__get_reachable_tiles_recurse(x - 1, y, visited)

        if x < len(self.__board) - 1 \
                and 'DOWN' in directions \
                and 'UP' in self.__board[x + 1][y].get_paths() \
                and (x + 1, y) not in visited:
            visited = visited + self.__get_reachable_tiles_recurse(x + 1, y, visited)

        if y > 0 and 'LEFT' in directions \
                and 'RIGHT' in self.__board[x][y - 1].get_paths() \
                and (x, y - 1) not in visited:
            visited = visited + self.__get_reachable_tiles_recurse(x, y - 1, visited)

        if y < len(self.__board[0]) - 1 \
                and 'RIGHT' in directions \
                and 'LEFT' in self.__board[x][y + 1].get_paths() \
                and (x, y + 1) not in visited:
            visited = visited + self.__get_reachable_tiles_recurse(x, y + 1, visited)

        return list(set(visited))


    def __str__(self):
        return_string = ''
        for row in self.__board:
            for tile in row:
                return_string += '[' + str(tile) + ']'
            return_string += '\n'

        return return_string[:-1]
