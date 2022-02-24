from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from time import sleep
from pong_game_functions import game_over, check_collision


screen = Screen()
screen.tracer(0)
screen.title("Pong Game")

screen.setup(width=800, height=600)
screen.bgcolor('black')
right_paddle = Paddle('right')
left_paddle = Paddle('left')
ball = Ball()
scoreboard = ScoreBoard()

right_side_player = screen.textinput(
    "Player Name", "Please enter the name of the right side player:")
left_side_player = screen.textinput(
    "Player Name", "Please enter the name of the left side player:")

screen.listen()
screen.onkeypress(key="Up", fun=right_paddle.move_up)
screen.onkeypress(key="Down", fun=right_paddle.move_down)
screen.onkeypress(key="w", fun=left_paddle.move_up)
screen.onkeypress(key="s", fun=left_paddle.move_down)
# ball.move(True)
screen.update()
game_active = True
new_rally = False

while game_active:
    screen.update()
    if new_rally:
        sleep(2)
        ball.move(True)
        new_rally = False
    sleep(ball.movement_speed)
    ball.move()
    new_rally = check_collision(
        right_paddle, left_paddle, ball, scoreboard, screen)
    game_active = game_over(right_paddle, left_paddle,
                            ball, scoreboard, screen, left_side_player, right_side_player)

screen.exitonclick()
