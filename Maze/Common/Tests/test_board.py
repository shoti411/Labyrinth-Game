import pytest
from board import Board
from tile import Tile

def test_board_constructor():
    test_board = [[Tile('┴'), Tile('┤')], [Tile('┤'), Tile('┼')]]
    board = Board(board=test_board)
    assert board.get_board() == test_board, 'Board does not match provided board in constructor.'

def test_board_constructor_2():
    # Test invalid Tile
    test_board = [[5, Tile('┤')], [Tile('┤'), Tile('┼')]]
    with pytest.raises(ValueError) as e_info:
        board = Board(board=test_board)

def test_board_constructor_3():
    # Test empty board
    test_board = []
    with pytest.raises(ValueError) as e_info:
        board = Board(board=test_board)

def test_board_constructor_4():
    # Test invalid row lengths
    test_board = [[Tile('┴')], [Tile('┤'), Tile('┼')]]
    with pytest.raises(ValueError) as e_info:
        board = Board(board=test_board)

def test_board_constructor_5():
    # Test invalid object for board 
    test_board = ('Ace of spades', '2 of diamonds')
    with pytest.raises(ValueError) as e_info:
        board = Board(board=test_board)

def test_board_shift_row():
    # Test right row shift
    test_tile_1 = Tile('│')
    test_tile_2 = Tile('─')
    test_tile_3 = Tile('┐')
    test_board = [[test_tile_1, test_tile_2, test_tile_3],
                  [Tile('┐'), Tile('│'), Tile('─')],
                  [Tile('│'), Tile('┐'), Tile('┐')]]
    test_extra_tile = Tile('┐')
    board = Board(board=test_board)
    actual_extra_tile = board.shift_row(0, 1, test_extra_tile)
    assert board.get_board()[0] == [test_extra_tile, test_tile_1, test_tile_2] and actual_extra_tile == test_tile_3, \
        "Basic right shift row failed."

def test_board_shift_row2():
    # Test left row shift
    test_tile_1 = Tile('│')
    test_tile_2 = Tile('─')
    test_tile_3 = Tile('┐')
    test_board = [[test_tile_1, test_tile_2, test_tile_3],
                  [Tile('┐'), Tile('│'), Tile('─')],
                  [Tile('│'), Tile('┐'), Tile('┐')]]
    test_extra_tile = Tile('┐')
    board = Board(board=test_board)
    actual_extra_tile = board.shift_row(0, -1, test_extra_tile)
    assert board.get_board()[0] == [test_tile_2, test_tile_3, test_extra_tile] and actual_extra_tile == test_tile_1, \
        "Basic left shift row failed."


def test_board_shift_row3():
    # Test negative invalid index
    test_board = [[Tile('│'), Tile('─'), Tile('┐')],
                  [Tile('┐'), Tile('│'), Tile('─')],
                  [Tile('│'), Tile('┐'), Tile('┐')]]
    test_extra_tile = Tile('┐')
    board = Board(board=test_board)
    with pytest.raises(IndexError) as e_info:
        board.shift_row(-1, -1, test_extra_tile)


def test_board_shift_row4():
    # Test higher invalid index
    test_board = [[Tile('│'), Tile('─'), Tile('┐')],
                  [Tile('┐'), Tile('│'), Tile('─')],
                  [Tile('│'), Tile('┐'), Tile('┐')]]
    test_extra_tile = Tile('┐')
    board = Board(board=test_board)
    with pytest.raises(IndexError) as e_info:
        board.shift_row(3, -1, test_extra_tile)


def test_board_shift_row5():
    # Test invalid direction
    test_board = [[Tile('│'), Tile('─'), Tile('┐')],
                  [Tile('┐'), Tile('│'), Tile('─')],
                  [Tile('│'), Tile('┐'), Tile('┐')]]
    test_extra_tile = Tile('┐')
    board = Board(board=test_board)
    with pytest.raises(ValueError) as e_info:
        board.shift_row(2, 0, test_extra_tile)


def test_board_shift_row6():
    # Test invalid row index
    test_board = [[Tile('│'), Tile('─'), Tile('┐')],
                  [Tile('┐'), Tile('│'), Tile('─')],
                  [Tile('│'), Tile('┐'), Tile('┐')]]
    test_extra_tile = Tile('┐')
    board = Board(board=test_board)
    with pytest.raises(IndexError) as e_info:
        board.shift_row(1, 1, test_extra_tile)


def test_board_shift_col():
    # Test downward column shift
    test_tile_1 = Tile('│')
    test_tile_2 = Tile('┐')
    test_tile_3 = Tile('│')
    test_extra_tile = Tile('┐')
    test_board = [[test_tile_1, test_tile_1, test_tile_1],
                  [test_tile_2, test_tile_1, test_tile_1],
                  [test_tile_3, test_tile_1, test_tile_1]]
    shifted_board = [[test_extra_tile, test_tile_1, test_tile_1],
                     [test_tile_1, test_tile_1, test_tile_1],
                     [test_tile_2, test_tile_1, test_tile_1]]
    board = Board(board=test_board)
    actual_extra_tile = board.shift_column(0, 1, test_extra_tile)
    assert board.get_board() == shifted_board and actual_extra_tile == test_tile_3, \
        "Basic down shift column failed."


def test_board_shift_col2():
    # Test upward column shift
    test_tile_1 = Tile('│')
    test_tile_2 = Tile('┐')
    test_tile_3 = Tile('│')
    test_extra_tile = Tile('┐')
    test_board = [[test_tile_1, test_tile_1, test_tile_1],
                  [test_tile_2, test_tile_1, test_tile_1],
                  [test_tile_3, test_tile_1, test_tile_1]]
    shifted_board = [[test_tile_2, test_tile_1, test_tile_1],
                     [test_tile_3, test_tile_1, test_tile_1],
                     [test_extra_tile, test_tile_1, test_tile_1]]
    board = Board(board=test_board)
    actual_extra_tile = board.shift_column(0, -1, test_extra_tile)
    assert board.get_board() == shifted_board and actual_extra_tile == test_tile_1, \
        "Basic down shift column failed."


def test_board_shift_col3():
    # Test negative invalid index
    test_board = [[Tile('│'), Tile('─'), Tile('┐')],
                  [Tile('┐'), Tile('│'), Tile('─')],
                  [Tile('│'), Tile('┐'), Tile('┐')]]
    test_extra_tile = Tile('┐')
    board = Board(board=test_board)
    with pytest.raises(IndexError) as e_info:
        board.shift_column(-1, -1, test_extra_tile)


def test_board_shift_col4():
    # Test high invalid index
    test_board = [[Tile('│'), Tile('─'), Tile('┐')],
                  [Tile('┐'), Tile('│'), Tile('─')],
                  [Tile('│'), Tile('┐'), Tile('┐')]]
    test_extra_tile = Tile('┐')
    board = Board(board=test_board)
    with pytest.raises(IndexError) as e_info:
        board.shift_column(3, -1, test_extra_tile)


def test_board_shift_col5():
    # Test invalid direction
    test_board = [[Tile('│'), Tile('─'), Tile('┐')],
                  [Tile('┐'), Tile('│'), Tile('─')],
                  [Tile('│'), Tile('┐'), Tile('┐')]]
    test_extra_tile = Tile('┐')
    board = Board(board=test_board)
    with pytest.raises(ValueError) as e_info:
        board.shift_column(2, 0, test_extra_tile)


def test_board_shift_col6():
    # Test invalid row index
    test_board = [[Tile('│'), Tile('─'), Tile('┐')],
                  [Tile('┐'), Tile('│'), Tile('─')],
                  [Tile('│'), Tile('┐'), Tile('┐')]]
    test_extra_tile = Tile('┐')
    board = Board(board=test_board)
    with pytest.raises(IndexError) as e_info:
        board.shift_column(1, 1, test_extra_tile)


def test_board_get_reachable0():
    # Basic functionality
    test_board = [[Tile('┌'), Tile('─'), Tile('┐')],
                  [Tile('│'), Tile('│'), Tile('│')],
                  [Tile('│'), Tile('┐'), Tile('┐')]]
    board = Board(board=test_board)
    test_list = board.get_reachable_tiles(0, 0)
    print(test_list)
    compare_list = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0)]
    assert all([x in test_list for x in compare_list] + [x in compare_list for x in test_list]), \
        'Basic reachable functionality failed.'


def test_board_get_reachable1():
    # All reachable
    test_board = [[Tile('┼'), Tile('┼'), Tile('┼')],
                  [Tile('┼'), Tile('┼'), Tile('┼')],
                  [Tile('┼'), Tile('┼'), Tile('┼')]]
    board = Board(board=test_board)
    test_list = board.get_reachable_tiles(0, 0)
    compare_list = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    assert all([x in test_list for x in compare_list] + [x in compare_list for x in test_list]), \
        'Basic reachable functionality failed.'


def test_board_get_reachable2():
    # None reachable
    test_board = [[Tile('│'), Tile('─'), Tile('│')],
                  [Tile('─'), Tile('│'), Tile('─')],
                  [Tile('│'), Tile('─'), Tile('│')]]
    board = Board(board=test_board)
    test_list = board.get_reachable_tiles(0, 0)
    assert test_list == [(0, 0)], \
        'Basic reachable functionality failed.'


def test_board_get_reachable3():
    # Test negative invalid x 
    test_board = [[Tile('│'), Tile('─'), Tile('│')],
                  [Tile('─'), Tile('│'), Tile('─')],
                  [Tile('│'), Tile('─'), Tile('│')]]
    board = Board(board=test_board)
    with pytest.raises(ValueError) as e_info:
        test_list = board.get_reachable_tiles(-1, 0)


def test_board_get_reachable4():
    # Test negatove invalid y
    test_board = [[Tile('│'), Tile('─'), Tile('│')],
                  [Tile('─'), Tile('│'), Tile('─')],
                  [Tile('│'), Tile('─'), Tile('│')]]
    board = Board(board=test_board)
    with pytest.raises(ValueError) as e_info:
        test_list = board.get_reachable_tiles(0, -1)


def test_board_get_reachable5():
    # Test too large invalid x
    test_board = [[Tile('│'), Tile('─'), Tile('│')],
                  [Tile('─'), Tile('│'), Tile('─')],
                  [Tile('│'), Tile('─'), Tile('│')]]
    board = Board(board=test_board)
    with pytest.raises(ValueError) as e_info:
        test_list = board.get_reachable_tiles(3, 0)


def test_board_get_reachable6():
    # Test too large invalid y
    test_board = [[Tile('│'), Tile('─'), Tile('│')],
                  [Tile('─'), Tile('│'), Tile('─')],
                  [Tile('│'), Tile('─'), Tile('│')]]
    board = Board(board=test_board)
    with pytest.raises(ValueError) as e_info:
        test_list = board.get_reachable_tiles(0, 3)

