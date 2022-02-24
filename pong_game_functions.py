def check_collision(right_paddle, left_paddle, ball, scoreboard, screen):
    """Checks if the ball has collided with the wall or one of the paddles."""
    # Detect collission with top and bottom wall.
    if abs(ball.ycor()) > 280:
        ball.bounce('wall')

    # Detect collission with paddles.
    # Detect collision with right paddle.
    if ball.xcor() > 325 and abs(ball.ycor() - right_paddle.ycor()) < 50:
        ball.bounce('paddle')
        print("Bouncing of paddle activated.")
    # Detect collision with left paddle.
    if ball.xcor() < -325 and abs(ball.ycor() - left_paddle.ycor()) < 50:
        ball.bounce('paddle')
        print("Bouncing of paddle activated.")

    # Detect if the ball goes out of bounds.
    if abs(ball.xcor()) > 385:
        if ball.xcor() > 350:
            winning_player = 'left'
        else:
            winning_player = 'right'
        scoreboard.increase_score(winning_player)
        ball.goto(0, 0)
        ball.movement_speed = 0.1
        scoreboard.draw_middle_line()
        return True

    return False


def game_over(right_paddle, left_paddle, ball, scoreboard, screen, left_side_player, right_side_player):
    if scoreboard.right_player_score == 3 or scoreboard.left_player_score == 3:
        ball.hideturtle()
        right_paddle.hideturtle()
        left_paddle.hideturtle()
        scoreboard.display_game_over(left_side_player, right_side_player)
        scoreboard.display_score()
        screen.update()
        return False

    return True
