import unittest, os, sys
sys.path.append(os.path.join(os.path.dirname(__file__),"../"))
from referee import Referee

class TestPlayer(unittest.TestCase):
    #TODO: test bad player functions to make sure they give a result in the case there is no error
    #(i.e. they havent reached the correct number of times calling the function)