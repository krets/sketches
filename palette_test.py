"""
"""
from PIL import Image, ImageDraw, ImageFont
import palette


insta_max = (1080, 1350)
img = Image.new('RGBA', (600, 600), 'dimgrey')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("Arial.ttf", 10)

pad = 20

funcs = [
    palette.triadic,
    palette.analogous,
    palette.complimentary,
    palette.split_complimentarty,
    palette.square,
    palette.rect,
    palette.mono
]
y_cursor = 0
x_cursor = 0
box_size = 50
for func in funcs:
    colors = func(saturation=.65, value=.7)
    colors = palette.wobble_colors(palette.expand_colors(colors), sat_variance=.5, val_variance=.2)
    box = (x_cursor+pad, y_cursor+pad, x_cursor+pad+box_size, y_cursor+pad+box_size)
    if box[3]+box_size*len(colors) > img.height-pad:
        x_cursor += box_size + pad
        y_cursor = 0
        box = (x_cursor + pad, y_cursor + pad, x_cursor + pad + box_size, y_cursor + pad + box_size)
    for i, color in enumerate(colors):
        draw.rectangle(box, fill=color)
        x1, y1, x2, y2 = box
        box = x1, y2, x2, y2+box_size
        y_cursor = y2
    draw.text((x_cursor+pad, y_cursor), "%.10s" % func.__name__, font=font)



img.show()