# Написать функцию которая вернет площадь фигуры: по-умолчанию треугольника, опционально квадрата.
# На входе 2 величины и параметр типа фигуры.

a = int(input('Ввести 1 значение: '))
b = int(input('Ввести 2 значение: '))
c = input('Square or triangle: ')

def s():
    if c == ('triangle'):
        p = 0.5 * a * b
        print(p)
    else:
        p = a ** 2
        print(p)
    return s

print(s())
