import colorsys
import random

def bit(item, depth=8):
    return tuple(int(_*(2**depth-1)) for _ in item)


def analogous(start=None, saturation=0.8, value=0.8):
    return get_colors(start, saturation, value, step=45, count=3)

def triadic(*args, **kwargs):
    return get_colors(*args, **kwargs, step=120, count=3)

def complimentary(*args, **kwargs):
    return get_colors(*args, **kwargs, step=180, count=2)

def square(*args, **kwargs):
    return get_colors(*args, **kwargs, step=90, count=4)

def get_colors(start=None, saturation=0.8, value=0.8, step=120, count=3):
    if start is None:
        start = int(random.random()*360)

    colors = []
    for i in range(count):
        colors.append(bit(colorsys.hsv_to_rgb((i*step+start)%360/360, saturation, value)))
    return colors

def split_complimentarty(start=None, saturation=0.8, value=0.8):
    if start is None:
        start = int(random.random()*360)

    steps = [start, (start+165)%360, (start+195)%360]
    colors = []
    for angle in steps:
        colors.append(bit(colorsys.hsv_to_rgb(angle/360, saturation, value)))

    return colors

def rect(start=None, saturation=0.8, value=0.8):
    if start is None:
        start = int(random.random()*360)

    steps = [start, (start+60)%360, (start+150)%360, (start+210)%360]
    colors = []
    for angle in steps:
        colors.append(bit(colorsys.hsv_to_rgb(angle/360, saturation, value)))

    return colors


def mono(start=None, saturation=0.8, value=0, count=5):
    if start is None:
        start = int(random.random()*360)
    colors = []
    step = 1/(count+2)
    for i in range(count):
        colors.append(bit(colorsys.hsv_to_rgb(start / 360, saturation, (i+1)*step)))
    return colors

def expand_colors(colors, expand=5):
    needed = expand - len(colors)
    if needed < 1:
        return colors

    for i in range(needed):

        r, g, b = random.choice(colors)
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

        s += (random.random() - .5) * .3
        v += (random.random() - .5) * .3

        colors.append(bit(colorsys.hsv_to_rgb(h,s,v)))
    return colors

def wobble_colors(colors, hue_variance=0, sat_variance=.1, val_variance=.1):
    sortable = []
    for r, g, b in colors:
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        h += random.uniform(-hue_variance, hue_variance)
        s += random.uniform(-sat_variance, sat_variance)
        v += random.uniform(-val_variance, val_variance)
        sortable.append((h, v, bit(colorsys.hsv_to_rgb(h, s, v))))

    sortable.sort()
    return [color for _, __, color in sortable]