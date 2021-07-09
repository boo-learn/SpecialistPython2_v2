# Сюда отправляем готовое решение IBank часть-2
# from generators import get_user_data
from abc import ABC, abstractmethod


class AccountBase(ABC):
    def __init__(self, name, passport8, phone_number, start_balance=0):
        self.name = name
        self.passport8 = passport8
        self.phone_number = phone_number
        self.balance = start_balance

    # @property
    # @abstractmethod
    # def name(self):
    #     pass

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
    def __init__(self, name, passport8, phone_number, start_balance=0):
        super().__init__(name, passport8, phone_number, start_balance)
        self.history = []

    def transfer(self, target_account, amount):
        self.withdraw(amount)
        target_account.deposit(amount)


    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Сумма должна быть положительная")
        self.balance += amount
        # self.history('deposit', amount)

    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if amount > self.balance:
            raise ValueError("Не достаточно денег насчёте")
        self.balance -= (amount + amount*0.02)
        self.history('withdraw', amount)
    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        return f"{self.name} баланс: {self.balance} руб. паспорт:{self.passport8} т.{self.phone_number}"

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.balance} руб."

    def history(self, type, amount):
        self.history.append(type, amount)


# if __name__ == "__name__":
account1 = Account("Иван", 12345678, "+79006001112")
account2 = Account("Алексей", 22345678, "+79006001212")

account1.deposit(500)
try:
    account1.withdraw(300)
except ValueError as e:
    print(e)
print(account1)
try:
    account1.withdraw(300)
except ValueError as e:
    print(e)
print(account1)

print(account1.history)
    # account1.transfer(account2, 500)
