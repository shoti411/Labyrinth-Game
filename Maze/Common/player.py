from state import state
from board import Board
from tile import Tile
from riemann import Riemann


class PlayerAPI:

    def __init__(self, name):
        self.name = name
        self.strategy = Riemann()
        self.game_state = False
        self.goal_position = False

    def name(self):
        return self.name

    def propose_board(self, rows, columns):
        board = []
        for i in range(rows):
            board.append([])
            for j in range(columns):
                board[i].append(Tile())
        return board

    def setup(self, game_state, goal_position):
        if game_state:
            self.game_state = game_state
        self.goal_position = goal_position

    def take_turn(self, game_state):
        self.game_state = game_state
        board, extra_tile, player = self.game_state
        action = self.strategy.slide_and_insert(board, extra_tile, player)
        if action == -1:
            return False
        degree, direction, index, is_row = action
        extra_tile.rotate(degree)
        if is_row:
            board.shift_row(index, direction, extra_tile)
        else:
            board.shift_column(index, direction, extra_tile)
        action = action, self.strategy.move(board, player)
        return action

    def won(self, w):
        return w
