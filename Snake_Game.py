import turtle
import time
from Fruit import Fruit
from Snake import Snake
from Score import Score

is_on = True

snake = Snake()
Fruit = Fruit()
Score_tracker = Score()

my_screen = turtle.Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_screen.listen()
my_screen.tracer(0)
my_screen.onkey(fun=snake.turnup, key="Up")
my_screen.onkey(fun=snake.turnright, key="Right")
my_screen.onkey(fun=snake.turnleft, key="Left")
my_screen.onkey(fun=snake.turndown, key="Down")


while is_on:
    my_screen.update()
    time.sleep(0.1)
    snake.snake_move()
    if snake.snake[0].distance(Fruit) < 15:
        Fruit.refresh()
        Score_tracker.increase_score()
        snake.extend()
    if snake.snake[0].xcor() > 290 or snake.snake[0].xcor() < -290 or snake.snake[0].ycor() > 290 or snake.snake[0].ycor() < -290:
        is_on = False
        Score_tracker.game_over()
    for segment in snake.snake[1:len(snake.snake)-1]:
        if snake.snake[0].distance(segment) < 10:
            is_on = False
            Score_tracker.game_over()


my_screen.exitonclick()
