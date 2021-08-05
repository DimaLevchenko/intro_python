# Написать функцию которая заменит в тексте слово на другое.
# Функция принимает 4 аргумента, изначальная строка, заменяемое слово, новое слово, количество замен, пример:
# fake_string('DC makes good movies, DC makes good comics', 'DC', 'Marvel', 1) ->
# 'Marvel makes good movies, DC makes good comics'
# fake_string('DC makes good movies, DC makes good comics', 'DC', 'Marvel', 2) ->
# 'Marvel makes good movies, Marvel makes good comics'

your_string = input('Input your string - ')
word_for_remove = input('Removed word - ')
new_word = input('New word - ')
replaced_count = input('Number of replacements - ')


def fake_string(string, rem_word, n_word, count):
    new_string = string.replace(rem_word, n_word, int(count))
    return new_string


print('New string -', fake_string(your_string, word_for_remove, new_word, replaced_count))
