from turtle import Turtle

class Score(Turtle):

     def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.stage = 1
        self.update_level()

     def game_over(self):
         self.goto(-100,0)
         self.write("Game Over", False,font=('Ariel',40,'normal'))

     def update(self):
         self.clear()
         self.stage += 1
         self.update_level()

     def update_level(self):
         self.goto(-460,340)
         self.write(f"Level : {self.stage}", False, font=('Ariel', 30, 'normal'))


