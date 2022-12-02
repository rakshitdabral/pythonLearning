from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreBoard import Score
import time
# setting up screen
screen = Screen()
screen.bgcolor('black')
screen.screensize(canvwidth=800,canvheight=600)
screen.title("Pong")
screen.tracer(0)
# main classes for game
l_paddle = Paddle((350,0))
r_paddle = Paddle((-350,0))
ball = Ball()
score = Score()
# defining keyPress
screen.listen()
screen.onkey(key='Up',fun =l_paddle.move_up)
screen.onkey(key="Down",fun =l_paddle.move_down)

screen.onkey(key='w',fun =r_paddle.move_up)
screen.onkey(key="s",fun =r_paddle.move_down)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.refresh()

# collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

# collision with paddle
    if ball.distance(l_paddle.segments[0]) < 50 and ball.xcor() > 330 or ball.distance(r_paddle.segments[0]) < 50 and ball.xcor() < 340:
        ball.bounce_paddle()

# missing paddle left
    if ball.xcor() > 380:
         ball.ball_reset()
         score.score_left()

# missing paddle right
    if ball.xcor() < -380:
        ball.ball_reset()
        score.score_rigth()








screen.exitonclick()