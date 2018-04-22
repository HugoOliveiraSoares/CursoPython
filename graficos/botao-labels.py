from tkinter import *

def bt_click():
    print("clicado")

    lb["text"] = "Funcionou!!"

janela = Tk()

bt = Button(janela, width=10, text="Ok", command=bt_click)
bt.place(x=100, y=100)

lb = Label(janela, text="teste")
lb.place(x=100, y=150)

janela.geometry("300x300+200+200")
janela.mainloop()
