from tkinter import *

janela = Tk()

lb1 = Label(janela, text="horizontal", bg="white")
lb1.pack(side=TOP, fill=X)

lb1 = Label(janela, text="Esquerda", bg="blue")
lb1.pack(side=LEFT, fill=Y)

lb1 = Label(janela, text="Direita", bg="red")
lb1.pack(side=RIGHT, fill=Y)

janela.geometry("500x200+-600+200")
janela.mainloop()
