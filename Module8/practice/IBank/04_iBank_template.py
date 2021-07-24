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
        if amount > self.balance:
            raise ValueError('Недостаточно средств на счете')
        self.balance -= amount
        target_account.balance += amount

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
        if amount > self.balance:
            raise ValueError('Недостаточно средств на счете')
        self.balance -= amount


    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        return f'Имя: {self.name}; баланс {self.balance}; Номер паспорта: {self.passport8}; тел.{self.phone_number}'

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.balance}"


account1 = Account('Иван', 12345678, '+7-999-556-18-54', 100)
account2 = Account('Петр', 23456781, '+7-999-985-17-45', 500)
account3 = Account('Василий', 34567812, '+7-989-915-77-45', 1000)
account4 = Account('Алексей', 45678123, '+7-989-915-77-45', 5000)

print('Перевод денег - 10 руб')
account1.transfer(account2, 10)
# print(account1.full_info())
# print(account2.full_info())
print(f'{account1 = }')
print(f'{account2 = }')

print('Положить на депозит 500руб')
account1.deposit(500)
# print(account1.full_info())
print(f'{account1 = }')

print('Снять 20руб')
account1.withdraw(20)
# print(account1.full_info())
print(f'{account1 = }')
