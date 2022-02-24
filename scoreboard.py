from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 40, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.speed('fastest')
        self.draw_middle_line()
        self.left_player_score = 0
        self.right_player_score = 0
        self.display_score()

    def draw_middle_line(self):
        self.penup()
        self.home()
        self.setheading(90)
        self.width(2)
        for i in range(5):
            self.penup()
            self.fd(30)
            self.pendown()
            self.fd(30)
        self.penup()
        self.home()
        self.setheading(270)
        for i in range(5):
            self.penup()
            self.fd(30)
            self.pendown()
            self.fd(30)

    def display_score(self):
        self.penup()
        self.goto(0, 230)
        score_text = f"{self.left_player_score}      {self.right_player_score}"
        self.write(arg=score_text, align=ALIGNMENT, font=FONT)

    def increase_score(self, winning_player):
        if winning_player == 'right':
            self.right_player_score += 1
            self.clear()
            self.display_score()
        elif winning_player == 'left':
            self.left_player_score += 1
            self.clear()
            self.display_score()

    def display_game_over(self, left_side_player, right_side_player):
        if self.right_player_score > self.left_player_score:
            game_over_text = f"{right_side_player.title()} won!"
        else:
            game_over_text = f"{left_side_player.title()} won!"
        self.clear()
        self.penup()
        self.home()
        self.write(arg=game_over_text, font=FONT, align=ALIGNMENT)
