from tkinter import *

janela = Tk()

def bt_click():
    #print("bt")
    
    if (str(ed.get()).isnumeric() and str(ed1.get()).isnumeric()):
        num1 = int(ed.get())
        num2 = int(ed1.get())
        soma = num1 + num2
        lb["text"] = soma
    else:
        lb["text"] = "Valores invalidos"

ed = Entry(janela)
ed.place(x = 100, y = 100)

ed1 = Entry(janela)
ed1.place(x = 100, y = 120)

bt = Button(janela, text = "Soma", width = 10, command = bt_click)
bt.place(x = 100, y = 150)

lb = Label(janela, text = "")
lb.place(x = 100, y = 200)

janela.geometry("400x300+200+200")
janela.mainloop()
