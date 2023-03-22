from tkinter import*
import tkinter.font as tkfont
from tkinter import messagebox

W=Tk()
W.title('BẢNG ĐIỂM ')
W.geometry("650x400+200+100")
fontstyle = tkfont.Font(family="arial",size=14)
x=IntVar()
def click_add():
    if E_name.get()==''or E_math.get()=='':
        pass
    else:
        if x.get()<0 or x.get()>10:
            messagebox.showinfo("BẢNG ĐIỂM",'Mời nhập lại giá trị')
        else:
            a=E_name.get()
            b=E_math.get()
            l_name.insert(0,str(a))
            l_math.insert(0,str(b))
def click_delete():
    x=l_name.curselection()
    for i in x:
        l_name.delete(i)
        l_math.delete(i)
#tạo 2 frame
f1=Frame(W,width=200,height=300)
f1.place(x=20,y=20)
f2=Frame(W,width=200,height=300)
f2.place(x=250,y=20)
#tạo 2 label
name=Label(f1,text='HỌ VÀ TÊN:',font=fontstyle, fg='blue')
name.place(x=0,y=0)
math=Label(f2,text='ĐIỂM SỐ:', font=fontstyle, fg='blue')
math.place(x=0,y=0)
#tạo 2 entry box
E_name=Entry(f1,font=fontstyle)
E_name.place(x=0,y=40)
E_math=Entry(f2,font=fontstyle,textvariable=x)
E_math.place(x=0,y=40)
#tạo 2 list box
l_name=Listbox(f1,font=fontstyle,selectmode=BROWSE )
l_name.place(x=0,y=80)
l_math=Listbox(f2,font=fontstyle,selectmode=BROWSE )
l_math.place(x=0,y=80)
#tạo 2 button
add=Button(W,text='ADD',font=fontstyle, width=10,command=click_add)
add.place(x=480,y=120)
delete=Button(W,text='DELETE',font=fontstyle, width=10,command=click_delete)
delete.place(x=480,y=180)
W.mainloop()