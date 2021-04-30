from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0, 340)
        self.hideturtle()

        self.write_score()

    def write_score(self):
        self.write(f'SCORE: {self.score}', align='center', font=('Arial', 18, 'normal'), )

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=('Arial', 18, 'normal'),)

    def refresh(self):
        self.clear()
        self.score = self.score + 1
        self.write_score()

