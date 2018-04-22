from tkinter import *

def bt_click():
    print(ed.get())
    lb["text"] = ed.get()

janela = Tk()
janela.title("Entrada-Dados")

ed = Entry(janela)
ed.place(x=100,y=100)

bt = Button(janela, width=10, text="OK", command=bt_click)
bt.place(x=100, y=150)

lb = Label(janela, text="Teste!")
lb.place(x=100, y= 200)


janela.geometry("300x300+200+200")
janela.mainloop()
