# Сюда отправляем готовое решение IBank часть-2
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


class Operation:
    DEPOSIT = 'Пополнение '
    WITHDRAW = 'Списание '
    TRANSFER = 'Перевод '
    CLOSE = 'Закрытие счета '

    def __init__(self, type, amount, fee=0, target=None, source=None):
        self.type = type
        self.amount = amount
        self.fee = fee
        self.target = target
        self.source = source

    def __str__(self):
        if self.target is not None:
            target_name = 'на счет клиента: ' + self.target.name
        elif self.source is not None:
            target_name = 'со счета клиента: ' + self.source.name
        else:
            target_name = ''
        return f'{self.type}{self.amount:+.2f} {target_name}'


class Account(AccountBase):
    def __init__(self, name, passport8, phone_number, start_balance=0):
        AccountBase.__init__(self, name, passport8, phone_number, start_balance)
        self.history = []

    def transfer(self, target_account, amount, record=True):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """

        self.withdraw(amount, record=False)
        target_account.deposit(amount)
        if record:
            operation = Operation(Operation.TRANSFER, -amount, target=target_account)
            self.history.append(operation)
            operation = Operation(Operation.TRANSFER, amount, source=self)
            target_account.history.append(operation)

    def deposit(self, amount, record=True):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        self.balance += amount
        if record:
            operation = Operation(Operation.DEPOSIT, amount)
            self.history.append(operation)

    def has_money(self, amount):
        return amount > self.balance

    def withdraw(self, amount, record=True):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.has_money(amount):
            raise ValueError('Недостаточно средств на счете')
        self.balance -= amount
        if record:
            operation = Operation(Operation.WITHDRAW, -amount)
            self.history.append(operation)

    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        return f'Имя: {self.name}; баланс {self.balance:.2f}; Номер паспорта: {self.passport8}; тел.{self.phone_number}'

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.balance:.2f}"

    def show_history(self):
        hist_str = ''
        for operation in self.history:
            hist_str += str(operation) + '\n'
        return hist_str


account1 = Account('Иван', '1234 565678', '+7-999-556-18-54', 100)
account2 = Account('Петр', '2345 746781', '+7-999-985-17-45', 500)
account3 = Account('Василий', '3456 587812', '+7-989-915-77-45', 1000)
account4 = Account('Алексей', '4567 728123', '+7-989-915-77-45', 5000)

try:
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

    print(account1.show_history())
    print(account1.full_info())
    print(account2.show_history())


except ValueError as e:
    print(e)
