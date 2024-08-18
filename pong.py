from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=800,height=600)
screen.title("The Pong Game")
screen.bgcolor('black')


screen.tracer(0)
paddle1=Paddle((360,0))
paddle2=Paddle((-360,0))
ball=Ball()
score=Scoreboard()

screen.listen()
screen.onkeypress(key='Up',fun=paddle1.go_up)
screen.onkeypress(key='Down',fun=paddle1.go_down)
screen.onkeypress(key='w',fun=paddle2.go_up)
screen.onkeypress(key='s',fun=paddle2.go_down)

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    # screen.delay(0.1)
    ball.move()
    if ball.ycor()>280 or ball.ycor() <-280:
        ball.bounce_y()

        
    if ball.xcor()>=340 and ball.distance(paddle1)<=50 or ball.xcor()<=-340 and ball.distance(paddle2)<=50:
        ball.bounce_x()
        
    if ball.xcor()>370:
        score.p1_wins()
        ball.reset()

    if ball.xcor()<-370:
        score.p2_wins()
        ball.reset()
screen.exitonclick()