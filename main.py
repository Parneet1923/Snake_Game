from turtle import Screen
from snake import Snake
from food import Food
from tkinter import messagebox
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("yellow")
screen.title("My Snake Game")
screen.tracer(0)

messagebox.showinfo(title="CONTROLS", message="UP ARROW: Direction Upward \n DOWN ARROW: Direction Downward \n "
                                              "RIGHT ARROW: Direction Right \n LEFT ARROW: Direction Right \n"
                                              "key esc : e ")

snake = Snake()

food = Food()

scoreboard = Scoreboard()

game_on = True


def game_exit():
    global game_on
    exit_game = messagebox.askyesno(title="Exit Screen", message="Do you want to exit?")
    if exit_game:
        game_on = False


def restart_game():
    global game_on
    game_restart = messagebox.askyesno(title="Game Restart", message="Wanna restart the game.")
    if not game_restart:
        game_on = False


screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="e", fun=game_exit)

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        restart_game()
        scoreboard.reset()
        snake.reset()
        food.refresh()

    body_parts = snake.segments[1:]
    for parts in body_parts:
        if snake.head.distance(parts) < 10:
            restart_game()
            scoreboard.reset()
            snake.reset()
            food.refresh()
