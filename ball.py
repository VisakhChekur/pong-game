from turtle import Turtle
import random


class Ball(Turtle):
    """Creates a ball."""

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.movement_speed = 0.1
        self.x_distance = 0
        self.y_distance = 0
        self.directions = ['left', 'right']
        self.random_direction = 0
        self.move(True)

    def move(self, movement_initial=False):
        """Handles the movement of the ball."""
        new_x = self.xcor() + self.x_distance
        new_y = self.ycor() + self.y_distance
        self.goto(new_x, new_y)
        if movement_initial == True:
            self.random_direction = random.choice(self.directions)
            if self.random_direction == 'left':
                self.x_distance = -10
            elif self.random_direction == 'right':
                self.x_distance = 10
            self.y_distance = random.choice([-10, 10])

    def bounce(self, bounce_object):
        """Bounces the ball of the wall or the paddle."""
        if bounce_object == 'wall':
            self.y_distance *= -1

        elif bounce_object == 'paddle':
            self.x_distance *= -1
            self.movement_speed *= 0.9
