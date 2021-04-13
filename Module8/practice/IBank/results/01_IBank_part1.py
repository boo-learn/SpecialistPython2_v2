# Сюда отправляем готовое решение IBank часть-1
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

    def transfer(self, target_account, amount):
        if target_account.phone_number:
            if self.balance > amount:
                self.balance -= amount
                target_account.balance += amount

    def deposite(self, amount):
        if self.phone_number:
            self.balance += amount

    def withdraw(self, amount):
        if self.phone_number:
            if self.balance > amount:
                self.balance -= amount
            else:
                print("not enough money")

    def full_info(self):
        print(self)

    def __repr__(self):

        return f"At your account {self.name}, passport {self.passport8} mobile number {self.phone_number} has money: {self.balance} "



account = Account("Jake",44444444,+79893332323)
account.deposite(50000)

account.full_info()
