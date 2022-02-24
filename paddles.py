from turtle import Turtle, Screen
# STARTING_POSITION_PADDLE1 = []
# screen = Screen()


class Paddle(Turtle):
    """Class for a paddle."""

    def __init__(self, paddle_location):
        """Create the paddle."""
        super().__init__()
        self.shape("square")
        self.speed('fastest')
        self.color('white')
        self.shapesize(stretch_len=5)
        self.penup()
        self.setheading(90)
        if paddle_location == 'right':
            self.goto(350, 0)
        elif paddle_location == 'left':
            self.goto(-350, 0)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
