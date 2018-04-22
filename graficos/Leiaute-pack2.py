from tkinter import *

janela = Tk()

'''
lb1 = Label(janela, text = "RIGHT", bg = "white")
lb2 = Label(janela, text = "BOTTOM", bg = "white")
lb3 = Label(janela, text = "LEFT", bg = "white")
lb4 = Label(janela, text = "TOP", bg = "white")

lb1.pack(side=RIGHT)
lb2.pack(side=BOTTOM)
lb3.pack(side=LEFT)
lb4.pack(side=TOP)
'''

lb1 = Label(janela, text = "side1", bg = "white")
lb2 = Label(janela, text = "side2", bg = "red")
lb3 = Label(janela, text = "anchor1", bg = "white")
lb4 = Label(janela, text = "anchor2", bg = "red")

lb1.pack(side=LEFT)
lb2.pack(side=LEFT)
lb3.pack(anchor=NW)
lb4.pack(side=BOTTOM, anchor=SW)

janela["bg"] = "black"

janela.geometry("400x300+200+200")
janela.mainloop()
