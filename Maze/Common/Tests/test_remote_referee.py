import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../Remote"))
from referee import Referee
sys.path.append(os.path.join(os.path.dirname(__file__), "../Common"))
from action import Move
from coordinate import Coordinate


def test_choice_to_json():
    choice = Move(0, 1, 4, True, Coordinate(5,1))