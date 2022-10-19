from strategy import AbstractStrategy
from queue import PriorityQueue
import math

class Euclid(AbstractStrategy):
    """
    Euclid is a Strategy for Maze game that interprets a board, player, and extra_tile to find what it thinks is the next best move.

    Euclid works by first testing every possible move and seeing if it can reach the goal the state.
    If it cannot then it will try to reach the closest tile to the goal state by Euclidean distance.
    Tie breaker for Euclidean distance is lexigraphically in row-column order.
    """

    def get_enumerated_tiles(self, board, player):
        """
        Creates a priority queue of the boards Tiles. 
        The highest priority is the goal tile then it is each tile with the closest Euclidean distance to the goal tile.
        Tie breaker for Euclidean distance is done lexigraphically in row-column order.

        If the goal tile is not on the board then the Euclidean distance will be based on the player position not the goal tile.
        
        :param: board <Board>: Maze game scenario board
        :param: player <Player>: Active player of Maze game scenario

        :return: <PriorityQueue>
        """

        enumerated_tiles = PriorityQueue()

        goal_position = board.find_tile_position_by_tile(player.get_goal())
        enumerated_tiles.put((-1, goal_position))

        target_x, target_y = goal_position
        if goal_position == (-1, -1):
            target_x, target_y = player.get_position()

        for r in range(len(board.get_board())):
            row_length = len(board.get_board()[r])
            for c in range(row_length):
                if (r, c) != player.get_position() and (r, c) != goal_position:
                    priority = math.sqrt((r-target_x)**2 + (c-target_y)**2)
                    enumerated_tiles.put((priority, (r, c)))
        return enumerated_tiles
