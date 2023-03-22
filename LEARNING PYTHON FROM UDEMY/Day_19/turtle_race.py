from turtle_gui import Turtle, Screen
import random
import keyboard
    
#tạo 1 danh sách có tất cả các vật 
screen=Screen()
screen.setup(height=500, width=1200)
screen.listen()
user_choice=screen.textinput(title='make your bet !', prompt='guess turtle win: ')
all_turtle=[]

list_turtle_color=["green","red","yellow","orange","black"]
pos_start_y=[200,100,0,-100,-200]
for i in range(0,5):
    new_turtle=Turtle()
    new_turtle.color(list_turtle_color[i])
    new_turtle.shape("turtle")
    new_turtle.penup()     
    new_turtle.goto(-500,pos_start_y[i])
    all_turtle.append(new_turtle)


race_continue=True
turtle_1_go=0
turtle_2_go=0
turtle_3_go=0
turtle_4_go=0
turtle_5_go=0
winning= ' '
def turtle_1():
    global turtle_1_go
    for i in range(0, len(list_step),5):
        turtle_1_go+=list_step[i]
        if turtle_1_go > 10000:
           global race_continue
           race_continue=False
           global winning
           winning=new_turtle.pencolor()
        else:
            pass
def turtle_5():
    global turtle_5_go
    for i in range(4, len(list_step),5):
        turtle_5_go+=list_step[i]
        if turtle_5_go > 10000:
           global race_continue
           race_continue=False
           global winning
           winning=new_turtle.pencolor()
        else:
            pass
def turtle_2():
    global turtle_2_go
    for i in range(1, len(list_step),5):
        turtle_2_go+=list_step[i]
        if turtle_2_go > 10000:
           global race_continue
           race_continue=False
           global winning
           winning=new_turtle.pencolor()
        else:
            pass
def turtle_3():
    global turtle_3_go
    for i in range(2, len(list_step),5):
        turtle_3_go+=list_step[i]
        if turtle_3_go > 10000:
           global race_continue
           race_continue=False
           global winning
           winning=new_turtle.pencolor()
        else:
            pass
def turtle_4():
    global turtle_4_go
    for i in range(3, len(list_step),5):
        turtle_4_go+=list_step[i]
        if turtle_4_go > 10000:
           global race_continue
           race_continue=False
           global winning
           winning=new_turtle.pencolor()
        else:
            pass


# tạo 1 hàm di chuyển cho các vật thể

#tạo 1 vòng lặp vô tận, khi tổng số bước của 1 vật thể bất kì lớn hơn 400 thì kết thúc

def move():
    new_turtle.forward(step)

list_step=[]
keyboard.wait('space')
   
while(race_continue):
    for turtle in all_turtle:
        step= random.randrange(20,50)
        list_step.append(step)
        turtle.forward(step)
    turtle_1() 
    turtle_2()
    turtle_3()
    turtle_4()
    turtle_5()
if winning == user_choice:
    print('Your win')
else:
    print(f'Your loss. turtle win is {new_turtle.pencolor()}')




screen.exitonclick()