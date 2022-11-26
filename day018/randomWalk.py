import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color

# color = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw():
    direction = [0,90,180,270]
    choice = random.choice(direction)
    color_select = random_color()
    timmy.speed('fastest')
    timmy.pensize(10)
    timmy.color(color_select)
    timmy.forward(20)
    timmy.setheading(choice)

for i in range(0,1000):
    draw()