from tkinter import*
from tkinter import ttk
import tkinter.font as tkfont
from tkinter import messagebox
W=Tk()
W.title('BMI Calculator')
W.geometry("600x400+200+100")
fontstyle = tkfont.Font(family="arial",size=15)

height=Label(master=W, text="CHIỀU CAO(cm):", font=fontstyle)
height.place(x=20,y=20)

entry_height=Entry(master=W, )
entry_height.place(x=20,y=60)

weight=Label(master=W, text="CÂN NẶNG(kg):", font=fontstyle)
weight.place(x=20,y=100)

entry_weight=Entry(master=W)
entry_weight.place(x=20,y=140)

x1=IntVar()

def click_rd2():
    height.configure(text="CHIỀU CAO(Inches)", fg="red")
    weight.configure(text="CÂN NẶNG(Pounds)", fg="red")
def click_rd1():
    height.configure(text="CHIỀU CAO(cm)", fg="blue")
    weight.configure(text="CÂN NẶNG(kg)", fg="blue")
def click_bt():
    a=float(entry_height.get())
    b=float(entry_weight.get())
    if x1.get()==0:
        messagebox.showinfo("BMI Calculator","VUI LONG CHON LOAI DON VI",)
    if x1.get() ==1:
        T = b/(a*a)
        LB.configure(text="BMI ="+str(T))
    else :
        T = (b/(a*a))*703
        LB.configure(text="BMI ="+str(T))

RB1=Radiobutton(master=W, text='Metric',variable=x1, font=fontstyle, value=1,command=click_rd1)
RB1.place(x=250,y=40)
RB2=Radiobutton(master=W, text='English',variable=x1, font=fontstyle, value=2, command=click_rd2)
RB2.place(x=250,y=100)

BT=Button(master=W, text='CALCULATOR',font=fontstyle, command=click_bt)
BT.place(x=180,y=200)

LB=Label(master=W, text="BMI=",font=fontstyle,fg="green")
LB.place(x=220,y=250)


W.mainloop()
