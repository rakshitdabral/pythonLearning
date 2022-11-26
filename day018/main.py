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

def draw(size_of_gap):
  for _ in range(int(360/size_of_gap)):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.setheading(timmy.heading()+size_of_gap)
    timmy.speed("fastest")

draw(5)