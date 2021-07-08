# Пользователь вводит число от 1 до 10, программа генерирует рандомное число от 1 до 10,
# если числа равны напечатать 'You won!' если нет - 'You lose!'. Дать пользователю три попытки ;)

import random

prog = random.randint(1, 10)
print('Загаданное число: ', prog)

i = 1
while i <= 3:
    pol = int(input('Введите число от 1 до 10: '))
    i += 1
    if pol == prog:
        print('You won!')
        break
    else:
        print('You lose!')
