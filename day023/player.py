from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.left(90)
        self.penup()
        self.goto(0,-350)

    def move_forward(self):
        self.forward(10)

    def move_backward(self):
        self.backward(10)


    def new_level_player(self):
        self.goto(0, -350)