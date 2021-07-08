# Написать программу которая вернет количество введенных пользователем слов и общее число символов.

s = input('Ввод: ')


def chis_vved_slov(spis):
    w = 0
    z = spis.split()
    for i in z:
        w += 1
    return w


def chis_vved_sym(spis):
    w = 0
    for i in spis:
        w += 1
    return w


print('Число введенных слов: ', chis_vved_slov(s))
print('Общее число введенных символов: ', chis_vved_sym(s))
