# Во вложении есть json файл. Написать программу которая прочитает его и посчитает общую длительность
# всех треков в альбоме.
# Базовый кейс - вернет количество секунд.
# * доп. усложнение вернуть в виде строки часы:минуты:секунды, прим. '0:41:39' (datetime.timedelta)

import json
from datetime import timedelta


def get_time():
    with open('acdc.json', 'r') as file:
        pars_file = json.load(file)
        indict = pars_file.get('album').get('tracks').get('track')
        dur = []
        for duration in indict:
            dur.append(int(duration['duration']))
        td = timedelta(seconds=sum(dur))
    return td


print(get_time())
