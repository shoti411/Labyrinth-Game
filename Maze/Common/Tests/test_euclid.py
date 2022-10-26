import pytest
from state import State
from player_state import Player
from board import Board
from tile import Tile
from euclid import Euclid

test_board = [[Tile('─'), Tile('─'), Tile('│')],
              [Tile('└'), Tile('─'), Tile('┐')],
              [Tile('┐'), Tile('─'), Tile('┐')]]
board = Board(board=test_board)
extra_tile = Tile('┐')
player = Player(None, test_board[0][0], test_board[0][2], (0, 0))
euclid_strategy = Euclid()

def test_check_degrees1():
    re = euclid_strategy.check_degrees(0, 2, player, board, extra_tile, 2, 1, False)
    assert re == 0, 'Cannot find correct degree'

def test_check_degrees2():
    extra_tile = Tile('└')
    re = euclid_strategy.check_degrees(1, 1, player, board, extra_tile, 0, 1, True)
    assert re == 270, 'Cannot find correct degree'

def test_check_degrees3():
    extra_tile = Tile('│')
    re = euclid_strategy.check_degrees(0, 2, player, board, extra_tile, 2, 1, False)
    assert re == -1, 'Found degree when one doesn\'t exist'

def test_check_direction1():
    re = euclid_strategy.check_direction(0, 2, player, board, extra_tile, 2, False)
    assert re == (0, 1), 'Cannot find correct degree and direction'

def test_check_direction2():
    re = euclid_strategy.check_direction(1, 1, player, board, extra_tile, 0, True)
    assert re == (90, 1), 'Cannot find correct degree and direction'

def test_check_direction3():
    re = euclid_strategy.check_direction(1, 1, player, board, extra_tile, 2, True)
    assert re == -1, 'Found degree and direction that doesnt exist'

def test_check_row_shift1():
    re = euclid_strategy.check_row_shift(1, 1, player, board, extra_tile)
    assert re == (90, 1, 0, True), 'Cannot find correct degree, direction, index and isrow'

def test_check_row_shift2():
    re = euclid_strategy.check_row_shift(2, 2, player, board, extra_tile)
    assert re == (-1), 'Found degree, direction, index and isrow when it doesnt exist'

def test_check_col_shift1():
    re = euclid_strategy.check_col_shift(0, 2, player, board, extra_tile)
    assert re == (0, 1, 2, False), 'Cannot find correct degree, direction, index and isrow'

def test_check_col_shift2():
    test_board = [[Tile('─'), Tile('│'), Tile('│')],
                [Tile('└'), Tile('│'), Tile('┐')],
                [Tile('┐'), Tile('│'), Tile('┐')]]
    player = Player(None, test_board[0][0], test_board[0][2], (2, 2))
    re = euclid_strategy.check_col_shift(1, 2, player, Board(board=test_board), extra_tile)
    assert re == -1, 'Found degree, direction, index and isrow when it doesnt exist'

def test_slide_and_insert1():
    re = euclid_strategy.slide_and_insert(board, extra_tile, player)
    assert re == (0, 1, 2, False), 'Cannot find goal tile'

def test_slide_and_insert2():
    test_board = [[Tile('─'), Tile('│'), Tile('└')],
                [Tile('│'), Tile('│'), Tile('│')],
                [Tile('┐'), Tile('│'), Tile('┐')]]
    player = Player(None, test_board[0][0], test_board[0][2], (1, 1))
    re = euclid_strategy.slide_and_insert(Board(board=test_board), extra_tile, player)
    assert re == (0, -1, 2, True), 'Did not find euclid tile'

def test_slide_and_insert2():
    test_board = [[Tile('│'), Tile('│'), Tile('│')],
                [Tile('│'), Tile('─'), Tile('│')],
                [Tile('│'), Tile('│'), Tile('│')]]
    player = Player(None, test_board[0][0], test_board[0][2], (1, 1))
    re = euclid_strategy.slide_and_insert(Board(board=test_board), extra_tile, player)
    assert re == -1, 'Found an unreachable tile'

def test_move1():
    test_board = [[Tile('─'), Tile('─'), Tile('─')],
              [Tile('└'), Tile('─'), Tile('┐')],
              [Tile('┐'), Tile('─'), Tile('┐')]]
    board = Board(board=test_board)
    player = Player(None, test_board[0][0], test_board[0][2], (0, 0))
    re = euclid_strategy.move(board, player)
    assert re == (0, 2), 'Did not move to goal tile'

def test_move2():
    test_board = [[Tile('─'), Tile('─'), Tile('─')],
              [Tile('└'), Tile('─'), Tile('┐')],
              [Tile('┐'), Tile('─'), Tile('┐')]]
    board = Board(board=test_board)
    player = Player(None, test_board[0][0], test_board[1][2], (0, 1))
    re = euclid_strategy.move(board, player)
    assert re == (0, 2), 'Did not move to the closest goal tile'

def test_move3():
    test_board = [[Tile('│'), Tile('│'), Tile('│')],
                [Tile('│'), Tile('─'), Tile('│')],
                [Tile('│'), Tile('│'), Tile('│')]]
    board = Board(board=test_board)
    player = Player(None, test_board[0][0], test_board[1][2], (1, 1))
    re = euclid_strategy.move(board, player)
    assert re == -1, 'Found unreachable tile'


    

