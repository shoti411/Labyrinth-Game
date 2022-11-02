from PIL import Image, ImageDraw
import itertools

def generate_background(dimensions=(100, 100), color='white'):
    im = Image.new(mode='RGB', size=dimensions, color=color)
    return im

stuff = ['UP', 'DOWN', 'LEFT', 'RIGHT']
all_tiles = []
for L in range(2, 5):
    for subset in itertools.combinations(stuff, L):
        all_tiles.append(subset)

i = 0
for tile in all_tiles:
    im = generate_background()
    w, h = im.size

    draw = ImageDraw.Draw(im)

    if 'UP' in tile:
        draw.line((w / 2, 0, w / 2, h / 2), fill='black', width=5)
    if 'LEFT' in tile:
        draw.line((0, h / 2, w / 2, h / 2), fill='black', width=5)
    if 'RIGHT' in tile:
        draw.line((w, h / 2, w / 2, h / 2), fill='black', width=5)
    if 'DOWN' in tile:
        draw.line((w / 2, h, w / 2, h / 2), fill='black', width=5)
    im.save(f'{i}.png')
    i += 1
