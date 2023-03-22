from turtle_gui import Turtle, Screen
import time
from pynput.keyboard import Key, Controller
import keyboard
screen=Screen()
screen.title("SNACK GAME")
screen.screensize(600,600)
screen.bgcolor("black")
screen.listen()

keyboards = Controller()
pos_st=[(0,30),(15,30),(25,30)]
turtles=[]
for i in pos_st:
    new_turtle = Turtle('square')
    new_turtle.color('white')
    new_turtle.penup()
    new_turtle.goto(i)
    turtles.append(new_turtle)
def go_up():
    for turtle in turtles:
        y=turtle.ycor()
        turtle.sety(y+10)
def go_down():
    for turtle in turtles:
        y=turtle.ycor()
        turtle.sety(y-10)
def turn_left():
        for turtle in turtles:
            x=turtle.xcor()
            turtle.setx(x-10)
def turn_right():
        for turtle in turtles:
            x=turtle.xcor()
            turtle.setx(x+10)

game_continue = True

while(game_continue):
    for snack in turtles:
        snack.forward(5)
        snack.speed('slow')
        screen.delay(10)
    keyboard.wait('space')
    go_up()
screen.exitonclick()
