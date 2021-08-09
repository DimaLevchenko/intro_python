# Написать программу кофейный магазин.
# Обьекты:
#    Product
#    - свойства: наименование, тип, цена
#    - print обьекта продукта должен возвращать прим. "Кофе: Эспрессо, цена: 27грн."
#    Store
#    - может импортировать продукты из файла invertory.csv
#    (по-умолчанию по 5 шт. каждого наименования)
#    - может вернуть список продуктов нужного типа (tea, coffee или все продукты)
#    - может вернуть общую стоимость продуктов в наличии
#    - может продать продукт
# *доп. Научить Store запоминать выручку (сумма проданных продуктов) и выводить баланс.
# Тип продукта может быть только coffee или tea (нельзя создать обьект с другим типом).

import csv


class Store:
    def __init__(self):
        self.list_of_product = []
        self.times_import = 5
        self.list_of_sale = []

    def reader(self):
        with open('inventory.csv', encoding='utf-8') as file:
            file_reader = csv.reader(file, delimiter=',')
            next(file_reader)
            for lines in file_reader:
                self.list_of_product.append(lines)
            self.list_of_product *= self.times_import
            answer = f'Общий список продуктов: {self.list_of_product}'
        return answer

    def type_of_product(self, type=None):
        list_of_type = []
        for lines in self.list_of_product:
            if lines[1] == type:
                list_of_type.append(lines)
            elif type == None:
                list_of_type.append(lines)
        answer = f'Список указанных продуктов: {list_of_type}'
        return answer

    def sum_of_cost(self):
        sum = 0
        for lines in self.list_of_product:
            sum += int(lines[2])
        answer = f'Стоимость продуктов в наличии: {sum}'
        return answer

    def sale(self, name: str):
        for lines in self.list_of_product:
            if lines[0] == name:
                self.list_of_product.remove(lines)
                self.list_of_sale.append(lines)
                break
        answer = f'Список проданных продуктов: {self.list_of_sale}'
        return answer

    def balance(self):
        balance = 0
        for lines in self.list_of_sale:
            balance += int(lines[2])
        answer = f'Выручка проданных продуктов: {balance}'
        return answer


class Product(Store):
    # вытягиваем продукт с магазина (уже существующий)
    def take(self, type: str):
        properties = ['name', 'type', 'cost']
        for lines in self.list_of_product:
            if lines[1] == type:
                result = dict(zip(properties, lines))
                return result

    def print_product(self, name: str):
        for lines in self.list_of_product:
            if lines[0] == name:
                answer = f'{lines[1]}: {lines[0]}, cost: {lines[2]}'
                return answer


s = Store()
print(s.reader())
print(s.type_of_product('tea'))
print(s.type_of_product())
print(s.sum_of_cost())
print(s.sale('Эспрессо'))
print(s.sum_of_cost())
print(s.sale('Имбирный чай'))
print(s.sum_of_cost())
print(s.balance())

p = Product()
p.reader()
print(p.take('tea'))
print(p.print_product('Earl Grey'))
