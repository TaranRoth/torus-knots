import turtle
import sys
from svg_turtle import SvgTurtle

# p, q are torus knot indices, a is the int/tuple representing one break point, b is the int/tuple of the other, 
def draw_standard_diagram(p: int, q: int, scalar, prop, prop_2, pen, band: bool=False, a: int=None, b: int=None, over: bool=True):
    """
    screen = turtle.Screen()
    screen.title(f"({p}, {q}) Torus Knot")
    screen.bgcolor("white")
    """

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
        """
        pen.color('red')
        pen.up()
        pen.goto(init)
        pen.down()
        pen.dot(10)
        pen.up()
        pen.goto(final)
        pen.down()
        pen.dot(10)
        """

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


def save_standard_diagram_img(p: int, q: int, filename: str, scalar=30, prop=.7, prop_2=1.2, width=2048, height=2048, band=False, band_info=[]):
    t = SvgTurtle(width, height)
    draw_standard_diagram(p, q, scalar, prop, prop_2, t, True, 1, 2, True)
    t.save_as(filename)


if __name__ == '__main__':
    # draw_standard_diagram(10, 7, 20, .8, 1.2)
    p = int(sys.argv[1])
    q = int(sys.argv[2])
    img = save_standard_diagram_img(p, q, f'imgs/({p}, {q}).svg', 30, .7, 1.2, 4096, 4096, True, [1, 2, True])
