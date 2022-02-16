import sys
from tkinter import *
from tkinter import messagebox
from functools import partial

cnt=0
def hellmsg(val):
    x = val.get()
    global   cnt
    if x != 'mvi':
            cnt=cnt+1
            if cnt == 3 :
                m=messagebox.showinfo("warning","Maximum attempts reached")
                sys.exit()
            while cnt<3 :
                m = messagebox.askretrycancel("Retry", "Login unsuccessful")
                break;
    else:
        m = messagebox.askokcancel("Login", "Login successful")
mywindow=Tk()
mywindow.geometry('500x500')
mywindow.title("login page")
val=StringVar()
w=Label(mywindow,text="Enter your name").grid(row=0,column=0)
w1=Label(mywindow,text="Enter your password").grid(row=1,column=0)
entry= Entry (mywindow).grid(row=0, column=1)
entry1= Entry (mywindow,show="*",textvariable=val).grid(row=1, column=1)
hellmsg=partial(hellmsg,val)
btn= Button(mywindow,text="Login", command= hellmsg).grid(row=3, column=2)
#w.pack()
mywindow.mainloop()
