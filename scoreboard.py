from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,-270)
        self.update_score()
    def update_score(self):
        self.write(f"score:{self.score}",align="centre",font=("aerial",24,"normal"))
    def game_over(self):
        self.write("game over","left",font=("aerial",24,"normal"))
    def score_up(self):
        self.score+=1
        self.clear()
        self.update_score()
