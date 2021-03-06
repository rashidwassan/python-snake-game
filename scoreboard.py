from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', 'r') as data:
            self.high_score = int(data.read())
        self.penup()
        self.color('white')
        self.goto(0, 340) 
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'SCORE: {self.score}  |  High Score: {self.high_score}', align='center', font=('Arial', 18, 'normal'), )

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        file = open('data.txt', 'w')
        file.write(str(self.high_score))
        file.close()
        self.score = 0
        self.update_scoreboard()
