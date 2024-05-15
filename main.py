from turtle import Turtle , Screen
from Snake import Snake
from food import Food
from ScoreBoard import score
import time
screen=Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(600,600)
screen.title("Snake Game")


snake=Snake()
food=Food()
Score=score()
game_on=True

screen.listen()
screen.onkeypress(snake.up,"Up")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(snake.left,"Left")
screen.onkeypress(snake.right,"Right")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.random_location()
        Score.increse_score()
        snake.extend_seg()
    if snake.head.xcor()>280 or snake.head.ycor()>280 or snake.head.xcor()<-280 or snake.head.ycor()<-280:
            snake.reset()
            Score.score_reset()
    for seg in snake.segment[1:]:
        if snake.head.distance(seg) < 10:
            Score.score_reset()
            snake.reset()
        
        







screen.exitonclick()