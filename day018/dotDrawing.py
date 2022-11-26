import turtle as t
from turtle import Screen
import colorgram
import random


t.colormode(255)
timmy = t.Turtle()
rgb_color = []
color = colorgram.extract('image.jpg',9)
size = 0
y_axis = 50

for color_select in color:
    r = color_select.rgb.r
    g = color_select.rgb.g
    b = color_select.rgb.b
    new_color = (r , g , b)
    rgb_color.append(new_color)
# print(rgb_color)

ext_color = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
timmy.hideturtle()
timmy.speed('fastest')
def draw():
 global size,y_axis
 timmy.penup()
 timmy.goto(-250,-200)
 while size < 10:
    for i in range(0,10):
        timmy.pencolor(random.choice(ext_color))
        timmy.dot(20)
        timmy.penup()
        timmy.forward(50)
        timmy.penup()
    timmy.goto(-250, (-200+y_axis))
    y_axis += 50
    size += 1

draw()

screen = Screen()
screen.exitonclick()
