import sys
import os
import socket
import threading
import random

sys.path.append(os.path.join(os.path.dirname(__file__), "../Player"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../Client"))

from client import Client
from player import LocalPlayerAPI

player1 = LocalPlayerAPI('tom')
player2 = LocalPlayerAPI('shaun')
player3 = LocalPlayerAPI('player3')
player4 = LocalPlayerAPI('player4')
player5 = LocalPlayerAPI('player5')
player6 = LocalPlayerAPI('player6')

client = Client('localhost', 888)
client.connect_players([player1, player2, player3, player4, player5, player6])
