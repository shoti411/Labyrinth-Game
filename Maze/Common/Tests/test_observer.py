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
from threading import *

default_board = Board([[Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
                       [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
                       [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
                       [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
                       [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
                       [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
                       [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()]])

observer = Observer()
ref = Referee(observer=observer)


def drawing():
    players = [
        PlayerAPI("a"),
        PlayerAPI("b"),
        PlayerAPI("c")
    ]
    ref.run(players)
    #assert winners[0] == players[1], "Player should have won game by win condition: reaching home"


if __name__ == '__main__':
    drawing() 