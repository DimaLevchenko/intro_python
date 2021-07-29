# Написать программу которая будет работать с открытыми данными регистрации транспортных средств.
# Официальные данные транспортных средств состоянием на 1е апреля 2021г., можно скачать
# https://data.gov.ua/dataset/0ffd8b75-0628-48cc-952a-9302f9799ec0/resource/c5cb530d-0533-40be-b9ad-f03e06c94b10/
# download/tz_opendata_z01012021_po01042021.zip
# Написать программу которая принимает параметры:
# o - имя файла с данными в формате csv (обязательный параметр)
# Опциональные параметры:
# --brand Марка авто
# --color Цвет авто
# --year Год выпуска авто
# --fuel Топливо
# Если все опциональные параметры None - программа завершает выполнение.
# С учетом выбраных опциональных параметров, например brand=Toyota; year=2012
# программа выгружает в новый csv файл колонки:
# D_REG BRAND MODEL COLOR MAKE_YEAR FUEL NEW_REG_NEW
# Название файла должно включать в себя выбранные параметры, например:
# brand-toyota-year-2012.csv
# Просьба не выгружать в гитхаб csv файл который прикреплен. Файлы которые сгенерировала программа - можно.
# ** доп задание. добавить опциональный параметр --reg_num, если он есть программа просто печатет те строки
# (с учетом колонок выше) в которых reg_num содержится в NEW_REG_NEW


