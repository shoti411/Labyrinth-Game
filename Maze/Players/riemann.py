from strategy import AbstractStrategy
from coordinate import Coordinate
from queue import PriorityQueue

class Riemann(AbstractStrategy):
    """
    Riemann is a Strategy for Maze game that interprets a board, player, and extra_tile to find what it thinks is the next best move.

    Riemann works by first testing every possible move and seeing if it can reach the goal the state.
    If it cannot then it will try to reach the top-most left-most position that it can reach. 
    """

    def get_enumerated_tiles(self, state):
        """
        Creates a priority queue of the boards Tiles. 
        The highest priority is the goal tile then it is each tile lexigraphically in row-column order. 
        
        :param: state <PlayerGameState>: Knowledge the player has about the game state

        :return: <PriorityQueue>
        """

        board = state.get_board()
        row_length = len(board.get_board())

        def priority_function(r, c):
            return r * row_length + c
        return super().enumerate_on_priority(state, priority_function)

