from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(0, 270)
        self.color("white")
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=('Arial', 16, 'normal'))


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=('Arial', 20, 'normal'))

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=('Arial', 8, 'normal'))