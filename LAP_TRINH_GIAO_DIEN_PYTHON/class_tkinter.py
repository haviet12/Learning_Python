from tkinter import *
import tkinter.font as tkfont
class bin:
    def __init__(self,master1):
        self.master = master1
        self.fontstyle = tkfont.Font(family="arial",size=15)
        self.l_dec=Label(self.master,text='DECIMAL',font=self.fontstyle)
        self.l_dec.place(x=40,y=40)
        self.l_bin=Label(self.master,text='DECIMAL',font=self.fontstyle)
        self.l_bin.place(x=40,y=90)
        self.e_dec=Entry(self.master,font=self.fontstyle)
        self.e_dec.place(x=100,y=40)
        self.e_bin=Entry(self.master,font=self.fontstyle)
        self.e_bin.place(x=100,y=90)
    
    def but_click():
        pass
class bin1:
    pass

def main():
    W=Tk()
    W.geometry('644x400+300+300')
    W.title('BINARY CONVERT')
    app=bin(W)
    W.mainloop()
if __name__ == '__main__':
    main()