import pytest
from state import State
from player_state import Player
from board import Board
from tile import Tile
from riemann import Riemann
from coordinate import Coordinate
from player_game_state import PlayerGameState
from action import Pass

test_board = [[Tile('─'), Tile('─'), Tile('│')],
              [Tile('└'), Tile('─'), Tile('┐')],
              [Tile('┐'), Tile('─'), Tile('┐')]]
board = Board(board=test_board)
extra_tile = Tile('┐')
player = Player(None, test_board[0][0], test_board[0][2], Coordinate(0, 0))
player_state = PlayerGameState(board, extra_tile, player, Pass())
riemann_strategy = Riemann()

def test_check_degrees1():
    re = riemann_strategy.check_degrees(Coordinate(0, 2), player_state, 2, 1, False)
    assert re == 0, 'Cannot find correct degree'

def test_check_degrees2():
    extra_tile = Tile('└')
    player_state = PlayerGameState(board, extra_tile, player, Pass())
    re = riemann_strategy.check_degrees(Coordinate(1, 1), player_state, 0, 1, True)
    assert re == 270, 'Cannot find correct degree'

def test_check_degrees3():
    extra_tile = Tile('│')
    player_state = PlayerGameState(board, extra_tile, player, Pass())
    re = riemann_strategy.check_degrees(Coordinate(0, 2), player_state, 2, 1, False)
    assert re == -1, 'Found degree when one doesn\'t exist'

def test_check_direction1():
    re = riemann_strategy.check_direction(Coordinate(0, 2), player_state, 2, False)
    assert re == (0, 1), 'Cannot find correct degree and direction'

def test_check_direction2():
    re = riemann_strategy.check_direction(Coordinate(1, 1), player_state, 0, True)
    assert re == (90, 1), 'Cannot find correct degree and direction'

def test_check_direction3():
    re = riemann_strategy.check_direction(Coordinate(1, 1), player_state, 2, True)
    assert re == -1, 'Found degree and direction that doesnt exist'

def test_check_row_shift1():
    re = riemann_strategy.check_row_shift(Coordinate(1, 1), player_state)
    assert re == (90, 1, 0, True), 'Cannot find correct degree, direction, index and isrow'

def test_check_row_shift2():
    re = riemann_strategy.check_row_shift(Coordinate(2, 2), player_state)
    assert re == (-1), 'Found degree, direction, index and isrow when it doesnt exist'

def test_check_col_shift1():
    re = riemann_strategy.check_col_shift(Coordinate(0, 2), player_state)
    assert re == (0, 1, 2, False), 'Cannot find correct degree, direction, index and isrow'

def test_check_col_shift2():
    test_board = [[Tile('─'), Tile('│'), Tile('│')],
                [Tile('└'), Tile('│'), Tile('┐')],
                [Tile('┐'), Tile('│'), Tile('┐')]]
    player = Player(None, test_board[0][0], test_board[0][2], Coordinate(2, 2))
    player_state = PlayerGameState(Board(board=test_board), extra_tile, player, Pass())
    re = riemann_strategy.check_col_shift(Coordinate(1, 2), player_state)
    assert re == -1, 'Found degree, direction, index and isrow when it doesnt exist'

def test_slide_and_insert1():
    re = riemann_strategy.slide_and_insert(player_state)
    assert re == (0, 1, 2, False), 'Cannot find goal tile'

def test_slide_and_insert2():
    test_board = [[Tile('─'), Tile('│'), Tile('└')],
                [Tile('│'), Tile('│'), Tile('│')],
                [Tile('┐'), Tile('│'), Tile('┐')]]
    player = Player(None, test_board[0][0], test_board[0][2], Coordinate(1, 1))
    player_state = PlayerGameState(Board(board=test_board), extra_tile, player, Pass())
    re = riemann_strategy.slide_and_insert(player_state)
    assert re == (0, -1, 2, True), 'Did not find top-most left-most tile'

def test_slide_and_insert2():
    test_board = [[Tile('│'), Tile('│'), Tile('│')],
                [Tile('│'), Tile('─'), Tile('│')],
                [Tile('│'), Tile('│'), Tile('│')]]
    player = Player(None, test_board[0][0], test_board[0][2], Coordinate(1, 1))
    player_state = PlayerGameState(Board(board=test_board), extra_tile, player, Pass())
    re = riemann_strategy.slide_and_insert(player_state)
    assert re == -1, 'Found an unreachable tile'

def test_move1():
    test_board = [[Tile('─'), Tile('─'), Tile('─')],
              [Tile('└'), Tile('─'), Tile('┐')],
              [Tile('┐'), Tile('─'), Tile('┐')]]
    board = Board(board=test_board)
    player = Player(None, test_board[0][0], test_board[0][2], Coordinate(0, 0))
    player_state = PlayerGameState(Board(board=test_board), extra_tile, player, Pass())
    re = riemann_strategy.move(player_state)
    assert re == Coordinate(0, 2), 'Did not move to goal tile'

def test_move2():
    test_board = [[Tile('─'), Tile('─'), Tile('─')],
              [Tile('└'), Tile('─'), Tile('┐')],
              [Tile('┐'), Tile('─'), Tile('┐')]]
    board = Board(board=test_board)
    player = Player(None, test_board[0][0], test_board[1][2], Coordinate(0, 1))
    player_state = PlayerGameState(Board(board=test_board), extra_tile, player, Pass())
    re = riemann_strategy.move(player_state)
    assert re == Coordinate(0, 0), 'Did not move to top-most left-most tile'

def test_move3():
    test_board = [[Tile('│'), Tile('│'), Tile('│')],
                [Tile('│'), Tile('─'), Tile('│')],
                [Tile('│'), Tile('│'), Tile('│')]]
    board = Board(board=test_board)
    player = Player(None, test_board[0][0], test_board[1][2], Coordinate(1, 1))
    player_state = PlayerGameState(Board(board=test_board), extra_tile, player, Pass())
    re = riemann_strategy.move(player_state)
    assert re == -1, 'Found unreachable tile'


    

