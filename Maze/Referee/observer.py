import os
import sys
import json
import random
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog as fd

sys.path.append(os.path.join(os.path.dirname(__file__), "../Common"))
from player_state import Player
from state import State
from tile import Tile


class Observer(tk.Tk):
    """
    Observer represents a GUI for a state of Maze game.

    Observer has the functionality to save a State and show the next State aswell.
    """

    TILE_CODE_FP_MAPPING = {
        '│': '0.png',
        '┘': '1.png',
        '└': '2.png',
        '┐': '3.png',
        '┌': '4.png',
        '─': '5.png',
        '┤': '6.png',
        '├': '7.png',
        '┴': '8.png',
        '┬': '9.png',
        '┼': '10.png'
    }

    def __init__(self):
        super().__init__()
        self.geometry(f'{800}x{900}')

        self.ready = True
        self.state = False

        self.board = self.__initialize_board(rows=7, cols=7)
        im = Image.open(f'{str(os.path.dirname(os.path.abspath(__file__)))}\Images\\blank.png')
        im = ImageTk.PhotoImage(im)
        self.extra_tile = tk.Label(self, image=im, bd=10)
        self.extra_tile.image = im
        self.extra_tile.pack()

        self.next_button = tk.Button(self, text="NEXT", command=self.next)
        self.next_button.pack()

        self.save_button = tk.Button(self, text="SAVE", command=self.save)
        self.save_button.pack()

    def __initialize_board(self, rows, cols):
        board = []
        board_frame = tk.Frame()
        im = Image.open(f'{str(os.path.dirname(os.path.abspath(__file__)))}\Images\\blank.png')
        im = ImageTk.PhotoImage(im)
        for r in range(rows):
            board.append([])
            for c in range(cols):
                tile = tk.Label(board_frame, image=im, bd=1)
                tile.image = im
                board[r].append(tile)
                tile.grid(row=r, column=c)
        board_frame.pack()
        return board

    def next(self):
        self.ready = True

    def save(self):
        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/')
        file = open(filename, 'w')
        file.write(self.state_to_json())
        file.close()

    def get_ready(self):
        return self.ready

    def draw(self, state):
        self.state = state

        self.ready = False
        extra_tile = state.get_extra_tile()
        self.draw_tile(self.extra_tile, extra_tile)
        self.draw_board(state.get_board().get_board())

    def draw_tile(self, reference, tile):
        fp = self.TILE_CODE_FP_MAPPING[tile.get_path_code()]
        im = Image.open(f'{str(os.path.dirname(os.path.abspath(__file__)))}\Images\{fp}')
        im = ImageTk.PhotoImage(im)
        reference.configure(image=im)
        reference.image = im

    def draw_board(self, board):
        for r in range(len(board)):
            for c in range(len(board[r])):
                reference = self.board[r][c]
                self.draw_tile(reference, board[r][c])

    def player_to_json(self, player, board):
        assert isinstance(player, Player)
        player_data = {}
        coords = player.get_coordinate()
        x = coords.getX()
        y = coords.getY()
        player_data['current'] = {'row#': x, 'column#': y}

        home_coords = board.find_tile_coordinate_by_tile(player.get_home())
        player_data['home'] = {'row#': home_coords.getX(), 'column#': home_coords.getY()}

        goal_coords = board.find_tile_coordinate_by_tile(player.get_goal())
        player_data['goto'] = {'row#': goal_coords.getX(), 'column#': goal_coords.getY()}

        player_data['color'] = "%06x" % random.randint(0, 0xFFFFFF)
        return player_data


    def board_to_json(self, board):
        connectors = []
        treasures = []
        board_obj = board.get_board()
        for row in range(len(board_obj)):
            connectors.append([])
            treasures.append([])
            for col in range(len(board_obj[row])):
                connectors[row].append(board_obj[row][col].get_path_code())
                treasures[row].append([g.value for g in board_obj[row][col].get_gems()])
        return {'connectors': connectors, 'treasures': treasures}

    def tile_to_json(self, tile):
        assert isinstance(tile, Tile)
        gems = tile.get_gems()
        return {'tilekey': tile.get_path_code(), '1-image': gems[0].value, '2-image': gems[1].value}

    def last_action_to_json(self):
        last_action = self.state.get_last_action()
        if not last_action or last_action.is_pass():
            return None
        direction_int = last_action.get_direction()
        if last_action.get_isrow():
            direction = 'LEFT' if direction_int == -1 else 'RIGHT'
        else:
            direction = 'UP' if direction_int == -1 else 'DOWN'
        last_action = [last_action.get_index(), direction]
        return last_action

    def state_to_json(self):
        state_json = {
            'board': self.board_to_json(self.state.get_board()),
            'spare': self.tile_to_json(self.state.get_extra_tile()),
            'plmt': [self.player_to_json(p, self.state.get_board()) for p in self.state.get_players()],
            'last': self.last_action_to_json()
        }
        return json.dumps(state_json)
