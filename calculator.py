#imporat
from  tkinter import  *

window = Tk()

window.title("Calculator")
window.geometry("500x500")

#Enter box
e = Entry(window,width=56,borderwidth=6)
e.place(x = 0,y = 0 )
#Button
def click(num):
    result = e.get()
    e.delete(0,END)
    e.insert(0,str(result)+str(num))
   

b = Button(window, text="1",width=12,bg="",fg="white",command=lambda:click(1))
b.place(x=10,y=60)

b = Button(window, text="2",width=12,command=lambda:click(2))
b.place(x=80,y=60)

b = Button(window, text="3",width=12,command=lambda:click(3))
b.place(x=170,y=60)

b = Button(window, text="4",width=12,command=lambda:click(4))
b.place(x=10,y=120)

b = Button(window, text="5",width=12,command=lambda:click(5))
b.place(x=80,y=120)

b = Button(window, text="6",width=12,command=lambda:click(6))
b.place(x=170,y=120)

b = Button(window, text="7",width=12,command=lambda:click(7))
b.place(x=10,y=180)

b = Button(window, text="8",width=12,command=lambda:click(8))
b.place(x=80,y=180)

b = Button(window, text="9",width=12,command=lambda:click(9))
b.place(x=170,y=180)

b = Button(window, text="0",width=12,command=lambda:click(0))
b.place(x=10,y=240)

#addition
def add():
    n1=e.get()
    global math
    math = "Addition"
    global i 
    i = int(n1) 
    e.delete(0,END)
     
    
b = Button(window, text="+",width=12,command=add)
b.place(x=80,y=240)

#subtraction
def sub():
    n1=e.get()
    global math
    math = "Subtraction"
    global i 
    i = int(n1) 
    e.delete(0,END)
    
b = Button(window, text="-",width=12,command=sub)
b.place(x=170,y=240)

#multiplication
def mul():
    n1=e.get()
    global math
    math = "Multiplication"
    global i 
    i = int(n1) 
    e.delete(0,END)
    
b = Button(window, text="*",width=12,command=mul)
b.place(x=10,y=300)

#divition
def div():
    n1=e.get()
    global math
    math = "Division"
    global i 
    i = int(n1) 
    e.delete(0,END)

b = Button(window, text="/",width=12,command=div)
b.place(x=80,y=300)

#Equal
def equal():
    n2 = e.get()
    e.delete(0,END)
    if math == "Addition":
        e.insert(0,i + int(n2))
    elif math == "Subtraction":
        e.insert(0,i - int(n2))
    elif math == "Multiplication":
        e.insert(0,i * int(n2))
    elif math == "Division":
        e.insert(0,i / int(n2))    

b = Button(window, text="=",width=12,command=equal)
b.place(x=170,y=300)

#Clear
def clear():
    e.delete(0,END)

b = Button(window, text="clear",width=12,command=clear)
b.place(x=10,y=350)


e.pack()
mainloop()