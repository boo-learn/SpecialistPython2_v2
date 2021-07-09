# from generators import get_user_data
from abc import ABC, abstractmethod


class AccountBase(ABC):
    def __init__(self, name, passport, phone_number, start_balance=0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.balance = start_balance

    @abstractmethod
    def transfer(self, target_account, amount):
        if self.balance > amount:
            self.balance -= amount
            target_account += amount
        else:
            raise ValueError ('Недостаточно средств для вывода')

    @abstractmethod
    def deposit(self, amount):
        self.balance += amount


    @abstractmethod
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            raise ValueError ('Недостаточно средств для вывода')

    @abstractmethod
    def full_info(self):
        return f"{self.name} баланс: {self.balance} руб. паспорт {self.passport}"

    @abstractmethod
    def __repr__(self):
        return f"{account1.name} баланс {account1.balance} руб."

class Account(AccountBase):

    def transfer(self, target_account, amount):
        if self.balance > amount:
            self.balance -= amount
            target_account += amount
        else:
            raise ValueError ('Недостаточно средств для вывода')
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            raise ValueError ('Недостаточно средств для вывода')

    def full_info(self):
        return f"{self.name} баланс: {self.balance} руб. паспорт {self.passport}"

    def __repr__(self):
        return f"{account1.name} баланс {account1.balance} руб."

account1 = Account('Иванов И.П.', 1234566, 876543, 0)
account1.deposit(1000)

print(account1)
print(account1.full_info())
print(account1.withdraw((500)))



