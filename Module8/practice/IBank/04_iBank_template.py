# from generators import get_user_data
from abc import ABC, abstractmethod


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
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"..."

class Account(AccountBase):

    def deposite(self, amount):
        self.balance += amount

    def transfer(self, target_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            target_account.balance += amount
        else:
            print("Недостаточно средств на счете")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Недостаточно средств на счете")

    def full_info(self):
        return f'{self.name} баланс {self.balance} руб. паспорт: {self.passport8} т.{self.phone_number}'

    def __repr__(self):
        name_list = self.name.split(' ')
        name = f'{name_list[0]} {name_list[1][0]}.{name_list[2][0]}.'
        return f'{name} баланс {self.balance} руб.'


acc1 = Account("Иванов Иван Иванович", 10101010, 89000000001)
acc1.deposite(100)
print(acc1)
print(acc1.full_info())
acc2 = Account("Иванов Петр Иванович", 10101011, 89000110001)
acc1.transfer(acc2, 50)
print(acc2)
