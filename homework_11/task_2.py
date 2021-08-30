# Написать функцию которая определит является ли введенная строка палиндромом
# (та которая читается одинаково с любой стороны), пример:
# ШАЛАШ, КАЗАК, ДЕД, ДОХОД, 13231 и т.д.

first = input('Введите сроку - ')


def palindrom(check):
    check2 = check[::-1]
    if check == check2:
        return True
    else:
        return False


print(palindrom(first))
