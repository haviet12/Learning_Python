from tkinter import*
from tkinter import ttk
import tkinter.font as tkfont
from tkinter import messagebox
W=Tk()
W.title('MONEY EXCHANGE')
W.geometry("600x400+200+100")

x1=IntVar

def click_button():
    M=0
    T=0
    if x1.get() !='':
        M= float(x1.get())
    if x1.get()==0:
       messagebox.showinfo("MONEY EXCHANGE","VUI LONG CHON LOAI NGOAI TE")
    else:
        T=M*x1.get()
        L.configure(text="gia tri quy doi: {:,} vnd".format(T))

    


fontstyle = tkfont.Font(family="arial",size=15)
USD=Radiobutton(master=W, text='USD: 22.000', font=fontstyle, variable=x1, value=22.000)
USD.place(x=20,y=20)

EUR=Radiobutton(master=W, text='EUR: 26.000', font=fontstyle, variable=x1, value=26.000)
EUR.place(x=20,y=80)

JYP=Radiobutton(master=W, text='JYP: 200', font=fontstyle, variable=x1, value=200)
JYP.place(x=20,y=140)

E= Entry(master=W,font=fontstyle, width=15)
E.place(x=280,y=20)

EX = Button(master=W, text="EXCHANGE", font=fontstyle, command=click_button)
EX.place(x=280,y=80)

L=Label(master=W, text="GIA TRI QUY DOI", font=fontstyle , fg="blue")
L.place(x=150,y=250)


W.mainloop()