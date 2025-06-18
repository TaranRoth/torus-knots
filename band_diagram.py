import sys
import math
from svg_turtle import SvgTurtle

def forward_break(pen, forward_amt, break_points, scalar, horizontal, break_length_prop=.5):
    break_length = scalar * break_length_prop
    heading = pen.heading()
    start = pen.pos()
    break_flag = False
    for break_point in break_points:
        horizontal_cond = break_point[1] == start[1] and break_point[0] <= start[0] and break_point[0] >= start[0] - forward_amt
        vertical_cond =  break_point[0] == start[0] and break_point[1] <= start[1] and break_point[1] >= start[1] - forward_amt
        if (horizontal and horizontal_cond) or (not horizontal and vertical_cond):
            break_flag = True
            break_dist = abs(start[0] - break_point[0])
            pen.down()
            pen.forward(break_dist)
            pen.up()
            pen.forward(break_length)
            pen.down()
            pen.forward(forward_amt - (break_dist + break_length))
            break
    if not break_flag:
        pen.forward(forward_amt)
            

def draw_band_diagram(p: int, q: int, scalar, prop, prop_2, pen, band_code):
    def get_coord(row, column=-scalar*(math.floor(p / 2))):
        return (-row * scalar, column)
    horizontal_breaks = []
    vertical_breaks = []
    row = 2
    for crossing in band_code:
        if crossing == '1':
            horizontal_breaks.append(get_coord(row))
        if crossing == '0':
            vertical_breaks.append(get_coord(row))
        row += 1

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
        forward_break(pen, (init[0] - final[0]) + ((c * 2 + 1) * scalar), horizontal_breaks, scalar, True)
        pen.setheading(90)
        pen.forward((final[1] - init[1]) + ((c * 2 - 1) * scalar))
        pen.setheading(0)
        pen.forward(c * scalar)
        c += 1


def save_band_diagram_img(p: int, q: int, filename: str, scalar=30, prop=.7, prop_2=1.2, width=2048, height=2048, band_code=''):
    filename = filename[:-4] + '-' + band_code + '.svg'
    pen = SvgTurtle(width, height)
    draw_band_diagram(p, q, scalar, prop, prop_2, pen, band_code)
    pen.save_as(filename)


if __name__ == '__main__':
    # draw_standard_diagram(10, 7, 20, .8, 1.2)
    p = int(sys.argv[1])
    q = int(sys.argv[2])
    img = save_band_diagram_img(p, q, f'imgs/({p}, {q}).svg', 30, .7, 1.2, 4096, 4096, '1')