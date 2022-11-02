import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../../Players"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../../Referee"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../../Common"))

import pytest
from state import State
from player_state import Player
from board import Board
from tile import Tile
from coordinate import Coordinate
from euclid import Euclid
from player_game_state import PlayerGameState
from action import Pass
from player import PlayerAPI
from referee import Referee
from observer import Observer

default_board = Board([[Tile("┘"), Tile("┤"), Tile("┼"), Tile("│"), Tile("┬"), Tile("┐"), Tile("┬")],
                       [Tile("─"), Tile("│"), Tile("│"), Tile("├"), Tile("┌"), Tile("├"), Tile("┌")],
                       [Tile("┬"), Tile("│"), Tile("┬"), Tile("┘"), Tile("┌"), Tile("┐"), Tile("┐")],
                       [Tile("┴"), Tile("┤"), Tile("│"), Tile("┐"), Tile("┌"), Tile("┤"), Tile("├")],
                       [Tile("┌"), Tile("┬"), Tile("┘"), Tile("┐"), Tile("┤"), Tile("┘"), Tile("┤")],
                       [Tile("┬"), Tile("└"), Tile("┌"), Tile("┤"), Tile("└"), Tile("┐"), Tile("┐")],
                       [Tile("┬"), Tile("┐"), Tile("─"), Tile("┐"), Tile("┘"), Tile("┤"), Tile("┘")]])

def test_drawing():
    players = [
        Player("",
               default_board.get_board()[0][0],
               default_board.get_board()[5][5], Coordinate(0, 0), player_api=PlayerAPI(''), has_reached_goal=True),
        Player("",
               default_board.get_board()[0][0],
               default_board.get_board()[5][5], Coordinate(5, 5), player_api=PlayerAPI('')),
        Player("",
               default_board.get_board()[0][0],
               default_board.get_board()[5][5], Coordinate(2, 4), player_api=PlayerAPI(''))
    ]

    s = State(players, default_board)
    observer = Observer()
    ref = Referee(observer=observer)
    winners, kicked = ref.pickup_from_state(s)
    #assert winners[0] == players[1], "Player should have won game by win condition: reaching home"

if __name__ == '__main__':
    test_drawing() 