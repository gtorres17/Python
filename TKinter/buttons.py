from tkinter import *
from functools import partial

def bt_click(btn):
    print(btn["text"])

screen = Tk()

bt1 = Button(screen, width=20, text="Botão 1")
bt1.place(x=100, y=100)
bt1["command"] = partial(bt_click, bt1)

bt2 = Button(screen, width=20, text="Botão 2")
bt2.place(x=100, y=130)
bt2["command"] = lambda: bt_click(bt2) 

screen.geometry("300x300+200+200")
screen.mainloop()