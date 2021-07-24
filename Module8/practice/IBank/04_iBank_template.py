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
    def __init__(self, name, passport8, phone_number, start_balance=0, operation_history=[]):
        AccountBase.__init__(self, name, passport8, phone_number, start_balance=0)
        self.operation_history = operation_history

    def history_append(self):
        self.operation_history.append()

    def transfer(self, target_account, amount):
        self.withdraw(amount)
        target_account.deposit(amount)
        

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Isn't enough money")
        interest = amount * 0.02
        self.balance -= amount + interest

    def full_info(self):
        return f"{self.name} баланс: {self.balance} руб. паспорт: {self.passport8} т.{self.phone_number}"

    def __repr__(self):
        return f"{self.name} баланс: {self.balance} руб."



class KreditAcc(Account):
    def __init__(self, name, passport8, phone_number, start_balance=0, negative_limit=-1000):
        Account.__init__(self, name, passport8, phone_number, start_balance=0)
        self.__negative_limit = negative_limit
        
    def __repr__(self):
        return f"{self.name} K-account баланс: {self.balance} руб."

    def withdraw(self, amount):
        if self.balance > self.__negative_limit:
            raise ValueError("Isn't enough money")
        if 0 > self.balance - amount > self.__negative_limit:
            interest = amount * 0.05
            self.balance -= amount + interest
        interest = amount * 0.02
        self.balance -= amount + interest
        
    def transfer(self, target_account, amount):
        self.withdraw(amount)
        target_account.deposit(amount)
