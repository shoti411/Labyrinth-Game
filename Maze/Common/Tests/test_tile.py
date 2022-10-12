import pytest
from tile import Tile
from directions import Direction


def test_tile_constructor_0():
    # Test default constructor works and that get_path_code works.
    tile = Tile('│')
    assert tile.get_path_code() == '│', 'Tile path_code doesn\'t match constructor'


def test_tile_constructor_1():
    # Test random constructor 
    acceptable_paths = ['│', '─', '┐', '└', '┌', '┘', '┬', '├', '┴', '┤', '┼']
    tile = Tile()
    assert tile.get_path_code() in acceptable_paths, 'Tile path_code randomized to non-acceptable string.'


def test_tile_constructor_fail():
    # Test invalid string constructor
    with pytest.raises(ValueError) as e_info:
        Tile('a')

def test_get_paths():
    # Test all paths
    tile = Tile('┼')
    assert tile.get_paths() == [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT], 'Tile get path does not return the expect directions.'

def test_get_paths():
    # Test some paths
    tile = Tile('┐')
    assert tile.get_paths() == [Direction.DOWN, Direction.LEFT], 'Tile get path does not return the expect directions.'


def test_rotate1():
    tile = Tile('│')
    tile.rotate(90)
    assert tile.get_path_code() == '─', 'Rotate functionality doesn\'t work'


def test_rotate2():
    tile = Tile('┐')
    tile.rotate(270)
    assert tile.get_path_code() == '┘', 'Rotate functionality doesn\'t work'


def test_rotate3():
    tile = Tile('┬')
    tile.rotate(180)
    assert tile.get_path_code() == '┴', 'Rotate functionality doesn\'t work'


def test_rotate4():
    tile = Tile('┼')
    tile.rotate(360)
    assert tile.get_path_code() == '┼', 'Rotate functionality doesn\'t work'


def test_rotate5():
    tile = Tile('┼')
    tile.rotate(-270)
    assert tile.get_path_code() == '┼', 'Rotate functionality doesn\'t work'


def test_rotate6():
    tile = Tile('┬')
    with pytest.raises(ValueError) as e_info:
        tile.rotate(5)


def test_rotate7():
    tile = Tile('┐')
    tile.rotate(0)
    assert tile.get_path_code() == '┐', 'Rotate functionality doesn\'t work'

