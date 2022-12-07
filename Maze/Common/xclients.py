import sys, os, json

sys.path.append(os.path.join(os.path.dirname(__file__), "../Players"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../Client"))

from client import Client
from player import LocalPlayerAPI, BadPlayerAPI

def xclients(in_stream):
    '''
    The stdin should contain one line representing a list of player specs
    so json_objects should always contain one list.
    '''
    json_objects = read_input(in_stream)
    connect_players(json_objects[0])

def connect_players(player_list):
    '''
    Player list will contain json player specs where the first item (p[0])
    is the name of the player.  
    The first argument on the command line will contain the port to 
    connect the client with.
    '''
    local_players = []
    for p in player_list:
        if len(p) == 3:
            local_players.append(BadPlayerAPI(p[0], p[2], 0, p[1]))
        elif (len(p) == 4):
            local_players.append(BadPlayerAPI(p[0], p[2], p[3], p[1]))
        else:
            local_players.append(LocalPlayerAPI(p[0], p[1]))
    client = Client('localhost', int(sys.argv[1]))
    client.connect_players(local_players)

def read_input(json_str):
    """
    Reads input from json_str, parses well-formed and valid json objects.

    :return: <list of Json Objects>
    """
    decoder = json.JSONDecoder()
    pos = 0
    objs = []
    while pos < len(json_str):
        json_str = json_str[pos:].strip()
        if not json_str:
            break
        obj, pos = decoder.raw_decode(json_str)
        objs.append(obj)
    return objs

xclients(sys.stdin.read())