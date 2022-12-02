from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        with open("highscore.txt") as data:
            self.highscore = int(data.read())
        self.score = 0
        self.hideturtle()
        self.pencolor('white')
        self.penup()
        self.goto(0,260)
        self.pendown()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.highscore} ", False, align="center", font=('Arial', 25, 'bold'))

    def increase_score(self):
        self.score += 1
        self.update_score()


    def game_over(self):
        self.reset()
        self.goto(-75,0)
        self.write("Game Over", False,font=('Arial',25,'bold'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt",'w') as data:
                data.write(f"{self.highscore}")
        self.score =0
        self.update_score()