# Программа которая при запуске должна:
# Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка. Каждая введённая строка, в файле, должна начинаться с новой строки.

filename = input('Enter filename - ')


def writ(name):
    with open(f'{name}.txt', 'w') as file:
        while True:
            data = input('Enter data: ')
            if data == '':
                break
            file.write(data+'\n')
        file.close()


writ(filename)
