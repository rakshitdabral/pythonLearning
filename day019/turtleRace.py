import turtle
from turtle import Turtle , Screen
import random

is_race_on = False
timmy = Turtle()
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make a bet",prompt="Which turtle will win the race? Enter a color: ")
color = ["red","green","yellow","blue","black","purple"]
y_position = [-70,-40,-10,20,50,80]
all_turtle = []

for turtle_index in range(0,6):
    timmy = Turtle(shape="turtle")
    timmy.penup()
    timmy.color(color[turtle_index])
    timmy.goto(x=-230,y=y_position[turtle_index])
    all_turtle.append(timmy)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won, your color {winning_color}")
            else:
                print(f"you lose, winner is {winning_color}")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
screen.exitonclick()