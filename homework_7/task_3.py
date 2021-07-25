# Получить прогноз погоды для Одессы на следующие 5 дней и записать в файл с именем текущей даты,
# http://api.openweathermap.org/data/2.5/forecast/daily?q=city&cnt=1&units=metric&appid=f9ada9efec6a3934dad5f30068fdcbb8
# Параметр cnt = количество дней
# Параметр q = город
# Так мы получим и обработаем дату из ответа(ключ dt):
# datetime.datetime.fromtimestamp(1600419600)
# Применив к полученному обьекту даты strftime("%d-%m-%Y") получим строковую дату для записи в файл.
# Пример имени файла: 19 - 09 - 2020 - Odessa - 5 - days - weather - forecast.txt
# *доп.предоставить пользователю выбор города и количества дней, а также добавить колонку Температура ночью

import requests
import datetime
city = input('Please, enter the city - ')
days = int(input('Enter the number of days - '))
app_id = 'f9ada9efec6a3934dad5f30068fdcbb8'


def get_file():
    r = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?',
                     params={'q': city, 'cnt': days, 'units': 'metric', 'appid': app_id})
    return r.json()


def get_inform():
    inform = get_file()
    big_list = []
    head_str = ['Date', 'Daytime temperature', 'Temperature at night', 'Feels like temperature']
    big_list.append(head_str)
    for k in inform['list']:
        small_list = []
        date = datetime.datetime.fromtimestamp(k['dt'])
        str_date = date.strftime('%d-%m-%Y')
        small_list.append(str_date)
        small_list.append(str(k['temp']['day']))
        small_list.append(str(k['temp']['night']))
        small_list.append(str(k['feels_like']['day']))
        big_list.append(small_list)
    return big_list


def get_filename():
    inform = get_file()
    date = datetime.datetime.fromtimestamp(inform['list'][0]['dt'])
    str_date = date.strftime('%d-%m-%Y')
    filename = [str(str_date), str(inform['city']['name']), str(inform['cnt'])]
    name = '-'.join(filename)
    return name


def modify_inform():
    inform = get_inform()
    mod_inform = []
    for data in inform:
        mod_data = []
        for value in data:
            mod_value = value.ljust(25)
            mod_data.append(mod_value)
        mod_inform.append(mod_data)
    return mod_inform


def create_file():
    with open(f'{get_filename()}-days-weather-forecast.txt', 'w') as file:
        inform = modify_inform()
        for data in inform:
            file.write(''.join(data) + '\n')


def main():
    get_file()
    get_filename()
    create_file()


main()
