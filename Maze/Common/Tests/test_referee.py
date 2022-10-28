import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../../Players"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../../Referee"))

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


default_board = Board([[Tile("┘"), Tile("┤"), Tile("┼"), Tile("│"), Tile("┬"), Tile("┐"), Tile("┬")],
                       [Tile("─"), Tile("│"), Tile("│"), Tile("├"), Tile("┌"), Tile("├"), Tile("┌")],
                       [Tile("┬"), Tile("│"), Tile("┬"), Tile("┘"), Tile("┌"), Tile("┐"), Tile("┐")],
                       [Tile("┴"), Tile("┤"), Tile("│"), Tile("┐"), Tile("┌"), Tile("┤"), Tile("├")],
                       [Tile("┌"), Tile("┬"), Tile("┘"), Tile("┐"), Tile("┤"), Tile("┘"), Tile("┤")],
                       [Tile("┬"), Tile("└"), Tile("┌"), Tile("┤"), Tile("└"), Tile("┐"), Tile("┐")],
                       [Tile("┬"), Tile("┐"), Tile("─"), Tile("┐"), Tile("┘"), Tile("┤"), Tile("┘")]])


def test_win_condition():
    """ Player reaches home after reaching goal """
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
    ref = Referee()
    winners, kicked = ref.pickup_from_state(s)
    assert winners[0] == players[0], "Player should have won game by win condition: reaching home"


def test_win_condition2():
    """ Closest players to home tile -- multiple"""
    players = [
        Player("",
               default_board.get_board()[1][1],
               default_board.get_board()[0][0], Coordinate(4, 4), player_api=PlayerAPI(''), has_reached_goal=True),
        Player("",
               default_board.get_board()[0][0],
               default_board.get_board()[2][2], Coordinate(3, 3), player_api=PlayerAPI(''), has_reached_goal=True),
        Player("",
               default_board.get_board()[3][3],
               default_board.get_board()[0][0], Coordinate(0, 0), player_api=PlayerAPI(''))
    ]
    s = State(players, default_board)
    s.do_pass()
    s.do_pass()
    s.do_pass()
    ref = Referee()
    winners, kicked = ref.pickup_from_state(s)
    assert winners == [players[0], players[1]], 'Error testing if multiple players win by distance to home'

def test_win_condition3():
    """ Closest player to home tile -- only 1 """
    players = [
        Player("",
               default_board.get_board()[1][1],
               default_board.get_board()[0][0], Coordinate(5, 5), player_api=PlayerAPI(''), has_reached_goal=True),
        Player("",
               default_board.get_board()[0][0],
               default_board.get_board()[2][2], Coordinate(3, 3), player_api=PlayerAPI(''), has_reached_goal=True),
        Player("",
               default_board.get_board()[3][3],
               default_board.get_board()[0][0], Coordinate(0, 0), player_api=PlayerAPI(''))
    ]
    s = State(players, default_board)
    s.do_pass()
    s.do_pass()
    s.do_pass()
    ref = Referee()
    winners, kicked = ref.pickup_from_state(s)
    assert winners == [players[1]], 'Error testing if multiple players win by distance to home'


def test_win_condition4():
    """ Closest players to goal tile -- multiple"""
    players = [
        Player("",
               default_board.get_board()[1][1],
               default_board.get_board()[0][0], Coordinate(4, 4), player_api=PlayerAPI('')),
        Player("",
               default_board.get_board()[0][0],
               default_board.get_board()[4][4], Coordinate(3, 3), player_api=PlayerAPI('')),
        Player("",
               default_board.get_board()[3][3],
               default_board.get_board()[1][1], Coordinate(0, 0), player_api=PlayerAPI(''))
    ]
    s = State(players, default_board)
    s.do_pass()
    s.do_pass()
    s.do_pass()
    ref = Referee()
    winners, kicked = ref.pickup_from_state(s)
    assert winners == [players[1], players[2]], 'Error testing if multiple players win by distance to home'



def test_win_condition5():
    """ Closest player to goal tile -- only 1 """
    players = [
        Player("",
               default_board.get_board()[1][1],
               default_board.get_board()[0][0], Coordinate(4, 4), player_api=PlayerAPI('')),
        Player("",
               default_board.get_board()[0][0],
               default_board.get_board()[4][4], Coordinate(3, 3), player_api=PlayerAPI('')),
        Player("",
               default_board.get_board()[3][3],
               default_board.get_board()[1][1], Coordinate(3, 3), player_api=PlayerAPI(''))
    ]
    s = State(players, default_board)
    s.do_pass()
    s.do_pass()
    s.do_pass()
    ref = Referee()
    winners, kicked = ref.pickup_from_state(s)
    assert winners == [players[1]], 'Error testing if multiple players win by distance to home'


def test_game_complete1():
    """ max rounds reached """
    players = [
        Player("",
               default_board.get_board()[1][1],
               default_board.get_board()[0][0], Coordinate(4, 4), player_api=PlayerAPI('')),
        Player("",
               default_board.get_board()[0][0],
               default_board.get_board()[4][4], Coordinate(3, 3), player_api=PlayerAPI('')),
        Player("",
               default_board.get_board()[3][3],
               default_board.get_board()[1][1], Coordinate(3, 3), player_api=PlayerAPI(''))
    ]
    s = State(players, default_board, rounds=1000)
    assert s.is_game_over(1000), 'Game incomplete even though rounds finished'


def test_game_complete2():
    """ all passes """
    players = [
        Player("",
               default_board.get_board()[1][1],
               default_board.get_board()[0][0], Coordinate(4, 4), player_api=PlayerAPI('')),
        Player("",
               default_board.get_board()[0][0],
               default_board.get_board()[4][4], Coordinate(3, 3), player_api=PlayerAPI('')),
        Player("",
               default_board.get_board()[3][3],
               default_board.get_board()[1][1], Coordinate(3, 3), player_api=PlayerAPI(''))
    ]
    s = State(players, default_board)
    s.do_pass()
    s.do_pass()
    s.do_pass()
    assert s.is_game_over(1000), 'Game incomplete even though all players passed'


def test_game_complete3():
    """ all kicked """
    players = [
        Player("",
               default_board.get_board()[1][1],
               default_board.get_board()[0][0], Coordinate(4, 4), player_api=PlayerAPI('')),
        Player("",
               default_board.get_board()[0][0],
               default_board.get_board()[4][4], Coordinate(3, 3), player_api=PlayerAPI('')),
        Player("",
               default_board.get_board()[3][3],
               default_board.get_board()[1][1], Coordinate(3, 3), player_api=PlayerAPI(''))
    ]
    s = State(players, default_board)
    s.kick_active()
    s.kick_active()
    s.kick_active()
    assert s.is_game_over(1000), 'Game incomplete even though all players kicked'


def test_game_complete4():
    """ game won """
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
    assert s.is_game_over(1000), 'Game incomplete even though player won'


