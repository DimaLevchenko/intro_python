# Написать калькулятор температур.
# Пользователь вводит число и тип температуры (C, F, K - Цельсий, Фарренгейт, Кельвин соответственно)
# Программа должна вывести температуру в трех шкалах температур - Цельсий, Фарренгейт, Кельвин.

temp = int(input('Enter temperature - '))
type_temp = input('Enter type of temperature (C, F, K) - ')


def temp_calc(t, type_t):
    if type_t == 'C':
        t_c = t
        t_f = (9 / 5) * t + 32
        t_k = 273 + t
    elif type_t == 'F':
        t_c = (t - 32) * (5 / 9)
        t_f = t
        t_k = (t - 32) * (5 / 9) + 273
    elif type_t == 'K':
        t_c = t - 273
        t_f = (9 / 5) * (t - 273) + 32
        t_k = t
    else:
        print('Please, enter one of the suggested options!')
    list_type = ['C', 'F', 'K']
    list_t = [t_c, t_f, t_k]
    ans = {k: v for k, v in zip(list_type, list_t)}
    return ans


print(temp_calc(temp, type_temp))
