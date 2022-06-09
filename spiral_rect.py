from PIL import Image, ImageDraw

insta_max = (1080, 1350)
img = Image.new('RGBA', insta_max, 'white')
draw = ImageDraw.Draw(img)
points = [(insta_max[0]//2, insta_max[1]//2)]
step = 9
order = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for i in range(999):
    mx, my = order[i%4]
    x, y = (step*i*mx, step*i*my)
    last_x, last_y = points[-1]
    if not 0 < last_x < insta_max[0]:
        print("Break at iter %s" % i)
        break
    points.append((x+last_x, y+last_y))
    draw.ellipse((points[-1][0]-step//2, points[-1][1]-step//2, points[-1][0]+step//2, points[-1][1]+step//2), fill='red')

draw.line(points, fill='black', width=step)
img.show()
