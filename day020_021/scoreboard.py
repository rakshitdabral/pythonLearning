from turtle import Turtle

SCORE = 0

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor('white')
        self.penup()
        self.goto(0,260)
        self.pendown()
        self.score_add()

    def score_add(self):
        global SCORE
        self.clear()
        self.write(f"Score : {SCORE} ", False, align="center", font=('Arial', 25, 'bold'))
        SCORE += 1

    def game_over(self):
        self.goto(-75,0)
        self.write("Game Over", False,font=('Arial',25,'bold'))
