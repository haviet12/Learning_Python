from tkinter import*
from PIL import Image,ImageTk
BMI=Tk()
BMI.title("Adult BMI Calculator")
BMI.geometry("600x400+300+100")

title= Label(master=BMI, text="Adult BMI Calculator" ,bg="darkblue", fg="white",  font=("arial", 15 ))
title.grid(column=0, row=0)

height= Label(master=BMI, text="Height:Centimeters" , font=("arial", 15 ))
height.grid(column=0, row=3)

textbox_height =Entry(master=BMI )
textbox_height.grid(column=0, row=4 )

weight= Label(master=BMI, text="Weight:Kilograms" , font=("arial", 15 ))
weight.grid(column=0, row=5)

textbox_weight= Entry(master=BMI)
textbox_weight.grid(column=0, row=6)



def click_1():
    A=float(textbox_height.get())/100
    A=float(textbox_weight.get())
    

BMI.mainloop()