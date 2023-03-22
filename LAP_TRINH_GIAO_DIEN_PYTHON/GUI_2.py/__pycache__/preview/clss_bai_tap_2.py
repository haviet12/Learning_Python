from tkinter import*
import tkinter.font as tkfont
from tkinter import messagebox
class Gui:
    def __init__(self,master1):
        self.x=IntVar()
        self.master=master1
        self.fontstyle = tkfont.Font(family="arial",size=14)
        self.name=Label(master1,text='HỌ VÀ TÊN:',font=self.fontstyle, fg='blue')
        self.name.place(x=10,y=0)
        self.math=Label(master1,text='ĐIỂM SỐ:', font=self.fontstyle, fg='blue')
        self.math.place(x=250,y=0)
        self.E_name=Entry(master1,font=self.fontstyle)
        self.E_name.place(x=10,y=40)
        self.E_math=Entry(master1,font=self.fontstyle,textvariable=self.x)
        self.E_math.place(x=250,y=40)
        self.l_name=Listbox(master1,font=self.fontstyle,selectmode=BROWSE )
        self.l_name.place(x=10,y=80)
        self.l_math=Listbox(master1,font=self.fontstyle,selectmode=BROWSE )
        self.l_math.place(x=250,y=80)
        self.add=Button(master1,text='ADD',font=self.fontstyle, width=10,command=self.click_add)
        self.add.place(x=480,y=120)
        self.delete=Button(master1,text='DELETE',font=self.fontstyle, width=10,command=self.click_delete)
        self.delete.place(x=480,y=180)
        self.menu_bar=Menu(self.master)
        self.master.configure(menu=self.menu_bar)
        self.menu_file=Menu(self.menu_bar,tearoff=False)
        self.menu_bar.add_cascade(label='Menu Help',menu=self.menu_file)
        self.menu_file.add_command(label='About', command=self.about)
    def click_add(self):
        if self.E_name.get()=='' or self.E_math.get()=='':
            pass
        else:
            x=float(self.E_math.get())
            if x<0 or x>10:
                messagebox.showinfo('Invalid','please enter your number again')
            else:
                y=self.E_name.get()
                self.l_name.insert(0,str(y))
                self.l_math.insert(0,str(x))
    def click_delete(self):
        x=self.l_name.curselection()
        for i in x:
            self.l_name.delete(i)
            self.l_math.delete(i)
    def about(self):
        mlist=[]
        a=int(self.l_math.size())
        for i in range (a):
            mlist.append(float(self.l_math.get(i)))
       
        Gui.aver=sum(mlist)/a
        Gui.name=self.l_name.get(mlist.index(max(mlist)))


        W2=Toplevel()
        W2.title('BẢNG ĐIỂM ')
        W2.geometry("650x400+200+100")
        app_2=Gui_2(W2)
        W2.grab_set()
        W2.mainloop()
def main():
    W=Tk()
    W.title('BẢNG ĐIỂM ')
    W.geometry("650x400+200+100")
    app=Gui(W)
    W.mainloop()

class Gui_2(Gui):
    
    def __init__(self,master2):
        
        self.master=master2
        self.fontstyle = tkfont.Font(family="arial",size=14)
        self.name=Label(master2,text='Sinh viên có điểm cao nhất là:{}'.format(self.name), font=self.fontstyle)
        self.name.place(x=20,y=20)
        self.aver_math=Label(master2,text='Điểm trung bình:{}'.format(self.aver), font=self.fontstyle)
        self.aver_math.place(x=20,y=80)
      
        
if __name__ == '__main__':
    main()