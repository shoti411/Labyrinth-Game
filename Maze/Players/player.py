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
        self.strategy = self.get_strategy(strategy)
        self.game_state = False
        self.goal_position = False

    def get_strategy(self, strategy):
        if strategy == 'Riemann':
            return Riemann()
        elif strategy == 'Euclid':
            return Euclid()

        raise ValueError(f'{strategy} does not exist')

    def get_name(self):
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


class BadPlayerAPI(PlayerAPI):

    def __init__(self, name, error_function, strategy='Riemann'):
        """ :param: error_function <String>: represents the name of the function that will fail """
        super().__init__(name, strategy)
        self.error_function = error_function

    def won(self, w):
        if self.error_function == 'win':
            raise ValueError(f'{self.name} ERRORED IN WON.')
        else:
            return super().won(w)

    def take_turn(self, game_state):
        if self.error_function == 'takeTurn':
            raise ValueError(f'{self.name} ERRORED IN TAKETURN.')
        else:
            return super().take_turn(game_state)

    def setup(self, game_state, goal_position):
        if self.error_function == 'setUp':
            raise ValueError(f'{self.name} ERRORED IN SETUP.')
        else:
            return super().setup(game_state, goal_position)

