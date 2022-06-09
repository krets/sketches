"""
https://www.instagram.com/p/CdNP0Lut_TA/
"""
from PIL import Image, ImageDraw

insta_max = (1080, 1350)
img = Image.new('RGBA', insta_max, '#0f9dc8')
draw = ImageDraw.Draw(img)
pad = 50
mid = img.height/2 - pad
draw.rectangle((0, mid, img.width, img.height), fill='#3b7aa1')
draw.rectangle((0, mid-pad, img.width, mid), fill='#f9ffff')
draw.rectangle((0, mid, img.width, mid+pad), fill='#c3e6ed')
img.show()