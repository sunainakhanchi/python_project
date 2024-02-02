import time
from snake import Snake
from turtle import Turtle ,Screen
from practice import Food
from scoreboard import Scoreboard
turtle=Turtle()
screen=Screen()
segments=[]
snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.setup(600,600)
screen.bgcolor("black")
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.score_up()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        scoreboard.game_over()
    for seg in segments:
        if seg==snake.segments:
            pass
        elif snake.head.distance(seg)<10:
            game_is_on=False
            scoreboard.game_over()
screen.exitonclick()