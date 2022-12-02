from turtle import Screen
import time
from car import Car
from player import Player
from scoreBoard import Score


car_index = []
initial_speed = 0.1
car_number_increment = 5

# setting up Screen
screen = Screen()
screen.title('Turtle Crossing')
screen.screensize(canvwidth=600, canvheight=600)
screen.tracer(0)
screen.colormode(255)
# calling objects
# creating multiple car objects
def car_create(increment=20):
  for i in range(increment):
    car = Car()
    car_index.append(car)

car_create()
# creating player user going to control
player = Player()
# creating level
score = Score()

# setting player controls
screen.listen()
screen.onkey(key="Up", fun=player.move_forward)
screen.onkey(key="Down", fun=player.move_backward)

is_playing = True
while is_playing:
    # updating screen and setting delay
    screen.update()
    time.sleep(initial_speed)

    # making car moves
    for i in range(len(car_index)):
         car_index[i].car_move()

         # making car reset its position after crossing a specific area
         if car_index[i].xcor() < -500:
            car_index[i].reset_car_position()

        # making sure game over when car hits player
         if car_index[i].distance(player) < 20:
            score.game_over()
            car_index[i].car_stop()
            is_playing = False


    # winning and level reset conditions
    if player.ycor() > 370:
        score.update()
        initial_speed -= 0.01

        if len(car_index) < 40:
         car_create(car_number_increment)
        else:
            pass

        player.new_level_player()

        for i in range(len(car_index)):
          car_index[i].new_car_position()



screen.exitonclick()