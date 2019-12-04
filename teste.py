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
from tqdm import tqdm

pencil = turtle.Turtle()
pencil.speed(200)
COLORS = ['red', 'yellow', 'green', 'blue']

for i in range(180):
    c = choice(COLORS)
    pencil.pencolor(c)
    pencil.forward(100)
    tqdm(i)
    pencil.right(30)
    tqdm(i)
    pencil.forward(20)
    tqdm(i)
    pencil.left(60)
    tqdm(i)
    pencil.forward(50)
    tqdm(i)
    pencil.right(30)
    tqdm(i)
    pencil.penup()
    tqdm(i)
    pencil.setposition(0,0)
    tqdm(i)
    pencil.pendown()
    pencil.right(2)
    tqdm(i)

turtle.done()
