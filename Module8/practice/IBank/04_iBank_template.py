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
    def deposit(self, amount):
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
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        if amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
        else:
            raise ValueError("Не достаточно денег на счёте")

    def deposit(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Не достаточно денег на счёте")

    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        return f"{self.name} баланс: {self.balance} руб. " \
               f"паспорт:{self.passport8} тел. {self.phone_number}"

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.balance} руб."


obj = Account("Иванов Иван Петрович", 12345678, 89101234567, 500)
obj2 = Account("Сидоров Пётр Иванович", 87654321, 89167654321, 1000)
print(f"Первый аккаунт: {obj}")
print(f" Полная информация аккаунт 1: {obj.full_info()}")
print(f"Второй аккаунт: {obj2}")
print(f" Полная информация аккаунт 2: {obj2.full_info()}")
# obj.deposit(1000)
# print(obj)
# obj.withdraw(2500)
obj.transfer(obj2, 200)
print(f"Первый аккаунт: {obj}")
print(f"Второй аккаунт: {obj2}")
