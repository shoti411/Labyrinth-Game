import os
import sys
import tkinter as tk
from PIL import Image, ImageTk

sys.path.append(os.path.join(os.path.dirname(__file__), "../Common"))
from state import State
from tile import Tile

class Observer:
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
        """
        Constructor

        ready represents True or False for whether the Observer is ready for a new State.
        """

        self.ready = True
        self.window = tk.Tk()

    def next(self):
        self.ready = True

    def get_ready(self):
        return self.ready

    def draw(self, state):
        self.ready = False
        
        tile_dimensions = (100, 100)
        w, h = (tile_dimensions[0]*2, tile_dimensions[1]*2)

        B = tk.Button(self.window, text ="NEXT", command = self.next)
        
        extra_tile = state.get_extra_tile()
        fp = self.TILE_CODE_FP_MAPPING[extra_tile.get_path_code()]
        im = Image.open(f'../Referee/Images/{fp}')
        im = ImageTk.PhotoImage(im)
        panel = tk.Label(self.window, image=im, bd=0)
        panel.image = im
        #panel.grid(row=0, column=0)


        self.window.geometry(f'{w}x{h}')
        B.pack()
        panel.pack()
        self.window.mainloop()

    def save(self, state, file_path):
        ...
        

    

    
