import turtle as t
import random
tim = t.Turtle()

colors = ["medium aquamarine","burlywood","medium purple","light green","navajo white"]

def drawshape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3,11):
    tim.color(random.choice(colors))
    drawshape(shape_side_n)

