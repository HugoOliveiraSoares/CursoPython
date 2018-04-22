from functools import partial
from tkinter import *

def bt_click(botao):
    print(botao["text"])


janela = Tk()
janela.title("Botao")

bt1 = Button(janela, width=10, text="Botao1")
bt1["command"] = partial(bt_click, bt1)
bt1.place(x=100,y=100)

bt2 = Button(janela, width=10, text="Botao2")
bt2["command"] = partial(bt_click, bt2)
bt2.place(x=100, y=150)

janela.geometry("300x300+200+100")
janela.mainloop()
