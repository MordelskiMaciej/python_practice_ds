from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.highscore = 0
        self.color("white")
        self.update()

    def update(self):
        self.write(f"Score: {self.highscore}", align='center', font=('Courier', 20, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align='center', font=('Courier', 20, 'normal'))

    def increase(self):
        self.highscore +=1
        self.clear()
        self.update()