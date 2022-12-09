import unittest, os, sys
sys.path.append(os.path.join(os.path.dirname(__file__),"../"))
from referee import Referee

class TestReferee(unittest.TestCase):
    def test_do_round_with_pass(self):
        #TODO figure out how to ensure do round will be given a pass and make sure it does not break
        pass