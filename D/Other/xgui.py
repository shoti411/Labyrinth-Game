import tkinter as tk
from PIL import Image, ImageTk
import json

tile_dimensions = (100, 100)

file_map = {
    "┌": './Images/right-down.png',
    "┐": './Images/left-down.png',
    "┘": './Images/left-up.png',
    "└": './Images/right-up.png'
}


def read_stdin():
    rows = []
    while True:
        try:
            input_str = input()
            if input_str != "":
                rows.append(input_str)
        # ending successfully (on user-break with 'CTRL-D') or End of File
        except EOFError:
            break
    return rows


def get_image(character):
    im = Image.open(file_map[character])
    im = ImageTk.PhotoImage(im)
    return im


def handle_mouse_click(event):
    y = event.widget.grid_info()['row']
    x = event.widget.grid_info()['column']
    out_str = json.dumps([x, y])
    print(out_str)
    exit()


def xgui(input_arr):
    window = tk.Tk()
    w, h = (tile_dimensions[0] * len(input_arr[0]),
            tile_dimensions[1] * len(input_arr))
    window.geometry(f'{w}x{h}')
    window.bind("<Button-1>", handle_mouse_click)
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
