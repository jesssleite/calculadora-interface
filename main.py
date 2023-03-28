from tkinter import *
class MyWindow:
 def __init__(self, win):
    self.lbl1=Label(win, text='Primeiro Número')
    self.lbl2=Label(win, text='Segundo Número')
    self.lbl3=Label(win, text='Resultado', fg='blue')
    self.t1=Entry(bd=3)
    self.t2=Entry()
    self.t3=Entry()
    self.btn1 = Button(win, text='Soma')
    self.btn2=Button(win, text='Subtração')
    self.btn3 = Button(win, text='Divisão')
    self.btn4 = Button(win, text='Multiplicação')
    self.lbl1.place(x=100, y=50)
    self.t1.place(x=200, y=50)
    self.lbl2.place(x=100, y=100)
    self.t2.place(x=200, y=100)
    self.b1=Button(win, text='Soma', fg='green', command=self.add)
    self.b2=Button(win, text='Subtração' , fg='red')
    self.b3=Button(win, text='Divisão', fg='purple')
    self.b4=Button(win, text='Multiplicação', fg='orange')
    self.b2.bind('<Button-1>', self.sub)
    self.b3.bind('<Button-1>', self.div)
    self.b4.bind('<Button-1>', self.mult)
    self.b1.place(x=100, y=150)
    self.b2.place(x=200, y=150)
    self.b3.place(x=300, y=150)
    self.b4.place(x=400, y=150)
    self.lbl3.place(x=100, y=200)
    self.t3.place(x=200, y=200)

 def add(self):
    self.t3.delete(0, 'end')
    num1=int(self.t1.get())
    num2=int(self.t2.get())
    result=num1+num2
    self.t3.insert(END, str(result))

 def sub(self, event):
    self.t3.delete(0, 'end')
    num1=int(self.t1.get())
    num2=int(self.t2.get())
    result=num1-num2
    self.t3.insert(END, str(result))

 def div(self, event):
    self.t3.delete(0, 'end')
    num1=int(self.t1.get())
    num2=int(self.t2.get())
    result=float(num1/num2)
    self.t3.insert(END, str(result))

 def mult(self, event):
    self.t3.delete(0, 'end')
    num1=int(self.t1.get())
    num2=int(self.t2.get())
    result=float(num1*num2)
    self.t3.insert(END, str(result))

window=Tk()
mywin=MyWindow(window)
window.title('Olá Python')
window.geometry("400x300+10+10")
window.mainloop()