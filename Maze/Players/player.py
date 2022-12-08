import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"../Common"))
from tile import Tile
from riemann import Riemann
from euclid import Euclid

class PlayerAPI:
    """ This class should not be instantiated """
    def propose_board(self, rows, columns):
        raise NotImplemented('propose_board not implemented')

    def setup(self, game_state, goal_position):
        raise NotImplemented('setup not implemented')

    def take_turn(self, game_state):
        raise NotImplemented('take_turn not implemented')

    def won(self, w):
        raise NotImplemented('won not implemented')


class LocalPlayerAPI(PlayerAPI):

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


class BadPlayerAPI(LocalPlayerAPI):

    def __init__(self, name, error_function, error_count, strategy='Riemann'):
        """ :param: error_function <String>: represents the name of the function that will fail """
        assert 7 >= error_count >= 1, 'Error count must be a natural num between 1-7'
        super().__init__(name, strategy)
        self.error_function = error_function
        self.error_count = error_count

    def won(self, w):
        if self.error_function == 'win':
            self.error_count -= 1
            if self.error_count == 0:
                raise TimeoutError('win timed out.')
        else:
            return super().won(w)

    def take_turn(self, game_state):
        if self.error_function == 'takeTurn':
            self.error_count -= 1
            if self.error_count == 0:
                raise TimeoutError('take turn timed out.')
        else:
            return super().take_turn(game_state)

    def setup(self, game_state, goal_position):
        if self.error_function == 'setUp':
            self.error_count -= 1
            if self.error_count == 0:
                raise TimeoutError('setup timed out.')
        else:
            return super().setup(game_state, goal_position)
