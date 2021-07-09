# from generators import get_user_data
from abc import ABC, abstractmethod
import re

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
    def __init__(self, name, passport8, phone_number, start_balance=0):
        if len(str(passport8)) < 8:
            raise ValueError("Паспорт: недостаточно символов")
        if not re.match("\+7-9\d{2}-\d{3}-\d{2}-\d{2}", phone_number):
            raise ValueError("Телефон: ошибочный формат телефона")
        if len(passport8) < 8:
            raise ValueError("Паспорт: недостаточно символов")
        super().__init__(name, passport8, phone_number, start_balance)

    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        if self.balance < amount:
            raise ValueError("Сумма перевода больше суммы баланса")
        self.balance -= amount
        target_account.balance += amount

    def deposit(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        if amount < 0:
            raise ValueError("Нельзя пополнить на отрицательную сумму")
        self.balance += amount

    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if amount < 0:
            raise ValueError("Нельзя снять отрицательную сумму")
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
        name_split = self.name.split(sep=" ")
        for i in range(len(name_split)):
            if i == 0:
                short_name = name_split[i] + ' '
                continue
            short_name += name_split[i][0] + '.'

        return f"{short_name} баланс: {self.balance} руб."


acc1 = Account("Иванов Петр Сидорович", "11111111", "+7-999-123-45-67")
print(acc1)
