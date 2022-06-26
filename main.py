from turtle import Screen
from snake import Snake
from food import Food
from score import Score

import time

screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

food = Food()
snake = Snake()
score = Score()

# to detect the keystrokes
screen.listen()

# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.right, "Right")
# screen.onkey(snake.left, "Left")


screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left,"a")

# here the game starts
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 18:
        food.refresh()
        score.update()
        snake.update_snake()

    if not (350 > snake.head.xcor() > -350 and 350 > snake.head.ycor() > -350):
        # game_is_on = False
        # score.game_over()
        snake.reset()
        score.reset()

    if snake.body_collide():
        snake.reset()
        score.reset()


screen.exitonclick()
