import random

min = 1
max = 10

#roll_again = 'sim'
roll = 1

while roll != 0:
    print('Sorteando')
    print(random.randint(min, max))

    roll_again = input('Quer sortear de novo?(s/n) ')
    if roll_again == 'sim' or roll_again == 's':
        roll = 1
    else:
        roll = 0
