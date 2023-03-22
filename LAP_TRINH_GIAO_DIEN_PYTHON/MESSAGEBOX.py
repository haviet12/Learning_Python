from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import tkinter.font as tkfont
from tkinter import messagebox


M =Tk()
M.title("CAP NHAT KHUON MAT")
M.geometry("600x600+400+100")

fontstyle = tkfont.Font(family="arial",size=15)
hello=Label(master=M,text="HELLO NGUOI DANG LAP TRINH", font= fontstyle,fg="blue")
hello.grid(column=1, row=0,padx=40)
box= Entry(master=M,  width=20,font=fontstyle,fg="blue")
box.grid(column=1, row=2,padx=40, pady=10)

def input_click():
    T=box.get()
    hello.configure(text="HELLO"+" " + T)
    messagebox.showinfo("CAP NHAT KHUON MAT", "HI" " "+ T+"" "HAPPYBIRTHDAY")

input=Button(master=M,text="INPUT",width=20,font=fontstyle, fg="blue", command=input_click)
input.grid(column=1, row=3)

M.mainloop()


