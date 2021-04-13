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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.history = []

    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        commission = self.withdraw(amount, True)
        target_account.deposite(amount)
        self.history_add(f'Перевод клиенту {target_account.name} {amount} руб. Текущий баланс: {self.balance} руб. Комиссия составила {commission} руб.')

    def deposite(self, amount):
        """
         Внесение суммы на текущий счет
         :param amount: сумма
         """
        self.balance += amount
        self.history_add(f'Пополнение баланса на {amount} руб. Текущий баланс: {self.balance} руб.')

    def withdraw(self, amount, transaction=False):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.balance < amount:
            raise ValueError("Недостаточно средств на счете")

        self.balance -= amount
        commission = self.get_commission(amount)
        if not transaction:
            self.history_add(f'Списание баланса на {amount} руб. Текущий баланс: {self.balance} руб. Комиссия составила {commission} руб.')
            return

        return commission

    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        return f"{self.name} баланс: {self.balance} руб. Паспорт: {self.passport8} т.{self.phone_number}"

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.balance} руб."

    def history_add(self, action):
        self.history.append(action)

    def get_history(self):
        return self.history

    def get_commission(self, amount):
        commission = amount * 0.02
        self.balance -= commission
        return commission


account_ivan = Account('Ivan', 12345678, '+79518796508')
account_andrey = Account('Andrey', 12345654, '+79518796580')

print(account_ivan)
print(account_andrey)

account_ivan.deposite(1000)
print(account_ivan)
print(account_andrey)

try:
    account_ivan.transfer(account_andrey, 100)
except ValueError as exp:
    print(exp)
print(account_ivan)
print(account_andrey)

print(account_ivan.get_history())
print(account_andrey.get_history())

