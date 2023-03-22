from turtal_gui import Turtle, Screen

tim=Turtle()
tim.shape("turtle")
tim.color("blue")
screen=Screen()
def move_forward():
    tim.penup()
    tim.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()
