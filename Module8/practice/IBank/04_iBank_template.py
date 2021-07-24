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
    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        if type(amount) is not int or amount <= 0:
            raise TypeError("Сумма для перевода должна быть числом больше 0")
        if self.balance < amount:
            raise ValueError("На счёте недостаточно средств")
        target_account.balance += amount
        self.balance -= amount

    def deposite(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        if type(amount) is not int or amount <= 0:
            raise TypeError("Сумма для перевода должна быть числом больше 0")
        self.balance += amount

    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if type(amount) is not int or amount <= 0:
            raise TypeError("Сумма для перевода должна быть числом больше 0")
        if self.balance < amount:
            raise ValueError("На счёте недостаточно средств")
        self.balance -= amount

    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        return f"{self.name} баланс: {self.balance} руб. паспорт: {self.passport8} т. {self.phone_number}"

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.balance} руб."


account1 = Account("Иван", 1234, "...")
account2 = Account("Пётр", 5678, "...", start_balance=300)
print(account1.full_info())
account1.deposite(100)
print(account1.full_info())
account1.transfer(account2, 100)
print(account1.full_info())
print(account2.full_info())
