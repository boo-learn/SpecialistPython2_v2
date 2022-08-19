import math
from typing import List
import re
# Сюда отправляем готовое решение IBank часть-2

COMMISSION = 0.02 # 2%
# класс для хранение информации об операциях
class Operation:
    # Типы операций храним в свойствах класса
    DEPOSIT = 'Пополнение'
    WITHDRAW = 'Снятие'
    TRANSFER_OUT = 'Перевод'
    TRANSFER_IN = 'Поступление'

    # Напоминаю: обращение к этим переменным происходит через имя класса, пример: Operation.WITHDRAW

    def __init__(self, amount, type, related_account=None):
        # TODO: Тут добавляем свойства для хранение информации об операции
        self.amount = amount
        self.operation = type
        self.related_account = related_account

    def __repr__(self) -> str:
        """
        :return: возвращает строковое представление операции. Формат указан в 02_IBank_part2.md
        """
        if self.operation == Operation.DEPOSIT or self.operation == Operation.WITHDRAW:
            return f'{self.operation} {self.amount} руб.'
        elif self.operation == Operation.TRANSFER_OUT:
            return f'{self.operation} {self.amount} руб. на счет клиента: {self.related_account.name}'
        elif self.operation == Operation.TRANSFER_IN:
            return f'{self.operation} {self.amount} руб. со счета клиента: {self.related_account.name}'



class Account:
    # TODO: сюда копируем реализацию класса Account из предыдущей задачи
    # TODO: историю храним как список объектов класса Operation, добавив свойство в конструктор:
    #   self.__history = []
    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        self.name = name
        self.passport = self.check_passport(passport)
        self.phone_number = self.check_phone_number(phone_number)
        self.__balance = start_balance  # TODO: Закрываем прямой доступ к балансу
        self.__history = []

    def full_info(self) -> str:
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 3200 123456 т.+7-900-200-02-03"
        """
        return f"{self.name} баланс: {self.balance} руб. паспорт: {self.passport} т.{self.phone_number}"

    def __repr__(self) -> str:
        """
        :return: Информацию о счете в виде строки в формате "Иван баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.balance} руб."

    @property
    def balance(self) -> int:
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        self.__balance = new_balance

    def deposit(self, amount: int, to_history: bool = True) -> None:
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        :param to_history: True - записывать операцию в историю, False - не записывать
        """
        self.__balance += amount
        if to_history:
            self.__history.append(Operation(amount, Operation.DEPOSIT))

    def get_history(self) -> List[str]:
        """
        :return: возвращаем историю операций  виде списка строковых представлений
        """
        return [str(operation) for operation in self.__history]

    def commission(self, amount):
        commission = amount + math.floor(amount * COMMISSION)
        return commission

    def withdraw(self, amount: int, to_history: bool = True) -> None:
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        amount = self.commission(amount)
        if amount > self.balance:
            raise ValueError("У Вас недостаточно средств")
        self.balance -= amount
        if to_history:
            self.__history.append(Operation(amount, Operation.WITHDRAW))


    # TODO-1: напишите реализацию метода transfer()
    def transfer(self, target_account: 'Account', amount: int) -> None:
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        self.withdraw(amount, to_history=False)
        target_account.deposit(amount, to_history=False)

        transfer_in = Operation(amount, Operation.TRANSFER_IN, self)
        transfer_out = Operation(amount, Operation.TRANSFER_OUT, target_account)

        self.__history.append(transfer_out)
        target_account.__history.append(transfer_in)

    # Данный метод дан в готовом виде. Изучите его и используйте как пример, для доработки других

    def check_passport(self, passport):
        passport_rule = re.compile(r'\d{4}\s\d{6}') # yyyy xxxxxx
        if passport_rule.search(passport):
            self.passport = passport
            return self.passport
        else:
            raise ValueError(f'{passport} - неверно введён паспорт, требуется "yyyy xxxxxx"')

    def check_phone_number(self, number):
        number_rule = re.compile(r'[+7-9]\d{2}-\d{3}-\d{2}-\d{2}') #+7-9xx-xxx-xx-xx
        if number_rule.search(number):
            self.phone_number = number
            return self.phone_number
        else:
            raise ValueError(f'{number} - неверно введён номер телефона, требуется "+7-9xx-xxx-xx-xx"')
