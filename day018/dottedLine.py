import turtle
from turtle import Turtle, Screen

timmy = Turtle()

for i in range(15):
    turtle.pendown()
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

screen = Screen()
screen.exitonclick()
