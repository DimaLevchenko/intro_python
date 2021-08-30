# Формат украинских номеров:
# ВН1010НС или АА1010АА
# На ввод программа получает строку, в ответ должна вернуть является строка автомобильным номером или нет.
# * доп. Должна вернуть регион (должна знать регионы 2004 и 2013 гг.)
# Должна одинаково воспринимать AI - англ и АІ - украинский варианты.
# (для BI, AI, IA и т.д.)

import csv
import re


def region(num):
    with open('ua_auto.csv', 'r+', encoding='utf-8') as file:
        csv_file = csv.reader(file)
        name = ' '
        for row in csv_file:
            if row[1] == num[:2] or row[2] == num[:2]:
                name = row[0]
        return name


def auto(num):
    match = re.findall(r'([А-ЯA-Z]){2}\d{4}[А-ЯA-Z]{2}', num)
    if match:
        return f'It is the UA car number, the region is {region(num)}'
    else:
        return f'Not match!'


def main():
    auto_number = input('Enter UA car number to check it: ')
    region(auto_number)
    print(auto(auto_number))


main()
