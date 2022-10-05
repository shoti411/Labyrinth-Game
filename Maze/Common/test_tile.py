import pytest
from tile import Tile

pytest.main()


def test_tile_constructor_0():
    tile = Tile('│')
    assert tile.get_path_code() == '│', 'Tile path_code doesn\'t match constructor'


def test_tile_constructor_1():
    acceptable_paths = ['│', '─', '┐', '└', '┌', '┘', '┬', '├', '┴', '┤', '┼']
    tile = Tile()
    assert tile.get_path_code() in acceptable_paths, 'Tile path_code randomized to non-acceptable string.'


def test_tile_constructor_fail():
    with pytest.raises(ValueError) as e_info:
        Tile('a')


