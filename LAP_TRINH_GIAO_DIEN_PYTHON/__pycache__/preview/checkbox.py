from tkinter import*
import tkinter.font as tkFont
from tkinter import messagebox

W=Tk()
W.title("Ckeckbox Programe")
W.geometry("600x400+400+100")

fontstyle=tkFont.Font(family='arial',size =14)
x1= IntVar()
x2= IntVar()
x3= IntVar()



C1= Checkbutton(master=W, text="Ga Ran: 100.000", font=fontstyle, onvalue=100000, variable=x1)
C1.grid(columns=1, row=0, sticky="w", pady=30, padx=30)
C2=Checkbutton(master=W, text="PHO: 50.000", font=fontstyle, onvalue=50000, variable=x2)
C2.grid(columns=1, row=1,sticky="w", pady=0, padx=30)
C3=Checkbutton(master=W, text="Bo: 70.000", font=fontstyle, onvalue=70000, variable=x3)
C3.grid(columns=1, row=3,sticky="w", pady=0, padx=30)

def B_click():
    tong=x1.get()+x2.get()+x3.get()
   
    messagebox.showinfo("Ckeckbox Programe", tong )


B=Button(master=W, text="Check", font=fontstyle, bg="green", command=B_click)
B.grid(columns=2, row=2,padx=200,sticky="w")


W.mainloop()