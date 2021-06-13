from tkinter import *
from tkinter import messagebox
from sympy import *
import math
 
root = Tk()
root.title("Импульс тела")
root.geometry("250x180+300+300")

def display():
    messagebox.showinfo("Ваш ответ:", answer)

def program():
	global answer
	x = symbols('x')
	f = func.get()
	my_diff = diff(f)
	m = mass.get()
	t = time.get()
	d = math.fabs(my_diff.subs(x,t))
	answer = float(m)*float(d)
	display()

def about():
	messagebox.showinfo("Справка", "Данная программа позволяет рассчитать импульс тела по исходным данным")

def me():
	messagebox.showinfo("Автор", "Приложение разработал Косоруков Роман Сергеевич")

about = Button(text='О программе', command=about)
about.pack()

func = Entry()
func.pack()
func.insert(0, "Ваша функция")

mass = Entry()
mass.pack()
mass.insert(0, "Масса тела")

time = Entry()
time.pack()
time.insert(0, "Момент времени")

btn = Button(text='Рассчитать', command=program)
btn.pack()

me = Button(text='Автор', command=me)
me.pack()

root.mainloop()