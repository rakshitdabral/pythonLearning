import turtle as t
import random

tim = t.Turtle()

color = ["red","grey","purple","yellow","blue","violet"]

def draw(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side in range(3,11):
    tim.color(random.choice(color))
    draw(shape_side)
