# Написать функцию которая вернет строку введенную пользователем.
# Обернуть функцию в декоратор чтобы функция вместо строки целиком вернула список слов.

user_string = input('Enter string - ')


def decorate(func):
    def str_to_list(*args, **kwargs):
        return func(*args, **kwargs).split()
    return str_to_list


@decorate
def show_the_string(string):
    return string


print(show_the_string(user_string))
