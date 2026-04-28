import turtle
from itertools import cycle

colors = ['red', 'green', 'blue', 'yellow', 'magenta']
c = cycle(colors)

t = turtle.Turtle()
t.speed(0)

for i in range(37):
    t.color(next(c))
    t.circle(50)
    t.left(20)

turtle.done()
