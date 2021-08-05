# Написать функцию которая вернет самое длинное слово в строке:
# longest_word("What makes a good man") -> makes

your_string = input('Input your string - ')


def longest_word(string):
    new_list = string.split()
    maximum = max(new_list, key=len)
    return maximum


print('The longest word - ', longest_word(your_string))
