def clicked1():
        messagebox.showinfo('Первое', 'Вы выбрали первый вариант')
def clicked2():
        messagebox.showinfo('Второе', 'Вы выбрали второй вариант')
def clicked3():
        messagebox.showinfo('Третий', 'Вы выбрали третий вариант')
def clicked4():
    f=open('C:/Users/User/Desktop/5al.txt')
    f=f.readlines()
    txt.insert(INSERT, f)
def clicked5():
    a=int(txt1.get())
    b=int(txt2.get())
    c=combo.get()
    if c=="+":
        lbl.configure(text=a+b)
    elif c=="-":
        lbl.configure(text=a-b)
    elif c=="*":
        lbl.configure(text=a*b)
    else: 
        if b==0:
           lbl.configure(text="Ошибка") 
        else: lbl.configure(text=a/b) 


from tkinter import *
from tkinter import ttk
from decimal import *
from tkinter.ttk import Checkbutton
from tkinter import messagebox
from tkinter import Menu
from tkinter import scrolledtext
from tkinter.ttk import Combobox
window=Tk()
window.title("Балдовская Дарья Александровна")
window.geometry('500x300')
style = ttk.Style()
style.theme_create( "MyStyle", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [5, 5, 5, 5]}},
        "TNotebook.Tab": {"configure": {"padding": [15, 5, 59, 5]}, }})

style.theme_use("MyStyle")
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='Загрузить',command=clicked4)
menu.add_cascade(label='Файл', menu=new_item)
window.config(menu=menu)
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Калькулятор')
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Чекбоксы')
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Файл')
txt1 = Entry(tab1,width=10)
txt1.grid(column=1, row=0) 
combo = Combobox(tab1)
combo['values'] = ('+','-','*','/')
combo.current(1) # установите вариант по умолчанию
combo.grid(column=2, row=0) 
txt2 = Entry(tab1,width=10)
txt2.grid(column=3, row=0)
btn = Button(tab1, text="=", command=clicked5)
btn.grid(column=4, row=0)
lbl = Label(tab1, text="")
lbl.grid(column=5, row=0)
tab1.grid_rowconfigure(6, weight=1)
tab1.grid_columnconfigure(4, weight=1)
chk1_state = IntVar()
chk1_state.set(0) 
chk2_state = IntVar()
chk2_state.set(0) 
chk3_state = IntVar()
chk3_state.set(0) 
chk1 = Checkbutton(tab2, text='Первое', var=chk1_state,command=clicked1)
chk1.grid(column=0, row=0)
chk2 = Checkbutton(tab2, text='Второе', var=chk2_state,command=clicked2)
chk2.grid(column=1, row=0)
chk3 = Checkbutton(tab2, text='Третье', var=chk3_state,command=clicked3)
chk3.grid(column=2, row=0)
tab2.grid_rowconfigure(6, weight=1)
tab2.grid_columnconfigure(4, weight=1)
txt = scrolledtext.ScrolledText(tab3, width=70, height=20)
txt.grid(column=0, row=0)
tab_control.pack(anchor=N)
tab3.grid_rowconfigure(6, weight=1)
tab3.grid_columnconfigure(4, weight=1)
window.mainloop()
