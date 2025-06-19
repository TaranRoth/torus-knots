import sys
import math
import os
from svg_turtle import SvgTurtle

def draw_band_diagram(p: int, q: int, scalar, prop, prop_2, pen, band_code):
    pen.color("black")
    pen.penup()
    pen.hideturtle()
    pen.speed(1000)
    pen.goto(0, 0)

    pen.pendown()

    final_coords = []
    initial_coords = []
    for i in range(p):
        base = (-(scalar * prop_2) * i, scalar * i)
        if i == 0:
            initial_coords.append(base)
        pen.up()
        pen.goto(base)
        pen.down()
        pen.setheading(180)
        pen.forward(scalar)
        pen.setheading(90)
        pen.forward(q * scalar)
        pen.setheading(180)
        pen.forward(scalar)
        pen.up()
        pen.goto(base)
        for i2 in range(q - 1):
            pen.up()
            coords = (base[0], base[1] + ((i2 + 1) * scalar))
            if i == 0:
                initial_coords.append(coords)
            pen.goto(coords)
            pen.down()
            pen.forward(scalar * prop)
    for i in range(-1, q - 1):
        pen.up()
        coords = (-(scalar * prop_2) * p, scalar * p + ((i + 1) * scalar))
        final_coords.append((coords[0] + 8, coords[1]))
        pen.goto(coords)
        pen.down()
        pen.forward(scalar * prop_2)

    c = 1
    print(initial_coords, final_coords)
    for init, final in zip(initial_coords, final_coords):
        pen.up()
        pen.goto(init)
        pen.down()
        pen.setheading(0)
        pen.forward(c * scalar)
        pen.setheading(270)
        pen.forward((c * 2 - 1) * scalar)
        pen.setheading(180)
        pen.forward((init[0] - final[0]) + ((c * 2 + 1) * scalar))
        pen.setheading(90)
        pen.forward((final[1] - init[1]) + ((c * 2 - 1) * scalar))
        pen.setheading(0)
        pen.forward(c * scalar)
        c += 1
    
    if len(band_code) > 0:
        bg_color = '#D5D3D3'
        pen.up()
        pen.goto((-math.floor(p / 2) * scalar, -scalar))
        right_start = pen.pos()
        pen.down()
        pen.color(bg_color)
        pen.forward(scalar * math.floor(p / 2))
        left_start = pen.pos()
        pen.up()
        pen.goto((-math.floor(p / 2)) * scalar, -scalar * (len(band_code) + 2))
        pen.down()
        pen.forward(scalar * math.floor(p / 2))
        for start in [right_start, left_start]:
            pen.up()
            pen.goto(start)
            pen.color('black')
            pen.down()
            pen.setheading(270)
            c = 0
            for crossing in band_code:
                c += 1
                if crossing == '1':
                    base = pen.pos()
                    pen.up()
                    pen.color(bg_color)
                    pen.setheading(180)
                    pen.goto((start[0] + (1 - prop) * scalar, start[1] - scalar * c))
                    pen.down()
                    pen.forward((1 - prop) * scalar * 2)
                    pen.up()
                    pen.goto(base)
                    pen.setheading(270)
                    pen.color('black')
                    pen.down()
                    pen.forward(scalar)
                if crossing == '0':
                    pen.forward(scalar * prop)
                    pen.up()
                    pen.forward((1 - prop) * 2 * scalar)
                    pen.down()
            pen.forward(scalar * prop)


def save_band_diagram_img(p: int, q: int, filename: str, scalar=30, prop=.7, prop_2=1.2, width=2048, height=2048, band_code=''):
    try:
        os.mkdir(os.getcwd() + f'/imgs/({p}, {q})')
    except FileExistsError:
        pass
    filename = filename[:-4] + '/' + band_code + '.svg'
    pen = SvgTurtle(width, height)
    draw_band_diagram(p, q, scalar, prop, prop_2, pen, band_code)
    pen.save_as(filename)


if __name__ == '__main__':
    # draw_standard_diagram(10, 7, 20, .8, 1.2)
    p = int(sys.argv[1])
    q = int(sys.argv[2])
    band_code = str(sys.argv[3])
    img = save_band_diagram_img(p, q, f'imgs/({p}, {q}).svg', 30, .7, 1.2, 1024, 1024, band_code)