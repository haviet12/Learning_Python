from tkinter import *
import tkinter.font as tkfont
W=Tk()
W.title('Test')
W.geometry('800x600+500+100')

fontstyle=tkfont.Font(family="arial", size=14)
T=Text(W, font=fontstyle)
T.pack(expand=True,fill="both")

def click_open():
  with open('D:\\PYTHON\\text.txt', mode="r", encoding="utf-8") as f:
    A=f.read()
    T.delete('1.0',END)
    T.insert('1.0',A)
    f.close()
s=IntVar(value="13")
def Zoom_in():
  s.set(s.get()+1)
  T.configure(font=(fontstyle,s.get()))

def Zoom_out():
  s.set(s.get()-1)
  T.configure(font=(fontstyle,s.get()))

def Zoom():
  T.configure(font=(fontstyle,s.get()))
menu_bar=Menu(master=W)
W.configure(menu=menu_bar)
file_menu= Menu(master=menu_bar, tearoff=False)
menu_bar.add_cascade(label = 'File',menu=file_menu)
file_menu.add_command(label='OPEN',command=click_open)
file_menu.add_command(label='SAVE')
file_menu.add_command(label='EXIT')
file_menu.add_command(label='NEW')

view_menu=Menu(master=menu_bar, tearoff=False)
menu_bar.add_cascade(label='View',menu=view_menu)
view_menu.add_command(label='Zoom In', command=Zoom_in)
view_menu.add_command(label='Zoom Out',command=Zoom_out)
view_menu.add_separator()
view_menu.add_radiobutton(label='100%',command=Zoom)
view_menu.add_radiobutton(label='200%',command=Zoom)

scrol=Scrollbar(master=W, orient=VERTICAL,command=T.yview)
scrol.pack(side='right',fill='y')


W.mainloop()