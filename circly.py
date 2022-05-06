""" Circles within circles
"""
from PIL import Image, ImageDraw
import random
import math

from perlin_noise import PerlinNoise


def size_mult(res, mult):
    return int(res[0] * mult), int(res[1] * mult)


def circle(center, radius):
    x, y = center
    return x - radius, y - radius, x + radius, y + radius


def new_point(point, offset):
    x, y = point
    return (
        random.randint(int(x) - offset, int(x) + offset),
        random.randint(int(y) - offset, int(y) + offset)
    )


def max_radius(line, offset):
    x1, y1, x2, y2 = line
    a = abs(x1 - x2)
    b = abs(y1 - y2)
    c = int(math.sqrt((a ** 2 + b ** 2)))
    return abs(offset - c)


def circly(center, draw, radius, count=999, move=.06, padding=15, outline='black', width=2):
    for i in range(count):
        if isinstance(outline, list):
            color = random.choice(outline)
        draw.ellipse(circle(center, radius), outline=color, width=width)
        new_center = new_point(center, int(radius * move))
        new_radius = max_radius(list(center) + list(new_center), radius - padding)
        if new_radius < width:
            print("Stop iteration due to small circle: %i" % i)
            break
        center, radius = new_center, new_radius


def interpolate(color_a, color_b, mult):
    ra, ga, ba = color_a
    rb, gb, bb = color_b

    rc = int(abs(ra - rb) * mult + min(ra, rb))
    gc = int(abs(ga - gb) * mult + min(ga, gb))
    bc = int(abs(ba - bb) * mult + min(ba, bb))

    return rc, gc, bc


def draw(size, cols, rows, resample_scale=8, bg='white', outline='black'):
    img = Image.new('RGBA', size_mult(size, resample_scale), bg)

    background = Image.new('RGBA', size_mult(size, .25))
    noise = PerlinNoise(octaves=10, seed=1)
    color_a = (0, 31, 84)
    color_b = (5, 44, 101)
    for x in range(background.width):
        for y in range(background.height):
            val = noise([x/background.width, y/background.height])
            background.putpixel((x, y), interpolate(color_a, color_b, val))
    img.paste(background.resize(img.size, resample=Image.BICUBIC))

    draw = ImageDraw.Draw(img)
    rows += 1
    cols += 1

    for x in range(1, cols):
        for y in range(1, rows):
            center = (img.width / cols * (x), img.height / rows * (y))
            radius = min(img.width / cols, img.height / rows) * .5 * (random.random() * .4 + .6)
            circly(center, draw, radius, outline=outline, width=int(1.3*resample_scale))
    return img.resize(size)

if __name__ == '__main__':
    insta_max = (1080, 1350)
    size = size_mult(insta_max, 1.3)
    img = draw(size, 8, 10, bg=(1, 35, 91), outline=['#306596', '#88aec6', '#e6f2f2'])
    crop_pad = [(img.width - 1080)//2, (img.height - 1350)//2]
    crop_box = crop_pad + [img.width - crop_pad[0], img.height - crop_pad[1]]
    img.crop(crop_box).show()