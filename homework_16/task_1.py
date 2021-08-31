# Во вложении файл csv с данными про аэропорты мира, написать программу которая сможет
# вернуть данные по таким параметрам:
# --iata_code - код аэропорта, должно вернуть 1 запись по коду аэропорта(всю строку)
# или вернуть ошибку AirportNotFoundError
# --country - страна, должно вернуть все записи по аэропортам или CountryNotFoundError
# --name - значение имени аэропорта, допустимо вхождение строки хотябы минимально,
# т.е. liman должен вернуть строки с такими названиями:
# Ilimanaq Heliport
# Sidi Slimane Airport
# Kilimanjaro International Airport
# West Kilimanjaro Airport
# Limanske Airfield
# Liman Airfield
# ...
# или AirportNotFoundError
# Только один параметр обязателен, если выбрано несколько - вернуть ошибку:
# MultipleOptionsError, если ни одного - NoOptionsFoundError
# ** доп. ошибки принимают два аргумента, текст ошибки и входные данные,
# пример:
# AirportNotFoundError: ('Airport not found', 'OESD')
# CountryNotFoundError: ('Country not found', 'UGUGU')
# IATA код может быть только 3х буквенным в верхнем регистре, сделать валидацию на него или вернуть IATACodeError

import csv
import argparse
from re import search


class CheckDataAirport:
    def __init__(self, iata_code=None, country=None, name=None):
        self.airport_data = self.airport_load_data()
        self.iata_code = iata_code
        self.country = country
        self.name = name

    def airport_load_data(self):
        with open('airport-codes_csv.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            return [line for line in csv_reader]

    def check_iata_code(self):
        for line in self.airport_data:
            if line['iata_code'] == self.iata_code.upper():
                return line
        raise AirportNotFoundError(self.iata_code, message='Airport not found')

    def check_country(self):
        airports = []
        for line in self.airport_data:
            if line['iso_country'] == self.country:
                airports.append(line)
        if not airports:
            raise CountryNotFoundError(self.country, message='Country not found')
        return airports

    def check_airport_name(self):
        names = []
        for line in self.airport_data:
            if search(self.name, line['name']):
                names.append(line['name'])
        if not names:
            raise AirportNotFoundError(self.name, message='Airport not found')
        return names

    def check_validation_iata_code(self):
        valid_code = self.iata_code.upper()
        if valid_code == self.iata_code:
            print('Valid code')
        else:
            raise IATACodeError


def check_args():
    if len([row for row in vars(args).values() if row is not None]) > 1:
        raise MultipleOptionsError(message='Just one parameter is necessary')
    if not len([row for row in vars(args).values() if row is not None]):
        raise NoOptionsFoundError(message='Parameters not found')


class IATACodeError(Exception):
    def __init__(self, iata_code, message='Not valid value'):
        self.iata_code = iata_code
        self.message = f'{iata_code} - {message}'
        super().__init__(self.message)


class CountryNotFoundError(Exception):
    def __init__(self, country, message='Country not found'):
        self.country = country
        self.message = f'{country} - {message}'
        super().__init__(self.message)


class AirportNotFoundError(Exception):
    def __init__(self, iata_data: str, message='Airport not found'):
        self.iata_data = iata_data
        self.message = f'{iata_data} - {message}'
        super().__init__(self.message)


class MultipleOptionsError(Exception):
    def __init__(self, message='Just one parameter is necessary'):
        self.message = message
        super().__init__(self.message)


class NoOptionsFoundError(Exception):
    def __init__(self, message='Parameters not found'):
        self.message = message
        super().__init__(self.message)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Checking data from airport')
    parser.add_argument('--iata_code', help='Three capital letter')
    parser.add_argument('--country', help='Name of a country')
    parser.add_argument('--name', help='Name of airport')
    args = parser.parse_args()
    check_args()
    test = CheckDataAirport(name=args.name, country=args.country, iata_code=args.iata_code)
