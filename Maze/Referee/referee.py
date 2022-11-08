import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../Common"))

from player_game_state import PlayerGameState
from state import State
from player_state import Player
from board import Board
from tile import Tile
from coordinate import Coordinate
import random
import copy
import itertools
from observer import Observer
from threading import *
import time

class Referee:

    def __init__(self, min_row=7, min_col=7, max_rounds=1000, observer=False):
        self.min_rows = min_row
        self.min_cols = min_col
        self.max_rounds = max_rounds
        self.kicked_players = []
        self.observer = observer
        self.game_quit = False

    def pickup_from_state(self, state):
        """ Continues an existing Labyrinth game """
        if not isinstance(state, State):
            raise ValueError('state must be an instance of class State')
        if self.observer:
            return self.__run_with_observer(state)
        return self.__run_game(state)

    def run(self, players):
        """ Starts a new Labyrinth game """

        board = self.__initialize_board(players)
        extra_tile = Tile()

        player_states, goal_positions = self.__initialize_players(board, players)
        self.__setup_players(players, board, extra_tile, player_states, goal_positions)
        state = State(board=board, extra_tile=extra_tile, players=player_states)
        if self.observer:
            return self.__run_with_observer(state)
        return self.__run_game(state)

    def __run_with_observer(self, state):
        try:
            t = Thread(target=self.__run_game, args=[state])
            t.start()
            self.observer.mainloop()
            t.join()
        except SystemExit:
            self.observer = False
            self.game_quit = True
            t.join()
        return state.get_winners()

    def __initialize_board(self, players):
        """
        Asks players to propose boards, selects a random (acceptable) board.
        Kicks players with invalid boards.
        """

        proposed_boards = []

        for player in players:
            try:
                proposed_board = Board(player.propose_board(self.min_rows, self.min_cols))
                proposed_boards.append(proposed_board)
            except Exception as e:
                self.kicked_players.append(player)

        [players.remove(x) for x in self.kicked_players]
        game_board = random.choice(proposed_boards)
        return game_board

    def __initialize_players(self, board, player_apis):
        """ Creates Player objects for all the PlayerAPIs, aka Referee's knowledge of the player. """
        players = []

        goal_positions = itertools.combinations(board.get_immoveable_columns() + board.get_immoveable_rows(), 2)

        board = board.get_board()
        valid_goal_tiles = []
        for (x, y) in goal_positions:
            valid_goal_tiles.append(Coordinate(x, y))

        goals = []
        for player in range(len(player_apis)):
            home_posn = random.choice(valid_goal_tiles)
            valid_goal_tiles.remove(home_posn)
            home_tile = board[home_posn.getX()][home_posn.getY()]

            goal_posn = random.choice(valid_goal_tiles)
            valid_goal_tiles.remove(goal_posn)
            goal_tile = board[goal_posn.getX()][goal_posn.getY()]

            players.append((Player(avatar=player_apis[player].get_name(),
                                   home=home_tile,
                                   goal=goal_tile,
                                   coordinate=home_posn,
                                   player_api=player_apis[player])))

            goals.append(goal_posn)

        return players, goals

    def __setup_players(self, player_apis, board, extra_tile, players, goal_positions):
        """ Calls setup in each player, giving them the initial state. """
        for i in range(len(player_apis)):
            player_apis[i].setup(PlayerGameState(board, extra_tile, players[i], False), goal_position=goal_positions[i])

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
            raise ValueError(f'Player cannot reach tile {action.get_coordinate()}')

    def __run_game(self, state):
        if isinstance(self.observer, Observer):
            self.observer.draw(state)

        while not state.is_game_over(self.max_rounds) and not self.game_quit:
            if not self.observer or self.observer.get_ready():
                state = self.__do_round(state)
            if isinstance(self.observer, Observer) and self.observer.get_ready():
                self.observer.draw(state)

        if isinstance(self.observer, Observer):
            self.observer.draw(copy.deepcopy(state), is_game_over=True)
        winners = state.get_winners()
        return winners, self.kicked_players

    def __do_round(self, state):
        """
        Precondition: This function assumes the game State is not over.
        """
        active_player_game_state = state.get_player_game_state()

        # TODO: timeout errors

        try:
            move = state.get_active_player().get_player_api().take_turn(active_player_game_state)
            self.__valid_move(state, move)
            self.__do_move(move, state)
        except Exception as e:
            print(e)
            self.kicked_players.append(state.get_active_player())
            state.kick_active()

        return state


    def __do_move(self, move, state):
        """ Performs a give move on the given state """
        state.rotate_extra_tile(move.get_degree())
        state.shift(move.get_index(), move.get_direction(), move.get_isrow())
        state.move_active_player(move.get_coordinate())
        state.set_last_action(move)
