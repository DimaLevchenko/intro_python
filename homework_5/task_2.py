#Написать программу которая вернет количество введенных пользователем слов и общее число символов.

s = input('Ввод: ')

w = 0
z = s.split()
for i in z:
    w += 1
print('Число введенных слов: ', w)

q = 0
for i in s:
    q += 1
print('Общее число введенных символов: ', q)
