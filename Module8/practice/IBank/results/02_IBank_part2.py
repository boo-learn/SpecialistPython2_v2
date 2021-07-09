# from generators import get_user_data
from abc import ABC, abstractmethod
import re
import math

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
    FEE_WITHDRAW = 0.02

    def __init__(self, name, passport8, phone_number, start_balance=0):
        if len(str(passport8)) < 8:
            raise ValueError("Паспорт: недостаточно символов")
        if not re.match("\+7-9\d{2}-\d{3}-\d{2}-\d{2}", phone_number):
            raise ValueError("Телефон: ошибочный формат телефона")
        if len(passport8) < 8:
            raise ValueError("Паспорт: недостаточно символов")
        self.history = [f"Создан счет, первоначальная сумма пополнения {start_balance}"]
        self.active = True
        super().__init__(name, passport8, phone_number, start_balance)

    def __eq__(self, other):
        if self.passport8 == other.passport8:
            return True
        return False

    def close(self):
        self.active = False

    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        self.withdraw(amount, add_log=False)
        target_account.deposit(amount, add_log=False)
        target_account.history.append(f"Перевод от клиента {self.name}, сумма {amount}")
        self.history.append(f"Перевод клиенту {target_account.name}, сумма {amount}")

    def deposit(self, amount, add_log=True):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        if amount < 0:
            raise ValueError("Нельзя пополнить на отрицательную сумму")
        self.balance += amount
        if add_log:
            self.history.append(f"Пополнение счета на сумму {amount}")

    def withdraw(self, amount, add_log=True):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if amount < 0:
            raise ValueError("Нельзя снять отрицательную сумму")
        if self.balance < amount:
            raise ValueError("Сумма снятия превышает баланс")
        fee = round(amount * self.FEE_WITHDRAW, 2)
        self.balance -= amount + fee
        # if add_log:
        self.history.append(f"Снятие со счета суммы {amount}, комиссия {fee}")

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

    def account_statement(self):
        statement = ""
        for record in self.history:
            statement += f"{str(record)}\n"
        return statement


class Bank:
    def __init__(self):
        self.accounts = []

    def open_account(self, account):
        self.accounts.append(account)

    def close_account(self, account):
        self

if __name__ == "__main__":
    acc1 = Account("Иванов Петр Сидорович", "11111111", "+7-999-123-45-67")
    print(acc1)
    acc1.deposit(300)
    acc1.withdraw(17)
    print(acc1.account_statement())
