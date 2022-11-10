from tile import Tile
from board import Board
from player_state import Player
from directions import Direction
from coordinate import Coordinate
from action import Move
import copy
from player_game_state import PlayerGameState


class State:
    """
    State is the representation of the game state of Maze game.
    
    This game state comprises three essential pieces of knowledge: 
        the current state of the board; the spare tile; and the players.
        
    State has the functionality to:
        rotate spare tiles.\n
        Shift rows or columns.\n
        check if the active player can reach a tile.\n
        check if the active player is a goal tile.\n
        Kick active player.
    """

    def __init__(self, players, board, extra_tile=False, last_action=False, rounds=0, round_passes=0):
        """
        Constructs State. A State is built up of players, a board, and an extra_tile.

        :param: players <list(Player)>: players represents the list of players in the Maze game.
                                        This list also represents the order of moves in the game. 
                                            S.t players[0] represents the currently active player.
        :param: board <Board>: board is default False and will be a randomized board of 7x7.
        :param: extra_tile <Tile>: extra_tile is default False and will be a randomized Tile.
        """

        self.players = players

        # starting_players represents the (static) age order of the players in the game
        self.__starting_players = copy.copy(players)

        self.extra_tile = extra_tile
        if not extra_tile:
            self.extra_tile = Tile()
        self.board = board
        self.last_action = last_action
        self.__rounds = rounds
        self.__round_passes = round_passes

        self.__check_valid_constructor()

    def __check_valid_constructor(self):
        if not isinstance(self.extra_tile, type(Tile())):
            raise ValueError('Spare tile must be of type Tile.')
        if not isinstance(self.board, Board):
            raise ValueError('Board must be of type Board.')
        if not all([isinstance(x, Player) for x in self.players]):
            raise ValueError('Players must be of type Player.')

    def get_players(self):
        return self.players

    def get_extra_tile(self):
        return self.extra_tile

    def get_board(self):
        return copy.deepcopy(self.board)

    def get_round(self):
        return self.__rounds

    def increment_round(self):
        self.__rounds += 1

    def get_round_passes(self):
        self.__round_passes

    def move_active_player(self, coordinate):
        """
        Moves the active player to the new location.

        :param: coordinate (Coordinate): Coordinate representing the location of the move.
        """
        if self.active_can_reach_tile(coordinate):
            goal_coordinate = self.board.find_tile_coordinate_by_tile(self.players[0].get_goal())
            if coordinate == goal_coordinate:
                home_coordinate = self.board.find_tile_coordinate_by_tile(self.players[0].get_home())
                self.players[0].get_player_api().setup(None, home_coordinate)
                self.players[0].reached_goal()
                self.players[0].set_goal(self.players[0].get_home())
            self.players[0].set_coordinate(coordinate)

        else:
            raise ValueError('The given move is unreachable or unvalid.')

        self.__round_passes = 0
        self.next_player()

    def rotate_extra_tile(self, degrees):
        """
        Rotates the tile based on a given number of degrees
        
        :param: degrees (int): degrees is an int that represents the number of degrees to rotate by. 
                               degrees can be positive or negative but must be a multiple of 90.
        """
        self.extra_tile.rotate(degrees)

    def active_can_reach_tile(self, coordinate):
        """
        Checks if the Tile on board at a given coordinate is reachable from the active player.
        If given an invalid location this will return False as the player is not at that location.

        :param: coordinate <Coordinate>: Coordinate of Tile.

        :return: <bool>: True or False depending on if the player can reach the Tile.
        """
        return self.board.coordinate_is_reachable_from(coordinate, self.players[0].get_coordinate())

    def active_on_goal_tile(self):
        """
        Check if the active players coordinate is at a goal tile.

        :return: <bool>: True or False depending on if the players coordinate is at a goal tile.
        """
        return self.players[0].get_goal() == self.board.getTile(self.players[0].get_coordinate())

    def player_on_home_tile(self, player):
        """
        Check if the players coordinate is at their home tile.

        :return: <bool>: True or False depending on if the players coordinate is at a home tile.
        """
        return player.get_home() == self.board.getTile(player.get_coordinate())

    def kick_active(self):
        """
        Kicks active player from the game.
        """
        if len(self.players) > 1:
            self.players = self.players[1:]
        elif len(self.players) <= 1:
            self.players = []

    def get_last_action(self):
        return copy.deepcopy(self.last_action)

    def do_pass(self):
        """
        Passes the active players turn.
        """

        self.__round_passes += 1
        self.next_player()

    def next_player(self):
        """
        Changes the active player to the next player.

        If the last player to act is 'older' than the next player, the round is incremented.
        """
        if self.__starting_players.index(self.players[0]) >= self.__starting_players.index(self.players[1]):
            self.increment_round()
        self.players = self.players[1:] + [self.players[0]]

    def get_active_player(self):
        """
        returns the active player

        :return: <Player>
        """

        return self.players[0]

    def is_game_over(self, max_rounds):
        """
        Checks if a game is over. 
        A game is over we have reached the maximum number of rounds.
        If all players in a round has passed.
        If all players have been kicked.
        If a player has previously reached their goal tile and now at their home tile.

        :param: max_rounds <int>

        :return: <bool>
        """
        if self.__rounds >= max_rounds:
            return True
        if len(self.players) == 0:
            return True
        if self.__round_passes == len(self.players):
            return True
        for player in self.players:
            if player.has_reached_goal() and self.player_on_home_tile(player):
                return True

        return False

    def get_winners(self):
        """
        Returns a list of players who are winning.

        :return: <list(Player)>
        """
        for player in self.players:
            if player.has_reached_goal() and self.player_on_home_tile(player):
                return [player]

        winners = self.__get_players_with_minimum_distance()
        if winners:
            return winners
        return self.__get_players_with_minimum_distance(go_to_goal=True)

    def __get_players_with_minimum_distance(self, go_to_goal=False):
        winners = []
        min_distance = Coordinate(0, 0).get_euclid_distance(Coordinate(len(self.get_board().get_board()) + 1,
                                                                       len(self.get_board().get_board()[0]) + 1))
        for player in self.players:

            if go_to_goal:
                goto_coords = self.get_board().find_tile_coordinate_by_tile(player.get_goal())
            elif player.has_reached_goal():
                goto_coords = self.get_board().find_tile_coordinate_by_tile(player.get_home())
            else:
                continue

            player_distance = player.get_coordinate().get_euclid_distance(goto_coords)

            if player_distance < min_distance:
                min_distance = player_distance
                winners = [player]
            elif player_distance == min_distance:
                winners.append(player)

        return winners

    def shift(self, index, direction, is_row):
        """
        Shifts a given moveable row or column in a given direction. 
        Knocking off the Tile at the end of the shifted direction and making it the extra tile. 
        The old extra tile will be inserted at the start of the shifted direction.

        A players position will move with a shifted Tile. If a player is on the new extra tile, move it to the old extra tile.

        :param: index <int>: index of the row or column to be shifted. index must be an even number.
        :param: direction <int>: direction represents whether it is being shifted forward or backward.\n
                                 direction can be either 1 or -1.\n
                                 1 represents we are shifting forward. row shifts to the right, column shifts down.\n
                                 -1 represents we are shifting backwards. row shifts to the left, column shifts up.
        :param: is_row <bool>: True or False depending on if the index is for a row or column.
        """
        if not isinstance(is_row, bool):
            raise ValueError('is_row must be a boolean value.')

        if is_row:
            self.extra_tile = self.board.shift_row(index, direction, self.get_extra_tile())
        else:
            self.extra_tile = self.board.shift_column(index, direction, self.get_extra_tile())
        for player in self.players:

            if player.get_coordinate().getX() == index and is_row:
                new_y = int((player.get_coordinate().getY() + direction) % len(self.board.get_board()[index]))
                player.set_coordinate(Coordinate(player.get_coordinate().getX(), new_y))

            elif player.get_coordinate().getY() == index and not is_row:
                new_x = int((player.get_coordinate().getX() + direction) % len(self.board.get_board()))
                player.set_coordinate(Coordinate(new_x, player.get_coordinate().getY()))

    def set_last_action(self, action):
        self.last_action = action

    def __str__(self):
        return_str = f'----- ROUND {self.__rounds + 1} ----- \n'
        w = 15
        return_str += 'NAME'.center(w + 10)
        return_str += 'COLOR'.center(w)
        return_str += 'COORD'.center(w)
        return_str += 'GOAL'.center(w)
        return_str += 'GOAL?'.center(w) + '\n'

        for player in self.players:
            goal_coord = self.board.find_tile_coordinate_by_tile(player.get_goal())
            player_str = f'{player.get_player_api().get_name()}'.center(w + 10)
            player_str += f'{player.get_avatar()}'.center(w)
            player_str += f'{player.get_coordinate()}'.center(w)
            player_str += f'{goal_coord}'.center(w)
            player_str += f'{player.has_reached_goal()}'.center(w)
            return_str += player_str + '\n'

        return return_str

    def game_over_string(self):
        winners = self.get_winners()
        return_str = f'----- ROUND {self.__rounds + 1} ----- \n'
        return_str += f'{len(winners)} player{"s" if len(winners) > 1 else ""} won:'
        for winner in winners:
            return_str += f' {winner.get_player_api().get_name()},'
        return return_str[:-1]

    def get_other_players(self):
        '''
        Returns a dictionary mapping of the players' name to a dictionary 
        containing of their home coordinate and their current coordinate,
        excluding the active player.
        E.g. {'bob' : {'home' : Coordinate(1,1), 'current' : Coordinate(0,0)}}
        '''
        other_player_dict = {}
        for p in self.players[1:]:
            player_name = p.get_player_api().get_name()
            home_coord = self.board.find_tile_coordinate_by_tile(p.get_home())
            current_coord = self.board.find_tile_coordinate_by_tile(p.get_coordinate())
            other_player_dict[player_name] = {'home': home_coord, 'current': current_coord}
        return other_player_dict

    def get_player_game_state(self, player=False):
        if not player:
            player = self.get_active_player()
        return PlayerGameState(self.get_board(), self.get_extra_tile(), player,
                               self.get_last_action(), self.get_other_players())
