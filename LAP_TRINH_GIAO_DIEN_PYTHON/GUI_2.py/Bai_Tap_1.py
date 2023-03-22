from tkinter import*
import tkinter.font as tkfont
from tkinter import messagebox

W=Tk()
W.title('BINARY CONVERSION')
W.geometry("350x300+200+100")
fontstyle = tkfont.Font(family="arial",size=14)

x=IntVar()
y=IntVar()
y.set(0)
h=IntVar
def BTN_click():
   
    if x.get()<=0:
        messagebox.showinfo("BINARY CONVERSION","Nhập sai định dạng")
    
  
    while Entry_Dec.get()!='':
        Output_Bin.delete(0,END)
        if Entry_Dec.get()!='':
            h=int(Entry_Dec.get())
            b=bin(h)[2:]
            Output_Bin.insert(0,str(b))
        break
    
Dec=Label(W,text='DECIMAL:',font=fontstyle)
Dec.place(x=50,y=50)
Entry_Dec=Entry(W,font=fontstyle,width=10, textvariable=x)
Entry_Dec.place(x=150,y=50)

Bin=Label(W,text='BINARY:',font=fontstyle)
Bin.place(x=50,y=90)
Output_Bin=Entry(W,font=fontstyle,width=10,textvariable=y)
Output_Bin.place(x=150,y=90)

BTN=Button(W,text='CONVERT',bg='blue',fg='white', width=15, command=BTN_click)
BTN.place(x=150,y=140)
W.mainloop()