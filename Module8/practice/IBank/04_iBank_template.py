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
        if target_account.phone_number and amount < self.balance:
            target_account.balance += amount
            self.balance -= amount
        else:
            print("На счете недостаточно средств")
    
    def deposite(self, amount):
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
            print("На счете недостаточно средств")
        else:
            self.balance -= amount
    
    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        return f"{self.name} баланс: {self.balance} руб. паспорт: {self.passport8} т.{self.phone_number}"
        
    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.balance} руб."

acc = Account("name", 2222222, 34343434)
acc2 = Account("name2", 4242424, 12312333)
print(acc)
print(acc.full_info())
acc.deposite(1000)
print(acc)
acc.withdraw(500)
print(acc)
acc.withdraw(5000)
print(acc)
acc.transfer(acc2, 300)
print(acc)
print(acc2)
acc.transfer(acc2, 4444)
