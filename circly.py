""" Circles within circles
"""
from PIL import Image, ImageDraw
import random
import math


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
        draw.ellipse(circle(center, radius), outline=outline, width=width)
        new_center = new_point(center, int(radius * move))
        new_radius = max_radius(list(center) + list(new_center), radius - padding)
        if new_radius < width:
            print("Stop iteration due to small circle: %i" % i)
            break
        center, radius = new_center, new_radius


def draw(size, cols, rows, resample_scale=8, bg='white', outline='black'):
    img = Image.new('RGBA', size_mult(size, resample_scale), bg)
    draw = ImageDraw.Draw(img)
    rows += 1
    cols += 1

    for x in range(1, cols):
        for y in range(1, rows):
            center = (img.width / cols * (x), img.height / rows * (y))
            radius = min(img.width / cols, img.height / rows) * .5 * (random.random() * .4 + .6)
            circly(center, draw, radius, outline=outline, width=2*resample_scale)
    return img.resize(size)

if __name__ == '__main__':
    insta_max = (1080, 1350)
    size = size_mult(insta_max, 1.2)
    img = draw(size, 10, 13, bg=(50, 50, 50), outline='white')
    crop_pad = [(img.width - 1080)//2, (img.height - 1350)//2]
    crop_box = crop_pad + [img.width - crop_pad[0], img.height - crop_pad[1]]
    img.crop(crop_box).show()