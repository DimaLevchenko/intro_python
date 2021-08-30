# Написать программу которая будет форматировать номер телефона к единому виду.
# На ввод программа принимает строку введенного номера телефона, например:
# 063-999-99-99 вывод (+38) 063 999-99-99
# 063 999-99-99 вывод (+38) 063 999-99-99
# 063-99999-99 вывод (+38) 063 999-99-99
# +3806399-999-99 вывод (+38) 063 999-99-99
# 380639999999 вывод (+38) 063 999-99-99
# Если что-то не так с номером - пишет 'Failed to recognize number'.

import re

number = input('Input your cell number - ')


def mobile(num):
    num = ''.join(filter(str.isdigit, num))
    if len(num) > 9:
        if re.match(f'38', num):
            num = num[2:]
        new_num = re.sub(r'(\d{3})(\d{3})(\d{2})(\d{2})', r'(+38) \1 \2-\3-\4', num)
        return new_num
    else:
        return 'Failed to recognize number'


print(mobile(number))
