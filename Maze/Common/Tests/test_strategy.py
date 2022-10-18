import pytest
from state import State
from player import Player
from board import Board
from tile import Tile
from gems import Gem
from strategy import Strategy

test_board = [[Tile('─'), Tile('─')],
              [Tile('┐'), Tile('│')]]
board = Board(board=test_board)
extra_tile = Tile('┐')
players = [
    Player(None, test_board[0][0], test_board[1][1], (0, 0)),
    Player(None, test_board[1][0], test_board[0][1], (2, 0)),
]

def test_check_degrees1():
    # check if goal tile reachable
    ...