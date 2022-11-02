import pytest
from state import State
from player_state import Player
from board import Board
from tile import Tile
from gems import Gem
from coordinate import Coordinate

# DEFAULT TESTING CONSTANTS
test_board = [[Tile('─'), Tile('─'), Tile('┐')],
              [Tile('┐'), Tile('│'), Tile('│')],
              [Tile('│'), Tile('┐'), Tile('┐')]]
board = Board(board=test_board)
extra_tile = Tile('┐')
players = [
    Player(None, test_board[0][0], test_board[1][2], Coordinate(0, 0)),
    Player(None, test_board[2][0], test_board[0][2], Coordinate(2, 0)),
]


def test_active_can_reach_tile1():
    # Check can reach
    s = State(players=players, board=board, extra_tile=extra_tile)
    assert s.active_can_reach_tile(Coordinate(1, 2)), 'Active cannot reach reachable tile'


def test_active_can_reach_tile2():
    # Check cannot reach
    s = State(players=players, board=board, extra_tile=extra_tile)
    assert not s.active_can_reach_tile(Coordinate(1, 0)), 'Active can reach non-reachable tile'


def test_active_on_goal_tile1():
    test_board = [[Tile('─'), Tile('─'), Tile('┐')],
              [Tile('┐'), Tile('│'), Tile('│')],
              [Tile('│'), Tile('┐'), Tile('┐')]]
    board = Board(board=test_board)
    extra_tile = Tile('┐')
    # Check player on goal tile
    test_players = [
        Player(None, test_board[0][0], test_board[2][2], Coordinate(2, 2)),
        Player(None, test_board[2][0], test_board[0][2], Coordinate(2, 0)),
    ]
    s = State(players=test_players, board=board, extra_tile=extra_tile)
    assert s.active_on_goal_tile(), 'Active player on goal tile wrongful false'


def test_active_on_goal_tile2():
    # DEFAULT TESTING CONSTANTS
    test_board = [[Tile('─', [Gem.ALEXANDRITE]), Tile('─', [Gem.ALEXANDRITE]), Tile('┐', [Gem.ALEXANDRITE])],
              [Tile('┐', [Gem.ALEXANDRITE]), Tile('│', [Gem.ALEXANDRITE]), Tile('│', [Gem.ALEXANDRITE])],
              [Tile('│', [Gem.ALEXANDRITE]), Tile('┐', [Gem.ALEXANDRITE]), Tile('┐', [Gem.ALEXANDRITE])]]
    board = Board(board=test_board)
    extra_tile = Tile('┐')
    players = [
        Player(None, test_board[0][0], test_board[2][2], Coordinate(0, 0)),
        Player(None, test_board[2][0], test_board[2][2], Coordinate(2, 0)),
    ]
    # Check player not on goal tile
    s = State(players=players, board=board, extra_tile=extra_tile)
    assert not s.active_on_goal_tile(), 'Active player on goal tile wrongful true'


def test_kick_active1():
    # Check kick
    s = State(players=players, board=board, extra_tile=extra_tile)
    s.kick_active()
    assert len(s.get_players()) == 1, 'Active player not kicked'


def test_kick_active2():
    # Check multiple kicks and kicked down to empty list
    s = State(players=players, board=board, extra_tile=extra_tile)
    s.kick_active()
    s.kick_active()
    assert len(s.get_players()) == 0, '2 players not kicked successfully'


def test_kick_active3():
    # Check multiple kicks and kick on empty list
    s = State(players=players, board=board, extra_tile=extra_tile)
    s.kick_active()
    s.kick_active()
    s.kick_active()
    assert len(s.get_players()) == 0, '2 players plus incorrect kick call not successful'


def test_shift1():
    # Test valid row forward shift. With player on new extra tile and player in row. 
    test_players = [
        Player(None, test_board[0][0], test_board[2][2], Coordinate(0, 0)),
        Player(None, test_board[0][2], test_board[0][2], Coordinate(0, 2)),
    ]
    s = State(players=test_players, board=board, extra_tile=extra_tile)
    s.shift(0, 1, True)
    assert s.get_players()[0].get_coordinate() == Coordinate(0, 1) and s.get_players()[1].get_coordinate() == Coordinate(0, 0), \
        'Shift row didn\'t work'


def test_shift2():
    # Test valid row backward shift. With player on new extra tile and player in row. 
    test_players = [
        Player(None, test_board[0][0], test_board[2][2], Coordinate(0, 0)),
        Player(None, test_board[0][2], test_board[0][2], Coordinate(0, 2)),
    ]
    s = State(players=test_players, board=board, extra_tile=extra_tile)
    s.shift(0, -1, True)
    assert s.get_players()[0].get_coordinate() == Coordinate(0, 2) and s.get_players()[1].get_coordinate() == Coordinate(0, 1), \
        'Shift row didn\'t work'


def test_shift3():
    # Test valid column forward shift. With player on new extra tile and player in column. 
    test_players = [
        Player(None, test_board[0][0], test_board[2][2], Coordinate(0, 0)),
        Player(None, test_board[0][2], test_board[0][2], Coordinate(2, 0)),
    ]
    s = State(players=test_players, board=board, extra_tile=extra_tile)
    s.shift(0, 1, False)
    assert s.get_players()[0].get_coordinate() == Coordinate(1, 0) and s.get_players()[1].get_coordinate() == Coordinate(0, 0), \
        'Shift col didn\'t work'


def test_shift4():
    # Test valid column backward shift. With player on new extra tile and player in column. 
    test_players = [
        Player(None, test_board[0][0], test_board[2][2], Coordinate(0, 0)),
        Player(None, test_board[0][2], test_board[0][2], Coordinate(2, 0)),
    ]
    s = State(players=test_players, board=board, extra_tile=extra_tile)
    s.shift(0, -1, False)
    assert s.get_players()[0].get_coordinate() == Coordinate(2, 0) and s.get_players()[1].get_coordinate() == Coordinate(1, 0), \
        'Shift col didn\'t work'


def test_move1():
    s = State(players=players, board=board, extra_tile=extra_tile)
    s.move_active_player(Coordinate(0,2))
    assert s.get_players()[1].get_coordinate() == Coordinate(0,2), 'Move did not work'

def test_move2():
    s = State(players=players, board=board, extra_tile=extra_tile)
    with pytest.raises(ValueError) as e_info:
        s.move_active_player(Coordinate(-1,2))

def test_move3():
    s = State(players=players, board=board, extra_tile=extra_tile)
    with pytest.raises(ValueError) as e_info:
        s.move_active_player(Coordinate(0,-1))

def test_move4():
    s = State(players=players, board=board, extra_tile=extra_tile)
    with pytest.raises(ValueError) as e_info:
        s.move_active_player(Coordinate(1,1))