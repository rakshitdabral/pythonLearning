from player import Turtle
import random




class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color_list = []
        self.create_car()


    def create_car(self):
         self.color_random()
         POSITION_X = random.randrange(-600, 600)
         POSITION_Y = random.randrange(-300, 300)
         self.shape('square')
         self.shapesize(stretch_wid=1,stretch_len=2)
         self.color(random.choice(self.color_list))
         self.goto(POSITION_X, POSITION_Y)


    def reset_car_position(self):
        self.color_random()
        POSITION_Y = random.randrange(-300, 300)
        self.color(random.choice(self.color_list))
        self.goto(600, POSITION_Y)

    def car_move(self):
         x_cor = self.xcor()
         y_cor = self.ycor()
         self.goto(x_cor-10, y_cor)

    def car_stop(self):
        self.goto(self.xcor(),self.ycor())

    def new_car_position(self):
        POSITION_X = random.randrange(-600, 600)
        POSITION_Y = random.randrange(-300, 300)
        self.color(random.choice(self.color_list))
        self.goto(POSITION_X, POSITION_Y)

    def color_random(self):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        self.color_list.append((r,g,b))


