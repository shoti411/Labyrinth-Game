import os
import sys
import json
import random
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
from tkinter import filedialog as fd

sys.path.append(os.path.join(os.path.dirname(__file__), "../Common"))
from player_state import Player
from state import State
from tile import Tile
from coordinate import Coordinate


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

    FILE_PATH = str(os.path.dirname(os.path.abspath(__file__)))

    def __init__(self):
        super().__init__()
        self.geometry(f'{1000}x{900}')
        self.protocol("WM_DELETE_WINDOW", self.close_window)
        self.ready = True
        self.state = False

        self.board = self.__initialize_board(rows=7, cols=7)
        im = Image.open(f'{self.FILE_PATH}/Images/blank.png')
        im = ImageTk.PhotoImage(im)

        info_frame = tk.Frame()

        self.extra_tile = tk.Label(info_frame, image=im, bd=20)
        self.extra_tile.image = im
        self.extra_tile.grid(row=0, column=0)

        self.next_button = tk.Button(info_frame, text="NEXT", command=self.next, bd=5)
        self.next_button.grid(row=0, column=1)

        self.save_button = tk.Button(info_frame, text="SAVE", command=self.save, bd=5)
        self.save_button.grid(row=0, column=2)

        self.state_info = tk.Label(info_frame, text='', bd=20, font=('Consolas', 10))
        self.state_info.grid(row=0, column=3)

        info_frame.pack()

    def __initialize_board(self, rows, cols):
        board = []
        board_frame = tk.Frame()
        im = Image.open(f'{self.FILE_PATH}/Images/blank.png')
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
        try:
            filename = fd.askopenfilename(
                title='Open a file',
                initialdir='/')
            file = open(filename, 'w')
            file.write(self.state_to_json())
            file.close()
        except FileNotFoundError:
            pass

    def get_ready(self):
        return self.ready

    def close_window(self):
        self.destroy()
        raise SystemExit('Observer closed early.')

    def draw(self, state, is_game_over=False):
        if is_game_over:
            self.next_button.configure(text='GAME OVER', command=self.destroy)
            self.state_info.configure(text=state.game_over_string())
        else:
            self.state_info.configure(text=str(state))
        self.state = state

        self.ready = False
        extra_tile = state.get_extra_tile()
        self.draw_tile(self.extra_tile, extra_tile)
        self.draw_board(state.get_board().get_board(), state.get_players())

    def draw_tile(self, reference, tile, players_on_tile=[], home_tile_on_tile=False):
        fp = self.TILE_CODE_FP_MAPPING[tile.get_path_code()]
        im = Image.open(f'{self.FILE_PATH}/Images/{fp}')
        draw = ImageDraw.Draw(im)

        for i in range(len(players_on_tile)):
            draw.ellipse((0, i * 10, 30, 30 + i * 10), fill=players_on_tile[i].get_avatar(), outline=(0, 0, 0))
        if home_tile_on_tile:
            draw.rectangle((65, 70, 95, 95), fill=home_tile_on_tile.get_avatar(), outline=(0, 0, 0))

        gems = [f'{self.FILE_PATH}/Images/gems/{gem.value}.png' for gem in tile.get_gems()]

        gem0 = Image.open(gems[0])
        gem1 = Image.open(gems[1])

        im.paste(gem0.resize((30, 30)), (70, 0))
        im.paste(gem1.resize((30, 30)), (0, 70))

        im = ImageTk.PhotoImage(im)
        reference.configure(image=im)
        reference.image = im

    def draw_board(self, board, players):
        for r in range(len(board)):
            for c in range(len(board[r])):
                players_on_tile = []
                home_tile_on_tile = False
                for player in players:
                    if Coordinate(r, c) == player.get_coordinate():
                        players_on_tile.append(player)
                    if board[r][c] == player.get_home():
                        home_tile_on_tile = player

                reference = self.board[r][c]
                self.draw_tile(reference, board[r][c], players_on_tile, home_tile_on_tile)

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

        color = player.get_avatar()
        if color[0] == '#':
            color = color[1:]
        player_data['color'] = color
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
