# Сюда отправляем готовое решение IBank часть-2
import re


def validate_passport(passport):
    pattern = r"\d{4} \d{6}"
    return re.match(pattern, passport)


def validate_phone_number(phone_number):
    pattern = r"[+]7-\d{3}-\d{3}-\d{2}-\d{2}"
    return re.match(pattern, phone_number)


class Operation:
    # класс для хранение информации об операциях
    def __init__(self, operation, amount, account=None):
        # Тут добавляем свойства для хранение информации об операции
        self.operation = operation
        self.amount = amount
        self.account = account

    def __repr__(self):
        add_str = ''
        if self.operation == "ПЕРЕВОД":
            add_str = f' на счет клиента: {self.account.name}'
        if self.operation == "ПОСТУПЛЕНИЕ":
            add_str = f' со счета клиента: {self.account.name}'
        return f'{self.operation} {self.amount} руб.' + add_str


class Account:
    # TODO: сюда копируем реализацию класса Account из предыдущей задачи
    # TODO: историю храним как список объектов класса Operation, добавив свойство в конструктор:
    #   self.__history = []
    def __init__(self, name, passport, phone_number, start_balance=0):
        self.name = name
        if validate_passport(passport):
            self.passport = passport
        else:
            raise ValueError('Некорректный номер паспорта')
        if validate_phone_number(phone_number):
            self.phone_number = phone_number
        else:
            raise ValueError('Некорректный номер телефона')
        self.__balance = start_balance
        self.__history = []

    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        self.withdraw(amount)
        target_account.deposit(amount)
        self.__history.pop()
        self.__history.append(Operation("ПЕРЕВОД", amount, target_account))
        target_account.__history.pop()
        target_account.__history.append(Operation("ПОСТУПЛЕНИЕ", amount, self))

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        self.__balance += amount
        self.__history.append(Operation("ПОПОЛНЕНИЕ", amount))

    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.__balance - amount < 0:
            raise ValueError('Недостаточно средств на счету')
        self.__balance -= amount
        self.__history.append(Operation("СНЯТИЕ", amount))

    def full_info(self):
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 3200 123456 т.+7-900-200-02-03"
        """
        return f'{self.name} баланс: {self.__balance} руб. паспорт: {self.passport} т.{self.phone_number}'

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иван баланс: 100 руб."
        """
        return f'{self.name} баланс: {self.__balance} руб.'

    def show_history(self):
        """
        :return: возвращаем историю операций в виде строки, в указанном формате
        """
        for operation in self.__history:
            print(operation)


account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 1000)
account2 = Account("Алексей", "3232 456124", "+7-901-744-22-99", 200)
account1.deposit(300)
account1.withdraw(100)
account1.transfer(account2, 500)
account1.show_history()
account2.show_history()
