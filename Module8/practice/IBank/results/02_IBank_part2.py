# Сюда отправляем готовое решение IBank часть-2
#!/usr/bin

import datetime
# from generators import get_user_data
from abc import ABC, abstractmethod

EMPLOYEE_PASSWORD = "123"


class AccountBase(ABC):
    def __init__(self, name, passport8, phone_number, start_balance=0):
        self.name = name
        self.passport8 = passport8
        self.phone_number = phone_number
        self.balance = start_balance

    @abstractmethod
    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: аккаунт клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        pass

    @abstractmethod
    def deposite(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        pass

    @abstractmethod
    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        pass

    @abstractmethod
    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        return f"..."

    @abstractmethod
    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"..."


class Account(AccountBase):
    def __init__(self, name, passport8, phone_number, start_balance=0):
        self.name = name
        try:
            self.__passport8 = int(passport8)
        except ValueError:
            raise ValueError("Номер паспорта должен быть целым числом")
        self.phone_number = phone_number
        self.balance = start_balance
        self.history = []
        self.is_closed = False

    @property
    def passport8(self):
        return self.__passport8

    @passport8.setter
    def passport8(self, value):
        try:
            self.__passport8 = int(value)
        except ValueError:
            raise ValueError("Номер паспорта должен быть целым числом")

    def change_history(self, amount):
        string = f"({self.phone_number}, {amount}, {str(datetime.datetime.now())})"
        self.history.append(string)

    def deposite(self, amount):
        self.balance += amount
        self.change_history(amount)

    def transfer(self, target_account, amount):
        self.withdraw(amount)
        target_account.deposite(amount)

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("На счете недостаточно средств")
        else:
            self.balance -= amount
            self.change_history(amount)

    def full_info(self):
        return f"{self.name}: {self.balance} руб. паспорт: {self.__passport8} т.{self.phone_number}"

    def close_account(self):
        self.is_closed = True
        string = f"({self.name}, {str(self.phone_number)}, {})"
        self.history.append(string)

    def show_history(self):
        for elem in self.history:
            print(elem)

    def __repr__(self):
        return f"{self.name} баланс: {self.balance} руб."


account_ivan = Account(name="Иван", passport8=12345678, phone_number="911", start_balance=200)
account_vasya = Account(name="Василий", passport8=12345679, phone_number="811", start_balance=1000)

new_passport = input("New passport: ")
account_ivan.passport8 = new_passport
