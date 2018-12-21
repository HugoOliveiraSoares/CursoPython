import random

min = 1
max = 10

roll_again = 'sim'

while roll_again == 'sim' or roll_again == 's':
    print('Sorteando')
    print(random.randint(min, max))

    roll_again = input('Quer sortear de novo?')
