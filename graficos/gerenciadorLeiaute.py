from tkinter import *

janela = Tk()

lb = Label(janela, text="Fala Galera!!")
lb.place(x=100, y=100)

# w x h + l + t
janela.geometry("300x300+200+100")

janela.mainloop()
