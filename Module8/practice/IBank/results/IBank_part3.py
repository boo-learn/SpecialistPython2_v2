# Сюда отправляем готовое решение IBank часть-3
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
    OPEN = 'Открытие счета '
    DEPOSIT = 'Пополнение '
    WITHDRAW = 'Списание '
    TRANSFER = 'Перевод '
    CLOSE = 'Закрытие счета '
    RESTORE = 'Восстановление счета '
    INCOME = 'Поступление '

    def __init__(self, type, amount, fee=0, target=None, sender=None):
        self.type = type
        self.amount = amount
        self.fee = fee
        self.target = target
        self.sender = sender

    def __str__(self):
        if self.target is not None:
            target_name = ' на счет клиента: ' + self.target.name
        elif self.sender is not None:
            target_name = ' со счета клиента: ' + self.sender.name
        else:
            target_name = ''
        return f'{self.type}{self.amount:+.2f}{target_name}' + (f' (комиссия -{self.fee:.2f})' if self.fee > 0 else '')


class Account(AccountBase):
    FEE = 2

    def __init__(self, name, passport8, phone_number, start_balance=0, in_archive=False):
        AccountBase.__init__(self, name, passport8, phone_number, start_balance)
        self.history = []
        self.in_archive = in_archive
        operation = Operation(Operation.OPEN, self.balance)
        self.history.append(operation)

    def fee_size_calc(self, amount):
        """
        Возвращает размер комиссии в руб. из расчета FEE в пределах положительного баланса
        :param amount: сумма снятия со счета в руб
        :return: сумма комиссии в руб
        """
        return amount * Account.FEE / 100

    def transfer(self, target_account, amount, record=True):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        fee_size = Account.fee_size_calc(self, amount)
        self.withdraw(amount, record=False)
        target_account.deposit(amount)
        if record:
            operation = Operation(Operation.TRANSFER, -amount, target=target_account, fee=fee_size)
            self.history.append(operation)
            operation = Operation(Operation.TRANSFER, amount, sender=self)
            target_account.history.append(operation)

    def deposit(self, amount, record=True):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        if self.in_archive:
            raise ValueError('Операция не может быть выполнена, т.к. целевой счет закрыт')
        self.balance += amount
        if record:
            operation = Operation(Operation.DEPOSIT, amount)
            self.history.append(operation)

    def has_money(self, amount):
        return amount + Account.fee_size_calc(self, amount) > self.balance

    def withdraw(self, amount, record=True):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.in_archive:
            raise ValueError('Операция не может быть выполнена, т.к. счет закрыт')
        fee_size = Account.fee_size_calc(self, amount)
        if self.has_money(amount):
            raise ValueError('Недостаточно средств на счете')
        self.balance -= (amount + Account.fee_size_calc(self, amount))
        if record:
            operation = Operation(Operation.WITHDRAW, amount, fee=fee_size)
            self.history.append(operation)

    def to_archive(self):
        if self.balance < 0:
            raise ValueError('Нельзя закрыть счет с отрицательным балансом')
        amount = self.balance / (1 + Account.FEE / 100)
        fee_size = Account.fee_size_calc(self, amount)
        self.withdraw(amount, record=False)
        self.in_archive = True
        operation = Operation(Operation.CLOSE, -amount, fee=fee_size)
        self.history.append(operation)

    def restore(self):
        self.in_archive = False
        operation = Operation(Operation.RESTORE, self.balance)
        self.history.append(operation)

    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        if self.in_archive:
            status = ' счет закрыт'
        else:
            status = ''
        return f'Имя: {self.name}; баланс {self.balance:.2f}{status}; ' \
               f'Номер паспорта: {self.passport8}; тел.{self.phone_number}'

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


if __name__ == "__main__":
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
        # тестирование закрытия счета
        print('Закрытие счета Василия')
        print(f'{account3 = }')
        account3.to_archive()
        print(f'{account3 = }')
        print(account3.show_history())
        print(account3.full_info())
        account3.restore()
        print(account3.show_history())
        print(account3.full_info())


    except ValueError as e:
        print(e)
