import time
from turtle import Screen
from Snake import Snake
from Food import Food
from Score import Score

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.2)
    snake.move()

    if snake.snake_head.distance(food) < 15:
        food.refresh()
        score.increase()
        snake.extend()

    if snake.snake_head.xcor()>280 or snake.snake_head.xcor()<-280 or snake.snake_head.ycor()>280 or snake.snake_head.ycor()<-280:
        game_is_on=False
        score.game_over()

    for segment in snake.segments:
        if segment == snake.snake_head:
            pass
        elif snake.snake_head.distance(segment) < 10:
            game_is_on=False
            score.game_over()

screen.exitonclick()