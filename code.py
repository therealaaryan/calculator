from distutils import command
from tkinter import *
root=Tk()

root.title("Calculator")

e=Entry(root,width=35,borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
def button_click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

def button_add():
    first_number=e.get()
    global f_num
    global comm
    comm="ADD"
    f_num=int(first_number)
    e.delete(0, END)

def button_sub():
    first_number=e.get()
    global f_num
    global comm
    comm="SUB"
    f_num=int(first_number)
    e.delete(0, END)

def button_mult():
    first_number=e.get()
    global f_num
    global comm
    comm="MULT"
    f_num=int(first_number)
    e.delete(0, END)

def button_div():
    first_number=e.get()
    global f_num
    global comm
    comm="DIV"
    f_num=int(first_number)
    e.delete(0, END)

def button_clear():
    e.delete(0, END)

def button_equal():
    second_number=e.get()
    e.delete(0, END)
    
    if comm=="ADD":
        e.insert(0, f_num + int(second_number))
    elif comm=="SUB":
        e.insert(0, f_num - int(second_number))
    elif comm=="MULT":
        e.insert(0, f_num * int(second_number))
    elif comm=="DIV":
        e.insert(0, f_num / int(second_number))


button_1=Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1)).grid(row=1,column=0)
button_2=Button(root,text="2",padx=40,pady=20,command=lambda :button_click(2)).grid(row=1,column=1)
button_3=Button(root,text="3",padx=40,pady=20,command=lambda :button_click(3)).grid(row=1,column=2)
button_4=Button(root,text="4",padx=40,pady=20,command=lambda :button_click(4)).grid(row=2,column=0)
button_5=Button(root,text="5",padx=40,pady=20,command=lambda :button_click(5)).grid(row=2,column=1)
button_6=Button(root,text="6",padx=40,pady=20,command=lambda :button_click(6)).grid(row=2,column=2)
button_7=Button(root,text="7",padx=40,pady=20,command=lambda :button_click(7)).grid(row=3,column=0)
button_8=Button(root,text="8",padx=40,pady=20,command=lambda :button_click(8)).grid(row=3,column=1)
button_9=Button(root,text="9",padx=40,pady=20,command=lambda :button_click(9)).grid(row=3,column=2)
button_0=Button(root,text="0",padx=40,pady=20,command=lambda :button_click(0)).grid(row=4,column=0)
button_plus=Button(root,text="+",padx=40,pady=20,command=button_add).grid(row=5,column=0)
equal_button=Button(root,text="=",padx=91,pady=20,command=button_equal).grid(row=4,column=1,columnspan=2)
clear_button=Button(root,text="CLEAR",padx=79,pady=20,command=button_clear).grid(row=6,column=1,columnspan=2)
button_minus=Button(root,text="-",padx=40,pady=20,command=button_sub).grid(row=6,column=0)
mult_button=Button(root,text="X",padx=40,pady=20,command=button_mult).grid(row=5,column=1)
div_button=Button(root,text="÷",padx=40,pady=20,command=button_div).grid(row=5,column=2)
root.mainloop()
