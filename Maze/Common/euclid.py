from strategy import AbstractStrategy
from queue import PriorityQueue
from coordinate import Coordinate
import math

class Euclid(AbstractStrategy):
    """
    Euclid is a Strategy for Maze game that interprets a board, player, and extra_tile to find what it thinks is the next best move.

    Euclid works by first testing every possible move and seeing if it can reach the goal the state.
    If it cannot then it will try to reach the closest tile to the goal state by Euclidean distance.
    Tie breaker for Euclidean distance is lexigraphically in row-column order.
    """

    def get_enumerated_tiles(self, state):
        """
        Creates a priority queue of the boards Tiles. 
        The highest priority is the goal tile then it is each tile with the closest Euclidean distance to the goal tile.
        Tie breaker for Euclidean distance is done lexigraphically in row-column order.
        
        :param: state <PlayerGameState>: Knowledge the player has about the game state

        :return: <PriorityQueue>
        """

        board = state.get_board()
        player = state.get_player()
        enumerated_tiles = PriorityQueue()
        goal_position = board.find_tile_coordinate_by_tile(player.get_goal())
        enumerated_tiles.put((-1, goal_position))

        for r in range(len(board.get_board())):
            row_length = len(board.get_board()[r])
            for c in range(row_length):
                if Coordinate(r, c) != player.get_coordinate() and Coordinate(r, c) != goal_position:
                    priority = math.sqrt((r-goal_position.getX())**2 + (c-goal_position.getY())**2)
                    enumerated_tiles.put((priority, Coordinate(r, c)))
        return enumerated_tiles
