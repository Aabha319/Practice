import tkinter
from tkinter import *
root=tkinter.Tk()
root.geometry("250x400")
root.resizable(0,0)
root.title("Calculator")
date=StringVar()

lbl=Label(root,text="",anchor=SE,font=("Verdana",20),textvariable=date,background="#FFFFFF",fg="#000000")
lbl.pack(expand=True,fill="both")

val=""
A=0.0
operator=""

def btn9_isclicked():
    global val
    val=val+"9"
    date.set(val)

def btn8_isclicked():
    global val
    val=val+"8"
    date.set(val)

def btn7_isclicked():
    global val
    val=val+"7"
    date.set(val)

def btn6_isclicked():
    global val
    val=val+"6"
    date.set(val)

def btn5_isclicked():
    global val
    val=val+"5"
    date.set(val)

def btn4_isclicked():
    global val
    val=val+"4"
    date.set(val)

def btn3_isclicked():
    global val
    val=val+"3"
    date.set(val)

def btn2_isclicked():
    global val
    val=val+"2"
    date.set(val)

def btn1_isclicked():
    global val
    val=val+"1"
    date.set(val)

def btn0_isclicked():
    global val
    val=val+"0"
    date.set(val)

def btnplus_isclicked():
    global val
    global operator
    global A
    operator="+"
    A=float(val)
    val=val+"+"
    date.set(val)

def btndiv_isclicked():
    global val
    global operator
    global A
    operator="/"
    A=float(val)
    val=val+"/"
    date.set(val)

def btnprod_isclicked():
    global val
    global operator
    global A
    operator="*"
    A=float(val)
    val=val+"*"
    date.set(val)

def btnmin_isclicked():
    global val
    global operator
    global A
    operator="-"
    A=int(val)
    val=val+"-"
    date.set(val)

def result():
    global A
    global operator
    global val
    val2=val
    if operator=="+":
        B=int((val2.split("+")[1]))
        C=A+B
        date.set(C)
        val=date.get()

    if operator=="-":
        B=int((val2.split("-")[1]))
        C=A-B
        date.set(C)
        val = date.get()

    if operator=="*":
        B=int((val2.split("*")[1]))
        C=A*B
        date.set(C)
        val = date.get()

    if operator=="/":
        B=int((val2.split("/")[1]))
        C=(A/B)
        date.set(C)
        val=date.get()

def C_pressed():
    global A
    global operator
    global val
    val=""
    A=0
    operator=""
    date.set(val)

btnrow1=Frame(root)
btnrow1.pack(expand=True,fill="both")

btnrow2=Frame(root)
btnrow2.pack(expand=True,fill="both")

btnrow3=Frame(root)
btnrow3.pack(expand=True,fill="both")

btnrow4=Frame(root)
btnrow4.pack(expand=True,fill="both")

btn7=Button(btnrow1,text="7",font=("Verdana","22"),relief=GROOVE,border=0,command=btn7_isclicked)
btn7.pack(side=LEFT,expand=True,fill="both",)

btn8=Button(btnrow1,text="8",font=("Verdana","22"),relief=GROOVE,border=0,command=btn8_isclicked)
btn8.pack(side=LEFT,expand=True,fill="both",)

btn9=Button(btnrow1,text="9",font=("Verdana","22"),relief=GROOVE,border=0,command=btn9_isclicked)
btn9.pack(side=LEFT,expand=True,fill="both",)

btnc=Button(btnrow1,text="C",font=("Verdana","22"),relief=GROOVE,border=0,command=C_pressed)
btnc.pack(side=LEFT,expand=True,fill="both",)


btn4=Button(btnrow2,text="4",font=("Verdana","22"),relief=GROOVE,border=0,command=btn4_isclicked)
btn4.pack(side=LEFT,expand=True,fill="both",)

btn5=Button(btnrow2,text="5",font=("Verdana","22"),relief=GROOVE,border=0,command=btn5_isclicked)
btn5.pack(side=LEFT,expand=True,fill="both",)

btn6=Button(btnrow2,text="6",font=("Verdana","22"),relief=GROOVE,border=0,command=btn6_isclicked)
btn6.pack(side=LEFT,expand=True,fill="both",)

btndiv=Button(btnrow2,text="/",font=("Verdana","22"),relief=GROOVE,border=0,command=btndiv_isclicked)
btndiv.pack(side=LEFT,expand=True,fill="both",)

btn1=Button(btnrow3,text="1",font=("Verdana","22"),relief=GROOVE,border=0,command=btn1_isclicked)
btn1.pack(side=LEFT,expand=True,fill="both",)

btn2=Button(btnrow3,text="2",font=("Verdana","22"),relief=GROOVE,border=0,command=btn2_isclicked)
btn2.pack(side=LEFT,expand=True,fill="both",)

btn3=Button(btnrow3,text="3",font=("Verdana","22"),relief=GROOVE,border=0,command=btn3_isclicked)
btn3.pack(side=LEFT,expand=True,fill="both",)

btnprod=Button(btnrow3,text="*",font=("Verdana","22"),relief=GROOVE,border=0,command=btnprod_isclicked)
btnprod.pack(side=LEFT,expand=True,fill="both",)

btn0=Button(btnrow4,text="0",font=("Verdana","22"),relief=GROOVE,border=0)
btn1.pack(side=LEFT,expand=True,fill="both",)

btnplus=Button(btnrow4,text="+",font=("Verdana","22"),relief=GROOVE,border=0,command=btnplus_isclicked)
btnplus.pack(side=LEFT,expand=True,fill="both",)

btnmin=Button(btnrow4,text="-",font=("Verdana","22"),relief=GROOVE,border=0,command=btnmin_isclicked)
btnmin.pack(side=LEFT,expand=True,fill="both",)

btneq=Button(btnrow4,text="=",font=("Verdana","22"),relief=GROOVE,border=0,command=result)
btneq.pack(side=LEFT,expand=True,fill="both",)

root.mainloop()
