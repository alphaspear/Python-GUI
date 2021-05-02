#a simple calculator with GUI
#######################################################
from tkinter import *
root = Tk()
root.title("Simple Calculator")

#Function definations
#########################################################

def Button_add():
    first_number= e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0,END)

def Button_subtract():
    first_number= e.get()
    global f_num
    global math
    math = "subtract"
    f_num = int(first_number)
    e.delete(0,END)

def Button_divide():
    first_number= e.get()
    global f_num
    global math
    math = "divide"
    f_num = int(first_number)
    e.delete(0,END)


def Button_multiply():
    first_number= e.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_number)
    e.delete(0,END)

def Button_equal():
    second_number = e.get()
    e.delete(0,END)

    if math=="addition":
        e.insert(0,f_num + int(second_number))
    if math=="subtract":
        e.insert(0,f_num - int(second_number))
    if math=="divide":
        e.insert(0,f_num / int(second_number))
    if math=="multiply":
        e.insert(0,f_num * int(second_number))

def Button_cls():
    e.delete(0, END)

def Button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0,str(current) + str(number))

#input Box    
###############################################################
e=Entry(root,width=40,borderwidth=2)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

#Button defs
###############################################################
button1 = Button(root,text = "1",padx=40,pady=20,command=lambda: Button_click(1))
button2 = Button(root,text = "2",padx=40,pady=20,command=lambda: Button_click(2))
button3 = Button(root,text = "3",padx=40,pady=20,command=lambda: Button_click(3))
button4 = Button(root,text = "4",padx=40,pady=20,command=lambda: Button_click(4))
button5 = Button(root,text = "5",padx=40,pady=20,command=lambda: Button_click(5))
button6 = Button(root,text = "6",padx=40,pady=20,command=lambda: Button_click(6))
button7 = Button(root,text = "7",padx=40,pady=20,command=lambda: Button_click(7))
button8 = Button(root,text = "8",padx=40,pady=20,command=lambda: Button_click(8))
button9 = Button(root,text = "9",padx=40,pady=20,command=lambda: Button_click(9))
button0 = Button(root,text = "0",padx=40,pady=20,command=lambda: Button_click(0))

buttoncls = Button(root,text = "Clear",padx=79,pady=20,command= Button_cls)

buttonsum = Button(root,text = "+",padx=40,pady=20,command=Button_add)
buttondif = Button(root,text = "-",padx=40,pady=20,command=Button_subtract)
buttondiv = Button(root,text = "/",padx=43,pady=20,command=Button_divide)
buttonpro = Button(root,text = "X",padx=40,pady=20,command=Button_multiply)
buttonres = Button(root,text = "=",padx=89,pady=20,command=Button_equal)

#Button View format
#################################################################
button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)

button0.grid(row=4,column=0)
buttoncls.grid(row=4,column=1,columnspan=2)

buttonsum.grid(row=6,column=0)
buttondif.grid(row=6,column=1)
buttondiv.grid(row=6,column=2)

buttonpro.grid(row=7,column=0)
buttonres.grid(row=7,column=1,columnspan=2)

#run
##################################################################
root.mainloop()
#################################################################