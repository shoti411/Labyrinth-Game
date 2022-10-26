from state import State
from player import PlayerAPI
from player_state import Player
from board import Board
from tile import Tile
import random
import copy
import itertools

class Referee:

    rows, cols = 7, 7
    rounds = 1000
    """
    TODO: strategy needs to be able to travel home
    TODO: enforce movable columns/rows
    TODO: state probably needs distance to goal

    TODO: run 1 game to completion
        - return winning players and those who misbehaved
        - end conditions:
            - player reaches home tile after reaching goal tile
            - all active players opt to pass
            - 1000 rounds
        - win conditions:
            - player(s) with shortest Euclidean distance to home tile
            after reaching goal tile
            - if no one has reached a goal tile, then it is the player(s)
            who are closest to their goal tile.

    TODO: interface that accepts game state, runs the game
        to completion from this state


    Two different teams may produce the player mechanism and the referee. Indeed, the plan calls for players from
    people that nobody knows. It is therefore imperative to consider failure modes and to have the referee react to
    failures in players.
        - When such “foreign” players misbehave, the referee immediately stops interacting with them
            so that they don’t bring down the system.
        #TODO: define misbehavior

    State what kind of abnormal interactions that referee takes care of now and what kind are left to the project
    phase that adds in remote communication.

    """

    def pickup_from_state(self, state):
        if not isinstance(state, State):
            raise ValueError('state must be an instance of class State')
        return self.__run_game(state)

    def run(self, players):
        starting_players = copy.deepcopy(players)
        board = self.__initialize_board(players)
        if len(players) == 0:
            return [], starting_players
        extra_tile = Tile()
        player_states, goal_positions = self.__initialize_players(board, len(players))
        self.__setup_players(players, board, extra_tile, player_states, goal_positions)
        state = State(board=board, extra_tile=extra_tile, players=player_states)
        return self.__run_game(state)

    def __initialize_board(self, players):
        proposed_boards = []
        kicked_players = []
        for player in players:
            try:
                proposed_board = Board(player.proposeBoard(self.rows, self.cols))
                proposed_boards.append(proposed_board)
            except ValueError:
                kicked_players.append(player)
                continue
        [players.remove(x) for x in kicked_players]
        game_board = random.choice(proposed_boards)
        return game_board

    def __initialize_players(self, board, num_players):
        players = []
        board_length = len(board)
        valid_goal_tiles = list(itertools.product(range(board_length, step=2), range(board_length, step=2)))
        for player in range(num_players):
            home_posn = random.choice(valid_goal_tiles)
            valid_goal_tiles.remove(home_posn)
            home_tile = board[home_posn[0]][home_posn[1]]

            goal_posn = random.choice(valid_goal_tiles)
            valid_goal_tiles.remove(goal_posn)
            goal_tile = board[goal_posn[0]][goal_posn[1]]

            players.append((Player(avatar='', home=home_tile, goal=goal_tile, position=home_posn), goal_posn))
        return players

    def __setup_players(self, player_apis, board, extra_tile, players, goal_positions):
        for i in range(len(player_apis)):
            player_apis[i].setup((board, extra_tile, players[i]), goal_position=goal_positions[i])

    def __run_game(self, state):
        kicked_players = []
        winners = []

        for round_number in range(self.rounds):
            # TODO : TAKE TURNS
            
        return winners, kicked_players

