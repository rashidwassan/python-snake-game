import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(height=768, width=1080)
screen.title('Snakoo')
screen.bgcolor('black')
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.segments[0].xcor() > 530 or snake.segments[0].xcor() < -530 or snake.segments[0].ycor() > 380 or snake.segments[0].ycor() < -380:
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    for segment in snake.segments:
        if segment == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
