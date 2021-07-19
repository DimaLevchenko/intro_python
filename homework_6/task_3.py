# Дан список значений. Вернуть словарь где каждый ключ - это индекс списка,
# а значение списка - это значение ключа:
# Input:
# ['a', 'b', 'c', 'd', 'e']
# Output
# {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'}

input_list = ['a', 'b', 'c', 'd', 'e']
print('Input - ', input_list)


def key(inp_li):
    k_li = []
    for i in inp_li:
        k_li.append(inp_li.index(i))
    return k_li


def output(ls1, ls2):
    di = {k: v for k, v in zip(ls1, ls2)}
    return di


print('Output - ', output(key(input_list), input_list))
