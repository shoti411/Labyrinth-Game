from PIL import Image, ImageDraw
from PIL.Image import Resampling


def generate_background(d, color='white'):
    im = Image.new(mode='RGB', size=d, color=color)
    return im


im = generate_background((100, 100))
draw = ImageDraw.Draw(im)

# left line
draw.line([(0, 50), (50, 50)], fill=(0,0,0), width=10)
# right line
# draw.line([(50, 50), (100, 50)], fill=(0,0,0), width=10)
# down line
# draw.line([(50, 50), (50, 100)], fill=(0,0,0), width=10)
# up line
draw.line([(50, 0), (50, 50)], fill=(0,0,0), width=10)


def add_border(img, thickness=10, color='black'):
    w, h = img.size
    bg = generate_background((w+thickness, h+thickness), color=color)
    return overlay_image(img, bg)


def overlay_image(overlay, background, vertical='center', horizontal='center'):
    assert type(background) == Image.Image, 'background must be Image object'

    bg_w, bg_h = background.size
    img_w, img_h = overlay.size
    offset = [0, 0]
    if vertical == 'center':
        offset[1] = (bg_h - img_h) // 2
    elif vertical == 'top':
        offset[1] = 0
    elif vertical == 'bottom':
        offset[1] = bg_h - img_h

    if horizontal == 'center':
        offset[0] = (bg_w - img_w) // 2
    elif horizontal == 'left':
        offset[0] = 0
    elif horizontal == 'right':
        offset[0] = bg_w - img_w

    background.paste(overlay, offset)
    return background


im = add_border(im, thickness=2)


def resize_to_fit(img, background):
    bg_w, bg_h = background.size
    img_w, img_h = img.size

    p = min(bg_w / img_w, bg_h / img_h)
    size = [int(img_w * p), int(img_h * p)]
    return img.resize(size, Resampling.LANCZOS)


im = resize_to_fit(im, generate_background((100, 100)))
im.save('left-up.png')
