import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"../Common"))

from board import Board
from tile import Tile
from riemann import Riemann
from euclid import Euclid



class PlayerAPI:

    # TODO: ENUM for strategies, not passing strings
    def __init__(self, name, strategy='Riemann'):
        self.name = name
        self.strategy = Riemann()
        self.game_state = False
        self.goal_position = False

    def get_strategy(self, strategy):
        if strategy == 'Riemann':
            return Riemann()
        elif strategy == 'Euclid':
            return Euclid()

        raise ValueError(f'{strategy} does not exist')


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
        return self.strategy.evaluate_move(self.game_state)

    def won(self, w):
        return w
