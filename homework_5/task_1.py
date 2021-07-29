# Написать функцию `is_prime`, принимающую 1 аргумент — число от 0 до 1000, и возвращающую `True`, если оно простое,
# и `False` - иначе.
# (Простые числа - те которые делятся без остатка только на само себя или 1, например 2, 3, 5, 7, 11...)

x = int(input('Введите число от 0 до 1000: '))


def is_prime(n):
    count = 0
    for i in range(n, 0, -1):
        if n % i == 0:
            count += 1
    if count > 2:
        return False
    else:
        return True


print(is_prime(x))
