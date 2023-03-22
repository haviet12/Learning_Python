from tkinter import *
from tkinter import messagebox as mbox

score = Tk()
score.geometry("700x500")
score.title("TRANSCRIPT")

y = IntVar()
list1 = []


# Create Button
def Add_click():
    if E1.get() == "" or E2.get() == "":
        pass
    else:
        if y.get() < 0 or y.get() > 10:
            mbox.showerror("Error", "The score is out of range!")
        else:
            a = E1.get()
            b = E2.get()
            LB1.insert(0, str(a))
            LB2.insert(0, str(b))
            list1.append(b)


def Delete_click():
    c = LB1.curselection()
    for i in c:
        LB1.delete(i)
        LB2.delete(i)


def Delete1():
    ans = mbox.askyesno("Announcement", "Do you want to delete all the data?")
    if ans:                  # Option "Yes"
        LB1.delete(0, END)
        LB2.delete(0, END)


def Stats():
    sum = 0
    A=int(LB2.size())
    for j in range(0, A):
        sum = sum + float(LB2.get(j))
    if len(list1) == 0:
        avg = "0"
    else:
        avg = str(sum/len(list1))
    mbox.showinfo("Average", "The average score is " + str(avg))


B1 = Button(master=score, text="ADD", font=("arial", 13), width=12, bg="green", fg="white", command=Add_click)
B1.place(x=515, y=190)
B2 = Button(master=score, text="DELETE", font=("arial", 13), width=12, bg="green", fg="white", command=Delete_click)
B2.place(x=515, y=250)

# Create Entry
E1 = Entry(master=score, font=("arial", 13), width=20)
E1.place(x=30, y=80)
E2 = Entry(master=score, font=("arial", 13), width=20, textvariable=y)
E2.place(x=270, y=80)

# Create Listbox
LB1 = Listbox(master=score, font=("arial", 13), width=20, height=15)
LB1.grid(row=0, column=0, padx=30, pady=120)
LB2 = Listbox(master=score, font=("arial", 13), width=20, height=15)
LB2.grid(row=0, column=1, padx=27, pady=120)

# Create Label
L1 = Label(master=score, text="FULL NAME:", font=("arial", 13))
L1.place(x=30, y=30)
score1 = Label(master=score, text="SCORE:", font=("arial", 13))
score1.place(x=250, y=30)

# Create Menu
menu_bar = Menu(master=score)
score.configure(menu=menu_bar)

file_menu = Menu(master=menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Stats", command=Stats())
file_menu.add_command(label="Delete All", command=Delete1)
file_menu.add_command(label="Exit", command=score.quit)

score.mainloop()