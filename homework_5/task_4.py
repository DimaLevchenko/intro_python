# Дан список случайных целых чисел. Замените все нечетные числа списка нулями. И выведете их количество.
import random
def randomspis():
    list = []
    c = 0
    while c < 10:
        i = random.randint(0, 100)
        list.append(i)
        c += 1
    print('Список случайных чисел: ', list)
    return list


spis = randomspis()


def newspis(lis):
    lis2 = []
    c = 0
    for i in lis:
       if i % 2 != 0:
           lis2.append(0)
           c += 1
       else:
           lis2.append(i)
    return lis2, c

spis2 = newspis(spis)
print('Новый список: ', spis2[0])
print('Количество нечетных чисел: ', spis2[1])
