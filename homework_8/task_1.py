# Написать приложение "Онлайн конвертер валют". =)
# Приложение спрашивает пользователя:
#   currency_from: string
#   currency_to: string
# Проверка ввода параметра валют (from, to) должна быть в symbols.json по ключу symbols)
#   amount: float
#   start_date: string
# (пример. 2020-09-22 если дата не в этом формате, выставлять по-умолчанию дату текущего дня,
#  если дата превышает текущий день, тоже выставляем дату текущего дня)
#  Если дата меньше или равна текущему дню, то от start_date до текущего идет итерация:
#  Приложение делает GET запрос:
#  https://api.exchangerate.host/convert
#  Принимаемые параметры from, to, amount, date
#  (from=USD&to=UAH&amount=10000.5&date=2020-09-18)
#  Итоговый вывод должен быть точно в таком же формате (пример если start_date == 2020-09-18):
#   [['date', 'from', 'to', 'amount', 'rate', 'result'],
#    ['2020-09-18', 'USD', 'UAH', 10000.5, 28.163466, 281648.743085],
#    ['2020-09-19', 'USD', 'UAH', 10000.5, 28.163466, 281648.737791],
#    ['2020-09-20', 'USD', 'UAH', 10000.5, 28.163455, 281648.630637],
#    ['2020-09-21', 'USD', 'UAH', 10000.5, 28.23733, 282387.419415],
#    ['2020-09-22', 'USD', 'UAH', 10000.5, 28.265772, 282671.854989]]
#    ** доп. задание. ввод данных должен приниматься парсингом аргументов, модуль
#       argparse.
#           Только --start_date опциональный параметр.
#           В итоге чтобы была возможность запустить приложение командой:
#           python exchange_rates.py USD UAH 100 --start_date 2020-09-18
# В данном случае пользователя спрашивать не нужно.

import argparse
import json
import datetime
import requests


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Exchange rates')
    parser.add_argument('currency_from', type=str, help='Initial currency. By default - USD.')
    parser.add_argument('currency_to', type=str, help='Final currency. By default - UAH.')
    parser.add_argument('amount', type=float, help='Amount')
    parser.add_argument('-sd', '--start_date', type=str, help='Optional: Exchange date. By default - today`s date')
    args = parser.parse_args()


def check_from_to():
    with open('symbols.json', 'r') as file:
        pars_file = json.load(file)
        symbol = pars_file.get('symbols')
        if args.currency_from not in symbol or args.currency_to not in symbol:
            print('Wrong enter! By default using currency from - USD, currency to - UAH.')
            args.currency_from = 'USD'
            args.currency_to = 'UAH'


def check_format_date():
    try:
        datetime.datetime.strptime(args.start_date, '%Y-%m-%d')
    except ValueError:
        args.start_date = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')


def check_date():
    script_date = datetime.datetime.strptime(args.start_date, '%Y-%m-%d')
    if script_date > datetime.datetime.now():
        args.start_date = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')


def get_file():
    script_date = datetime.datetime.strptime(args.start_date, '%Y-%m-%d')
    inform_list = [['Date', 'From', 'To', 'Amount', 'Rate', 'Result']]
    while script_date <= datetime.datetime.now():
        r = requests.get('https://api.exchangerate.host/convert?',
                         params={'from': args.currency_from, 'to': args.currency_to, 'amount': args.amount,
                                 'date': script_date})
        inform = r.json()
        inform_list.append([inform['date'], inform['query']['from'], inform['query']['to'], inform['query']['amount'],
                            inform['info']['rate'], inform['result']])
        script_date += datetime.timedelta(days=1)
    return inform_list


def main():
    check_from_to()
    check_format_date()
    check_date()
    print(get_file())


main()
