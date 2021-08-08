# Описать класс "Банковский счет", атрибуты у которого:
#    имя аккаунта - str
#    уникальный id (uuid)
#    баланс float
#    транзакции (список)
# Методы
#     депозит средств
#     вывод средств
#     получить баланс
#   При изменении баланса записывать в транзакции (сумма, тип операции, текущая_дата)
#   * доп. добавить и учитывать банковские комиссии (1%)

from uuid import uuid4
from datetime import datetime


class BankAccount:
    def __init__(self, name: str, balance: float):
        self.name = name
        self.id = uuid4()
        self.balance = balance
        self.transaction = []

    def operations(self, operation: float):
        commission = 0.01
        sum_of_commission = operation * commission
        sum_of_operation = operation - sum_of_commission
        return sum_of_operation

    def deposit(self, operator: float):
        self.balance += self.operations(operator)
        self.transaction.append([self.operations(operator), 'deposit', datetime.today().strftime('d%-%m-%Y')])
        answer = f'Your deposit is {self.operations(operator)}, your balance is {self.balance}'
        return answer

    def withdrawal(self, operator: float):
        self.balance -= self.operations(operator)
        self.transaction.append([self.operations(operator), 'withdrawal', datetime.today().strftime('d%-%m-%Y')])
        answer = f'Your withdrawal is {self.operations(operator)}, your balance is {self.balance}'
        return answer

    def get_balance(self):
        answer = f'Your balance is {self.balance}'
        return answer


first_account = BankAccount('First', 1000)
