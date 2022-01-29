# import packages

import turtle
import random
import time

# creating screen

screen = turtle.Screen()
screen.title('SNAKE GAME')
screen.setup(width=700, height=700)
screen.tracer(0)
turtle.bgcolor('#1d1d1d')

# creating border

turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color('white')
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

# score

score = 0
delay = 0.2

# snake

snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color("white")
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'

# food

fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape('square')
fruit.color('red')
fruit.penup()
fruit.goto(30, 30)

old_fruit = []

# scoring

scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Your Score: ", align="center", font=("Courier", 24, "bold"))
