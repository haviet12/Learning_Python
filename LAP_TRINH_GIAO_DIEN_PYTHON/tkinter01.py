from tkinter import*
from PIL import Image, ImageTk
import tkinter.font as tkfont
import cv2
W=Tk()
W.geometry("600x600+400+100")
W.title('CHUONG TRINH XAY DUNG DO HOA')

fontstyle =tkfont.Font(family="arial", size=15)
H1=Label(master=W,text="HINH_1", font=fontstyle, fg="blue" )
H1.grid(column=1,row=2)
A=ImageTk.PhotoImage(Image.open("D:\ANH\logo_AI.png"))

img_1=Label(master=W ,image=A,height=400,width=300, bg="red")

img_1.grid(column=1,row=1)

H2=Label(master=W,text="HINH_2",font=fontstyle, fg="blue")
H2.grid(column=2,row=2)
B=ImageTk.PhotoImage(Image.open("D:\ANH\logo_pythoon.png"))
img_2=Label(master=W, image=B, width=250, height=220, bg="red")
img_2.grid(column=2,row=1)

x= IntVar()
x.set(0)

def button_1_click():
    x.set(x.get()+1)
    if x.get() ==1:
        H1["bg"] ="green"
        img_1["bg"]="yellow"
    if x.get()==2:
        H1["bg"] ="white"
        img_1["bg"]="red"
        x.set(0)
def button_2_click():
    x.set(x.get()+1)
    if x.get()==1:
        H1["fg"] ="green"
    if x.get()==2:
        H2["fg"]="red"
        x.set(0)

button_1= Button(master=W,text="bg color", font=fontstyle, fg="blue", justify="center", command=button_1_click)
button_1.grid(column=1,row=3, pady=20)

button_2= Button(master=W,text="fg color", font=fontstyle, fg="blue", justify="center",command=button_2_click)
button_2.grid(column=2,row=3, pady=20)

W.mainloop()