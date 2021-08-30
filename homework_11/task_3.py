# Написать функцию которая сдвинет полученный список на N элементов вправо или влево,
# принимаемые аргументы - список и натуральное число(если отрицательное сдвигаем влево, положительное - вправо).

enter = input('Enter your list - ')
step = int(input('Enter number of steps - '))


def shift(st, steps):
    lst = st.split()
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())
    return lst


print(shift(enter, step))
