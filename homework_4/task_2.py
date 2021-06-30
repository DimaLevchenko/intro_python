# Программа запрашивает ввод последовательности целых неотрицательных чисел, пока не будет введён 0.
# Как только будет введён 0 (ноль), программа должна посчитать и вывести на экран:

posl_c = []
i = int(input('Введите число: '))
while i != 0:
    posl_c.append(i)
    i = int(input('Введите новое число: '))
print('Последовательность чисел:', posl_c)

# - количество введённых чисел (завершающий 0 не считается)
def col_chis(posl):
    x = 0
    for i in posl:
        x += 1
    return x
print('Количество введенных чисел:', col_chis(posl_c))

# - их сумму
def sum_chis(posl):
    x = sum(posl)
    return x
print('Сумма введенных чисел:', sum_chis(posl_c))

# - произведение
def proiz_chis(posl):
    c = 1
    for i in posl:
        c *= i
    return c
print('Произведение введенных чисел:', proiz_chis(posl_c))

# - среднее арифметическое (не считая завершающего числа 0)
def srar_chis(posl):
    x = sum(posl)
    z = 0
    for i in posl:
        z += 1
    s = x / z
    return s
print('Среднее арифметическое введенных чисел:',srar_chis(posl_c))

# - определить значение и порядковый номер наибольшего элемента последовательности. Если наибольших элементов несколько,
# выведите порядковый номер первого из них.
def max_chis(posl):
    m = 0
    for i in posl:
        if i > m:
            m = i
    x = posl.index(m)
    return {'Индекс максимального:': x, 'Максимальное число:': m}
print(max_chis(posl_c))

# - определить количество чётных и не чётных элементов в последовательности
def chet_nechet_chis(posl):
    chet = 0
    nechet = 0
    for i in posl:
        if i % 2 == 0:
            chet += 1
        else:
            nechet += 1
    return {'Количество четных:': chet, 'Количество нечетных:': nechet}
print(chet_nechet_chis(posl_c))

# - определить значение второго по величине элемента в этой последовательности
def max2_chis(posl):
    m = 0
    m2 = 0
    for i in posl:
        if i > m:
            m = i
    posl.remove(m)
    for z in posl:
        if z > m2:
            m2 = z
    return m2
print('Второй по величине:', max2_chis(posl_c))

# - определите, сколько элементов этой последовательности равны ее наибольшему элементу
def ravn_max_chis(posl):
    m = 0
    col = 0
    for i in posl:
        if i > m:
            m = i
    for z in posl:
        if z == m:
            col += 1
    return col
print('Количество равных максимуму:', ravn_max_chis(posl_c))
