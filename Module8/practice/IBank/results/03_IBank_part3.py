# Сюда отправляем готовое решение IBank часть-3

from abc import ABC, abstractmethod
import re

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
        :param target_account: аккаунт клиента для перевода
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

    def __init__(self, name, passport8, phone_number, start_balance=0):
        self.name = name
        if re.fullmatch('\d{8}', passport8):
            self.__passport8 = passport8
        else:
            raise ValueError('Паспорт должен быть восьмизначным целым числом')
        if re.fullmatch('\+7\d{3}-\d{3}-\d{2}-\d{2}', phone_number):
            self.phone_number = phone_number
        else:
            raise ValueError('Телефон должен быть введен в формате "+7xxx-xxx-xx-xx"')
        self.balance = start_balance
        self.history = []
        str_history = f'Начальный баланс {start_balance}'
        self.history.append(str_history)
        self.closed = False
        self.commission_rate = 0.02

    @property
    def passport8(self):
        self.not_closed()
        return self.__passport8

    @passport8.setter
    def passport8(self, value):
        self.not_closed()
        try:
            self.__passport8 = int(value)
        except ValueError:
            raise ValueError("Номер паспорта должен быть целым числом")

    def not_closed(self):
        if self.closed:
            raise ValueError("Счет клиента закрыт")

    def deposite(self, amount):
        self.not_closed()
        self.balance += amount
        str_history = f'Пополнение на сумму {round(amount)}, баланс {round(self.balance)}'
        self.history.append(str_history)

    def transfer(self, target_account, amount):
        self.not_closed()
        self.withdraw(amount)
        target_account.deposite(amount)

    def withdraw(self, amount, limit=0):
        self.not_closed()
        commission = amount * self.commission_rate
        if amount + commission > self.balance + limit:
            raise ValueError("На счете недостаточно средств")
        else:
            self.balance -= amount
            self.balance -= commission
            str_history = f'Списание суммы {round(amount)}, баланс {round(self.balance)}'
            self.history.append(str_history)
            str_history = f'Списание комиссии {round(commission)}, баланс {round(self.balance)}'
            self.history.append(str_history)

    def close(self):
        self.not_closed()
        if self.balance:
            self.withdraw(self.balance / (1 + self.commission_rate))
        self.closed = True
        str_history = f'Счет закрыт'
        self.history.append(str_history)

    def get_history(self):
        return '\n'.join(self.history)

    def full_info(self):
        return f"{self.name}: {self.balance} руб. паспорт: {self.__passport8} т.{self.phone_number}"

    def __repr__(self):
        return f"{self.name} баланс: {self.balance} руб."


class Credit_Account(Account):

    def __init__(self, name, passport8, phone_number, start_balance=0, negative_limit=0):
        self.name = name
        if re.fullmatch('\d{8}', passport8):
            self.__passport8 = passport8
        else:
            raise ValueError('Паспорт должен быть восьмизначным целым числом')
        if re.fullmatch('\+7\d{3}-\d{3}-\d{2}-\d{2}', phone_number):
            self.phone_number = phone_number
        else:
            raise ValueError('Телефон должен быть введен в формате "+7xxx-xxx-xx-xx"')
        self.phone_number = phone_number
        self.balance = start_balance
        self.history = []
        str_history = f'Начальный баланс {start_balance}'
        self.history.append(str_history)
        self.closed = False
        self.limit = negative_limit
        str_history = f'Максимальный кредит {negative_limit}'
        self.history.append(str_history)
        self.commission_rate = 0.05

    def withdraw(self, amount):
        Account.withdraw(self, amount, self.limit)

    def close(self):
        self.not_closed()
        if self.balance < 0:
            self.deposite(-self.balance)
        Account.close(self)

    def full_info(self):
        return f"< K > {self.name}: {self.balance} руб. паспорт: {self.__passport8} т.{self.phone_number}"

    def __repr__(self):
        return f"< K > {self.name} баланс: {self.balance} руб."


account_ivan = Credit_Account(name="Иван", passport8="23451678", phone_number="+7911-900-00-00", start_balance=0, negative_limit=1000)
account_vasya = Account(name="Василий", passport8="12345679", phone_number="+7911-800-00-00", start_balance=1000)

# new_passport = input("New passport: ")
# account_ivan.passport8 = new_passport
#
# print(account_ivan.passport8)

account_ivan.deposite(500)
account_ivan.withdraw(1000)
account_ivan.transfer(account_vasya, 100)
print(account_ivan.full_info())
account_ivan.close()
print(account_ivan.get_history())

