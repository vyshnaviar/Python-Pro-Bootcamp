import turtle as t
import random
tim = t.Turtle()

colors = ["medium aquamarine","burlywood","indianred","medium purple","light green","navajo white","seagreen"]
directions = [0,90,180,270]
tim.pensize(15)
tim.speed("fast")

for _ in range(100):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))