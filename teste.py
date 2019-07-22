"""import sys

args = sys.argv

print("File is:", args[0])

try:
    print("Name is:",args[1])
except IndexError:
    print("User didn't enter name")
---------------------------------------------------
from tqdm import tqdm
from time import sleep

for i in tqdm(range(10)):
    sleep(0.2)
"""
import turtle
from random import choice

pencil = turtle.Turtle()
pencil.speed(200)
COLORS = ['red', 'yellow', 'green', 'blue']

for i in range(180):
    c = choice(COLORS)
    pencil.pencolor(c)
    pencil.forward(100)
    pencil.right(30)
    pencil.forward(20)
    pencil.left(60)
    pencil.forward(50)
    pencil.right(30)
    pencil.penup()
    pencil.setposition(0,0)
    pencil.pendown()
    pencil.right(2)

turtle.done()
