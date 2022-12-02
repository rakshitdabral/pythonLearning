from turtle import  Turtle


class Paddle():
    def __init__(self,position):
        self.segments = []
        self.create_paddle(position)

    def create_paddle(self,position):

            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.shapesize(5,1)  # default size is 20pixel so 5*20 = 100 height and 20 width
            new_segment.penup()
            new_segment.setpos(position)
            self.segments.append(new_segment)

    def move_up(self):
            x_cor = self.segments[0].xcor()
            y_cor = self.segments[0].ycor()
            self.segments[0].setpos(x_cor,y_cor+20)

    def move_down(self):
        x_cor = self.segments[0].xcor()
        y_cor = self.segments[0].ycor()
        self.segments[0].setpos(x_cor,y_cor-20)

