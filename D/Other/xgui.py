import tkinter as tk
from PIL import Image, ImageTk
import json

# The dimensions of a single image tile in the gui
tile_dimensions = (100, 100)

# Mapping acceptable characters to their corresponding file path
file_map = {
    "┌": 'Other/Images/right-down.png',
    "┐": 'Other/Images/left-down.png',
    "┘": 'Other/Images/left-up.png',
    "└": 'Other/Images/right-up.png'
}


def read_stdin():
    """
    Parses the stdin stream into distinct rows of acceptable characters
    :return: rows: (List-of String) -> Represents the acceptable characters that were parsed
    """
    rows = []
    while True:
        try:
            input_str = input().strip()
            input_rows = [x.strip() for x in input_str.split('\"')]

            while "" in input_rows:
                input_rows.remove('')

            for row in input_rows:
                rows.append(row)

        # ending successfully (on user-break with 'CTRL-D') or End of File
        except EOFError:
            break
    return rows


def get_image(character):
    """
    Return the correct image, given an acceptable character
    :param character: (String) Acceptable character
    :return: im: (Image) The mapped acceptable character's image
    """
    im = Image.open(file_map[character])
    im = ImageTk.PhotoImage(im)
    return im


def handle_mouse_click(event):
    """
    Prints click location, and exits program on click event
    :param event: (ButtonPress event) left mouse click event
    """
    out_str = json.dumps([event.x, event.y])
    print(out_str)
    exit()


def xgui(input_arr):
    """
    Creates gui effect representing the parsed rows of acceptable characters from STDIN
    :param input_arr: (List-of String) -> The parsed rows of acceptable characters
    """
    window = tk.Tk()
    window.bind("<Button-1>", handle_mouse_click)

    if input_arr:
        w, h = (tile_dimensions[0] * len(input_arr[0]),
                tile_dimensions[1] * len(input_arr))
        window.geometry(f'{w}x{h}')
        for i in range(len(input_arr)):
            for j in range(len(input_arr[0])):
                im = get_image(input_arr[i][j])
                panel = tk.Label(window, image=im, bd=0)
                panel.image = im
                panel.grid(row=i, column=j)

    window.mainloop()


if __name__ == "__main__":
    gui_input = read_stdin()
    xgui(gui_input)
