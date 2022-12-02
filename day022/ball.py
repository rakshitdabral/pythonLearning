from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.move_speed = 0.1
        self.x_axis = 10
        self.y_axis = 10

    def refresh(self):
        new_x = self.xcor() + self.x_axis
        new_y = self.ycor() + self.y_axis
        self.goto(new_x,new_y )

    def bounce_wall(self):
        self.y_axis *= -1

    def bounce_paddle(self):
        self.x_axis *= -1
        self.move_speed *= 0.9

    def ball_reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_axis *= -1