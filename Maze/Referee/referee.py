import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),"../Common"))

from player_game_state import PlayerGameState
from state import State
from player_state import Player
from board import Board
from tile import Tile
from coordinate import Coordinate
import random
import copy
import itertools



class Referee:

    def __init__(self, min_row=7, min_col=7, max_rounds=1000):
        self.min_rows = min_row
        self.min_cols = min_col
        self.max_rounds = max_rounds
    """
    TODO: create slide, insert classes for lastAction and Move
    

    TODO: run 1 game to completion
        - return winning players and those who misbehave


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
        player_states, goal_positions = self.__initialize_players(board, len(players), players)
        self.__setup_players(players, board, extra_tile, player_states, goal_positions)
        state = State(board=board, extra_tile=extra_tile, players=player_states)
        return self.__run_game(state)

    def __initialize_board(self, players):
        proposed_boards = []
        kicked_players = []
        for player in players:
            try:
                proposed_board = Board(player.proposeBoard(self.min_rows, self.min_cols))
                proposed_boards.append(proposed_board)
            except ValueError:
                kicked_players.append(player)
                continue
        [players.remove(x) for x in kicked_players]
        game_board = random.choice(proposed_boards)
        return game_board

    def __initialize_players(self, board, num_players, player_apis):
        players = []
        board_length = len(board)
        goal_positions = list(itertools.product(range(board_length, step=2), range(board_length, step=2)))
        valid_goal_tiles = []
        for (x, y) in goal_positions:
            valid_goal_tiles.append(Coordinate(x,y))
        for player in range(num_players):
            home_posn = random.choice(valid_goal_tiles)
            valid_goal_tiles.remove(home_posn)
            home_tile = board[home_posn.getX()][home_posn.getY()]

            goal_posn = random.choice(valid_goal_tiles)
            valid_goal_tiles.remove(goal_posn)
            goal_tile = board[goal_posn.getX()][goal_posn.getY()]

            players.append((Player(avatar='', home=home_tile, goal=goal_tile, position=home_posn, player_api=player_apis[player]), goal_posn))
        return players

    def __valid_move(self, state, action):
        """
        Checks if a Action is valid. 

        valid for a Pass is anything
        valid for a Move requires:
            degrees must be a multiple of 90
            direction must be -1 or 1
            index must be in board's moveable rows or columns
            isrow must be a boolean
            Coordinate must be on the board and reachable.
            Move cannot undo the last action a player has made.

        :param: state <State>: Game knowledge of the referee
        :param: action <Action>: Action a player is taking 
        """

        if action.is_pass():
            return
        
        if action.get_degree() % 90 != 0:
            raise ValueError(f'{action.get_degree()} not multiple of 90')
        if action.get_direction() not in [-1, 1]:
            raise ValueError(f'Invalid direction: {action.get_direction()}')
        if not isinstance(action.get_isrow(), bool):
            raise ValueError(f'{action.get_isrow()} not a boolean.')
        if action.get_isrow() and action.get_index() not in state.get_board().get_moveable_rows():
            raise ValueError(f'{action.get_index()} not movable row')
        if not action.get_isrow() and action.get_index() not in state.get_board().get_moveable_columns():
            raise ValueError(f'{action.get_index()} not movable col')
        if action.does_undo(state.get_last_action()):
            raise ValueError(f'Action undoes last action.')

        state_copy = copy.deepcopy(state)
        state_copy.rotate_extra_tile(action.get_degree())
        state_copy.shift(action.get_index(), action.get_direction(), action.get_isrow())
        if not state_copy.active_can_reach_tile(action.get_coordinate()):
            raise ValueError(f'Action undoes last action.')

    def __setup_players(self, player_apis, board, extra_tile, players, goal_positions):
        for i in range(len(player_apis)):
            player_apis[i].setup((board, extra_tile, players[i]), goal_position=goal_positions[i])

    def __run_game(self, state):
        kicked_players = []
        while not state.is_game_over(self.max_rounds):
            # TODO: build get_player_game_state for this line in state
            active_player_game_state = PlayerGameState(state.get_board(), state.get_extra_tile(),
                                                       state.get_active_player(), state.get_last_action())

            # TODO: timeout errors
            move = state.get_active_player().get_player_api().take_turn(active_player_game_state)

            # try:
            #     pass
            # except Exception as e:
            #     print(e)
            #     state.kick_active()
            #     continue

            try:
                self.__valid_move(state, move)
            except ValueError as e:
                print(e)
                kicked_players.append(state.get_active_player())
                state.kick_active()
                continue

            state.rotate_extra_tile(move.get_degree())
            state.shift(move.get_index(), move.get_direction(), move.get_isrow())
            state.move_active_player(move.get_coordinate())
        winners = state.get_winners()
        return winners, kicked_players

