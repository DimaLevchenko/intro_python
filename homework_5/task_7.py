# Написать функцию `is_date`, принимающую 3 аргумента — день, месяц и год.
# Вернуть `True`, если дата корректная (надо учитывать число месяца. Например 30.02 - дата не корректная,
# так же 31.06 или 32.07 и т.д.), и `False` иначе.
# (можно использовать модуль calendar или datetime)

from datetime import datetime

d = int(input('Enter day: '))
m = int(input('Enter month: '))
y = int(input('Enter year: '))


def is_date(x, y, z):
    try:
        datetime(day=x, month=y, year=z)
        print('True')
    except ValueError:
        print('False')


is_date(d, m, y)
