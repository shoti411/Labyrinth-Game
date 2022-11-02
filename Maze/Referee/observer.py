import tkinter as tk
from PIL import Image, ImageTk

class Observer:
    """
    Observer represents a GUI for a state of Maze game.

    Observer has the functionality to save a State and show the next State aswell.
    """

    def __init__(self):
        """
        Constructor

        ready represents True or False for whether the Observer is ready for a new State.
        """

        self.ready = True

    def next(self):
        self.ready = True

    def get_ready(self):
        return self.ready

    def draw(self, state):
        print("HERERERERE")
        self.ready = False
        window = tk.Tk()
        tile_dimensions = (100, 100)
        w, h = (tile_dimensions[0], tile_dimensions[1])


        im = Image.open('Images/left-down.png')
        im = ImageTk.PhotoImage(im)
        panel = tk.Label(window, image=im, bd=0)
        panel.image = im
        panel.grid(row=0, column=0)


        window.geometry(f'{w}x{h}')
        window.mainloop()

    def save(self, state, file_path):
        ...
        

    

    
