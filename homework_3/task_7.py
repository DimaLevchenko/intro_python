# Написать программу которая найдет факториал введенного пользователем числа.
# Например, факториал числа 5 равен произведению 1 * 2 * 3 * 4 * 5 = 120.
# Формула нахождения факториала:
# n! = 1 * 2 * … * n, где n - введенное пользователем число.

x = int(input('Введите число: '))

f = 1
while x > 1:
    f *= x
    x -= 1
print('Факториал от числа:', f)