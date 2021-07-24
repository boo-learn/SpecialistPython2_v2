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
        self.withdraw(amount)
        target_account.deposit(amount)

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
        if self.balance < amount:
            raise ValueError("На счёте недостаточно средств")
        self.balance -= amount

    def full_info(self):
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        return f"{self.name} баланс:{self.balance} руб. паспорт: {self.passport8} т.{self.phone_number}"

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иван баланс: 100 руб."
        """
        return f"{self.name} баланс:{self.balance} руб."


class CreditAccount(AccountBase):
    def __init__(self, name, passport8, phone_number, start_balance=0):
        AccountBase.__init__(self, name, passport8, phone_number, start_balance=0)
        ...
        ...
    
    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        self.withdraw((amount*(1+0.02)))
        target_account.deposit(amount)
        

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
        if self.balance < amount:
            raise ValueError("На счёте недостаточно средств")
        self.balance -= amount

    def full_info(self):
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        return f"{self.name} баланс:{self.balance} руб. паспорт: {self.passport8} т.{self.phone_number}"

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иван баланс: 100 руб."
        """
        return f"{self.name} баланс:{self.balance} руб."




account1 = CreditAccount("Иван", 12345678, "...")
account2 = CreditAccount("Петр", 12345678, "...")
print(account1)  # account.__str__()
account1.deposit(10000)
print(account1)
try:
    account1.withdraw(1000)
except ValueError as e:
    print(e)
print(account1)
try:
    account1.transfer(account2, 500)
    print(f"{account1=}")
    print(f"{account2=}")
    account1.transfer(account2, 500)
    print(f"{account1=}")
    print(f"{account2=}")    
    account1.transfer(account2, 500)
    print(f"{account1=}")
    print(f"{account2=}")
except ValueError as e:
    print(e)
