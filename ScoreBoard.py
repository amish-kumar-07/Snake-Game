from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial",12,"normal")
class score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.highest=0
        with open("High_Score.txt") as data:
            self.highest=int(data.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.write(f"Score : {self.score}       HighestScore : {self.highest}",align=ALIGNMENT,font=FONT)
        

    def score_update(self):
        self.clear()
        self.write(f"Score : {self.score}        HighestScore : {self.highest}",align=ALIGNMENT,font=FONT)

    def score_reset(self):
        if self.score > self.highest:
            self.highest=self.score
            with open("High_Score.txt",mode="w") as data:
                data.write(f"{self.highest}")
        self.score=0
        self.score_update()

    def increse_score(self):
        self.score+=1
        self.score_update()


    #def game_over(self):
    #    self.goto(0,0)
    #    self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        