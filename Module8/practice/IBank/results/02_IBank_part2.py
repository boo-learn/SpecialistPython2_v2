# Сюда отправляем готовое решение IBank часть-2
# from generators import get_user_data
from abc import ABC, abstractmethod


class AccountBase(ABC):
    def __init__(self, name, passport8, phone_number, start_balance=0, type='normal'):
        self.name = name
        self.passport8 = passport8
        self.phone_number = phone_number
        self.balance = start_balance
        self.type = type

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
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"..."


class Account(AccountBase):
    def transfer(self, target_account, amount):
        self.withdraw(amount)
        target_account.deposite(amount)

    def withdraw(self, amount):
        if self.type=='normal':
            if amount <= self.balance:
                self.balance -= amount
            else:    
                raise ValueError('Недостаточно средств на счете.')
        else:
            self.balance -= amount
        

    def deposite(self, amount):
        self.balance += amount

    def full_info(self):
        return f"{self.name} баланс: {self.balance}. Паспорт: {self.passport8}. тел.: {self.phone_number}"

    def __repr__(self):
        return f"{self.name} баланс: {self.balance}."


account_ivan = Account("Ivan", 12345678, "+79008001122", 0, 'credit')
account_petr = Account("Petr", 12345677, "+79008001133")

account_ivan.deposite(500)
print(account_ivan)
print(account_petr)
print('**********')

try:
    account_ivan.transfer(account_petr, 1500)
except ValueError as e:
    print(e)
    
print(account_ivan)
print(account_petr)
