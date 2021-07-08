# Написать функцию которая уберет из dict элементы с пустыми значениями:
# {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
# Должно вернуть {'first_color': 'Red', 'second_color': 'Green'} # * dict может быть произвольным

slov = {'hero1': 'iron_man', 'hero2': 'batman', 'hero3': None, 'hero4': None, 'hero5': 'deadpool'}
print('Словарь: ', slov)


def ubr_elem(sl):
    sl2 = {k: v for k, v in sl.items() if v != None}
    return sl2


print('Новый словарь: ', ubr_elem(slov))
