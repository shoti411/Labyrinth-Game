import pytest
from board import Board
from tile import Tile

pytest.main()


def test_board_constructor_0():
    board = Board(rows=8, cols=4)
    assert len(board.get_board()) == 8 and len(board.get_board()[0]) == 4, 'Board size doesn\'t match constructor'


def test_board_constructor_1():
    test_board = [[Tile('┴'), Tile('┤')], [Tile('┤'), Tile('┼')]]
    board = Board(board=test_board)
    assert board.get_board() == test_board, 'Board does not match provided board in constructor.'


def test_board_constructor_2():
    extra_tile = Tile()
    board = Board(extra_tile=extra_tile)
    assert board.get_extra_tile() == extra_tile, \
        'Extra tile does not match provided extra tile in constructor.'


def test_board_constructor_3():
    board = Board(rows=0, cols=4)
    assert board.get_board() == [], 'Board size doesn\'t match constructor'


def test_board_constructor_4():
    board = Board(rows=10, cols=0)
    assert board.get_board() == [], 'Board size doesn\'t match constructor'


def test_board_constructor_5():
    with pytest.raises(ValueError) as e_info:
        Board(rows=1, cols=-1)


def test_board_constructor_6():
    with pytest.raises(ValueError) as e_info:
        Board(rows=-1, cols=1)


def test_board_shift_row():
    test_board = [[Tile('│'), Tile('─'), Tile('┐')],
                  [Tile('┐'), Tile('│'), Tile('─')],
                  [Tile('│'), Tile('┐'), Tile('┐')]]
    test_extra_tile = Tile('┐')
    board = Board(board=test_board, extra_tile=test_extra_tile)
    board.shift_row(0, 1)
    assert board.get_board()[0] == [Tile('┐'), Tile('│'), Tile('─')] and board.get_extra_tile() == Tile('┐'), \
        "Basic right shift row failed."


def test_board_shift_row2():
    test_board = [[Tile('│'), Tile('─'), Tile('┐')],
                  [Tile('┐'), Tile('│'), Tile('─')],
                  [Tile('│'), Tile('┐'), Tile('┐')]]
    test_extra_tile = Tile('┐')
    board = Board(board=test_board, extra_tile=test_extra_tile)
    board.shift_row(0, -1)
    assert board.get_board()[0] == [Tile('─'), Tile('┐'), Tile('┐')] and board.get_extra_tile() == Tile('│'), \
        "Basic left shift row failed."


def test_board_shift_row3():
    test_board = [[Tile('│'), Tile('─'), Tile('┐')],
                  [Tile('┐'), Tile('│'), Tile('─')],
                  [Tile('│'), Tile('┐'), Tile('┐')]]
    test_extra_tile = Tile('┐')
    board = Board(board=test_board, extra_tile=test_extra_tile)
    with pytest.raises(IndexError) as e_info:
        board.shift_row(-1, -1)


def test_board_shift_row4():
    test_board = [[Tile('│'), Tile('─'), Tile('┐')],
                  [Tile('┐'), Tile('│'), Tile('─')],
                  [Tile('│'), Tile('┐'), Tile('┐')]]
    test_extra_tile = Tile('┐')
    board = Board(board=test_board, extra_tile=test_extra_tile)
    with pytest.raises(IndexError) as e_info:
        board.shift_row(3, -1)


def test_board_shift_row5():
    test_board = [[Tile('│'), Tile('─'), Tile('┐')],
                  [Tile('┐'), Tile('│'), Tile('─')],
                  [Tile('│'), Tile('┐'), Tile('┐')]]
    test_extra_tile = Tile('┐')
    board = Board(board=test_board, extra_tile=test_extra_tile)
    with pytest.raises(ValueError) as e_info:
        board.shift_row(1, 0)


def test_board_shift_col():
    test_board = [[Tile('│'), Tile('─'), Tile('┐')],
                  [Tile('┐'), Tile('│'), Tile('─')],
                  [Tile('│'), Tile('┐'), Tile('┐')]]
    shifted_board = [[Tile('┐'), Tile('─'), Tile('┐')],
                     [Tile('│'), Tile('│'), Tile('─')],
                     [Tile('┐'), Tile('┐'), Tile('┐')]]
    test_extra_tile = Tile('┐')
    board = Board(board=test_board, extra_tile=test_extra_tile)
    board.shift_column(0, 1)
    assert board.get_board() == shifted_board and board.get_extra_tile() == Tile('│'), \
        "Basic down shift column failed."


def test_board_shift_col2():
    test_board = [[Tile('│'), Tile('─'), Tile('┐')],
                  [Tile('┐'), Tile('│'), Tile('─')],
                  [Tile('┐'), Tile('┐'), Tile('┐')]]
    shifted_board = [[Tile('┐'), Tile('─'), Tile('┐')],
                     [Tile('┐'), Tile('│'), Tile('─')],
                     [Tile('┐'), Tile('┐'), Tile('┐')]]
    test_extra_tile = Tile('┐')
    board = Board(board=test_board, extra_tile=test_extra_tile)
    board.shift_column(0, -1)
    assert board.get_board() == shifted_board and board.get_extra_tile() == Tile('│'), \
        "Basic down shift column failed."


def test_board_shift_col3():
    test_board = [[Tile('│'), Tile('─'), Tile('┐')],
                  [Tile('┐'), Tile('│'), Tile('─')],
                  [Tile('│'), Tile('┐'), Tile('┐')]]
    test_extra_tile = Tile('┐')
    board = Board(board=test_board, extra_tile=test_extra_tile)
    with pytest.raises(IndexError) as e_info:
        board.shift_column(-1, -1)


def test_board_shift_col4():
    test_board = [[Tile('│'), Tile('─'), Tile('┐')],
                  [Tile('┐'), Tile('│'), Tile('─')],
                  [Tile('│'), Tile('┐'), Tile('┐')]]
    test_extra_tile = Tile('┐')
    board = Board(board=test_board, extra_tile=test_extra_tile)
    with pytest.raises(IndexError) as e_info:
        board.shift_column(3, -1)


def test_board_shift_col5():
    test_board = [[Tile('│'), Tile('─'), Tile('┐')],
                  [Tile('┐'), Tile('│'), Tile('─')],
                  [Tile('│'), Tile('┐'), Tile('┐')]]
    test_extra_tile = Tile('┐')
    board = Board(board=test_board, extra_tile=test_extra_tile)
    with pytest.raises(ValueError) as e_info:
        board.shift_column(1, 0)


def test_board_get_reachable0():
    test_board = [[Tile('┌'), Tile('─'), Tile('┐')],
                  [Tile('│'), Tile('│'), Tile('│')],
                  [Tile('│'), Tile('┐'), Tile('┐')]]
    board = Board(board=test_board)
    test_list = board.get_reachable_tiles(0, 0)
    compare_list = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0)]
    assert all([x in test_list for x in compare_list] + [x in compare_list for x in test_list]), \
        'Basic reachable functionality failed.'


def test_board_get_reachable1():
    test_board = [[Tile('┼'), Tile('┼'), Tile('┼')],
                  [Tile('┼'), Tile('┼'), Tile('┼')],
                  [Tile('┼'), Tile('┼'), Tile('┼')]]
    board = Board(board=test_board)
    test_list = board.get_reachable_tiles(0, 0)
    compare_list = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    assert all([x in test_list for x in compare_list] + [x in compare_list for x in test_list]), \
        'Basic reachable functionality failed.'


def test_board_get_reachable2():
    test_board = [[Tile('│'), Tile('─'), Tile('│')],
                  [Tile('─'), Tile('│'), Tile('─')],
                  [Tile('│'), Tile('─'), Tile('│')]]
    board = Board(board=test_board)
    test_list = board.get_reachable_tiles(0, 0)
    assert test_list == [(0, 0)], \
        'Basic reachable functionality failed.'


def test_board_get_reachable3():
    test_board = [[Tile('│'), Tile('─'), Tile('│')],
                  [Tile('─'), Tile('│'), Tile('─')],
                  [Tile('│'), Tile('─'), Tile('│')]]
    board = Board(board=test_board)
    with pytest.raises(ValueError) as e_info:
        test_list = board.get_reachable_tiles(-1, 0)


def test_board_get_reachable4():
    test_board = [[Tile('│'), Tile('─'), Tile('│')],
                  [Tile('─'), Tile('│'), Tile('─')],
                  [Tile('│'), Tile('─'), Tile('│')]]
    board = Board(board=test_board)
    with pytest.raises(ValueError) as e_info:
        test_list = board.get_reachable_tiles(0, -1)


def test_board_get_reachable5():
    test_board = [[Tile('│'), Tile('─'), Tile('│')],
                  [Tile('─'), Tile('│'), Tile('─')],
                  [Tile('│'), Tile('─'), Tile('│')]]
    board = Board(board=test_board)
    with pytest.raises(ValueError) as e_info:
        test_list = board.get_reachable_tiles(3, 0)


def test_board_get_reachable6():
    test_board = [[Tile('│'), Tile('─'), Tile('│')],
                  [Tile('─'), Tile('│'), Tile('─')],
                  [Tile('│'), Tile('─'), Tile('│')]]
    board = Board(board=test_board)
    with pytest.raises(ValueError) as e_info:
        test_list = board.get_reachable_tiles(0, 3)

