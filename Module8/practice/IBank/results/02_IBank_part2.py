# Сюда отправляем готовое решение IBank часть-2

import datetime
from abc import ABC, abstractmethod

EMPLOYEE_PASSWORD = "123"
COMMISSION = 2

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
        :param target_account: счет клиента для перевода
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
        return f"At your account {self.name}, passport {self.passport8} mobile number {self.phone_number} has money: {self.balance} "


class Account(AccountBase):
    def __init__(self, *args, **kwargs):
        AccountBase.__init__(self, *args, **kwargs)
        self.history = [datetime.datetime.now()]


    def transfer(self, target_account, amount,comission):
        self.withdraw(amount)
        target_account.deposite(amount+ amount*comission)
        self.history.append(str(datetime.datetime.now())+" transfer "+ str(amount)+str(target_account.passport8)+ "com:"+str(comission))

    def deposite(self, amount):
        if self.phone_number:
            self.balance += amount
            self.history.append(str(datetime.datetime.now())+" deposite "+str(amount))

    def withdraw(self, amount):
        if self.phone_number:
            if self.balance < amount:
                raise ValueError('Not enough money')
            self.balance -= amount
            self.history.append(
            str(datetime.datetime.now()) + " withdraw " + str(amount))

    def full_info(self):
        return f"At your account {self.name}, passport {self.passport8} mobile number {self.phone_number} has money: {self.balance} "

    def __repr__(self):

        return f"At your account {self.name}, passport {self.passport8}  has money: {self.balance} "


account = Account("Jake", 44444444, +79893332323)
account1 = Account("Michelle", 333333, +79893332323)
account.deposite(50000)
print(account)
try:
    account.transfer(account1, 450000, 2)
except ValueError as e:
    print(e)
account.withdraw(343)
print(account)
print(account1)
print(account.history)
