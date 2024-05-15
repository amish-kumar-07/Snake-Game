from turtle import Turtle
POSITION=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segment=[]
        self.create_seg()
        self.head=self.segment[0]

    def create_seg(self):
        for p in POSITION:
           self.add_new_seg(p)

    def add_new_seg(self,p):
        new_seg=Turtle()
        new_seg.penup()
        new_seg.color("white")
        new_seg.shape("square")
        new_seg.goto(p)
        self.segment.append(new_seg)
   
    def extend_seg(self):
        self.add_new_seg(self.segment[-1].position())
        

    def move(self):
        for seg in range(len(self.segment)-1,0,-1):
            x=self.segment[seg-1].xcor()
            y=self.segment[seg-1].ycor()
            self.segment[seg].goto(x,y)
        
        self.segment[0].forward(20)

    def reset(self):
        for seg in self.segment:
            seg.goto(1500,1500)
        self.segment.clear()
        self.create_seg()
        self.head=self.segment[0]

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)