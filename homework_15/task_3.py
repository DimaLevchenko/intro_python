# Вводимый пользователем пароль должен соответсвовать требованиям,
# 1. Как минимум 1 символ от a-z
# 2. Как минимум 1 символ от A-Z
# 3. Как минимум 1 символ от 0-9
# 4. Как минимум 1 символ из $#@-+=
# 5. Минимальная длина пароля 8 символов.
# Программа принимает на ввод строку, в случае если пароль не верный -
# пишет какому требованию не соответствует и спрашивает снова,
# в случае если верный - пишет 'Password is correct'.

import re

password = input('Enter your password - ')


def check(pw):
    if not re.search(r'[a-z]', pw):
        return 'At least 1 symbol from a-z is required'
    if not re.search(r'[A-Z]', pw):
        return 'At least 1 symbol from A-Z is required'
    if not re.search(r'\d', pw):
        return 'At least 1 symbol from 0-9 is required'
    if not re.search(r'[$#@+=\-]', pw):
        return 'At least 1 symbol of $#@-+= is required'
    if len(pw) < 8:
        return 'At least 8 symbol is required'
    return 'Password is correct'


print(check(password))
