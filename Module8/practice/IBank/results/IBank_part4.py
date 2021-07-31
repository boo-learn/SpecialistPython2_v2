# from generators import get_user_data
from abc import ABC, abstractmethod

class Operation:

    DEPOSIT = 'Пополнение'
    WITHDRAW = 'Снятие'
    TRANSFER = 'Перевод'
    INCOME = 'Поступление'

    def __init__(self, event, amount, fee=0, target=None, sender=None):
        self.type = event 
        self.amount = amount
        self.fee = fee 
        self.target = target
        self.sender = sender

    def __repr__(self) -> str:
        if  self.type == Operation.TRANSFER:
            return f'{self.type}: -{self.amount} руб. на счет клиента: {self.target.name}, комиссия:{self.fee}'
        elif self.type == Operation.INCOME:
            return f'{self.type}: +{self.amount} со счета клиента: {self.sender.name}'
        elif self.type == Operation.WITHDRAW:
            return f'{self.type}: -{self.amount} руб., комиссия: {self.fee}'
        elif self.type == Operation.DEPOSIT:
            return f'{self.type}: +{self.amount}'


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

    FEE = 0.02

    def __init__(self, name, passport8, phone_number, start_balance=0):
        AccountBase.__init__(self, name, passport8, phone_number, start_balance)
        self.history = []
        self._fee = Account.FEE
        self.in_archive = False

    def transfer(self, target_account, amount) -> None:
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return: None
        """
        self.withdraw(amount, record=False)
        target_account.deposit(amount, record=False)
        operation = Operation(Operation.TRANSFER, amount, fee=self._fee * amount, target=target_account)
        self.history.append(operation)
        operation_other = Operation(Operation.INCOME, amount, sender=self)
        target_account.history.append(operation_other)

    def deposit(self, amount, record=True) -> None:
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        :return: None
        """
        self.balance += amount
        if record:
            operation = Operation(Operation.DEPOSIT,
                                    amount)
            self.history.append(operation)

    def _has_money(self, amount) -> bool:
        """"
        Есть ли средства на счету
        :return: True если есть средства
        """
        return self.balance >= amount * (1 + self._fee)

    def withdraw(self, amount, record=True) -> None:
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        :return: None
        """
        if not self._has_money(amount):
            raise ValueError('Недостаточно средств')
        self.balance -= (amount * (1 + self._fee))
        if record:
            operation = Operation(Operation.WITHDRAW,
                                    amount,
                                    fee=self._fee * amount)
            self.history.append(operation)

    def full_info(self) -> str:
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203"
        :return: данные клиента
        """
        return f"{self.name}, баланс: {self.balance} руб., паспорт: {self.passport8}, т. {self.phone_number}"

    def __repr__(self) -> str:
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"{self.name}, баланс: {self.balance} руб."

    def show_history(self):
        message = '\n'.join((str(op) for op in self.history))
        return message

    def to_archive(self):
        self.balance = 0
        self.in_archive = True

    def restore(self):
        self.in_archive = False



class CreditAccount(Account):

    NEGATIVE_FEE = 0.05
    POSITIVE_FEE = 0.02

    def __init__(self, name, passport8, phone_number, start_balance=0, negative_limit=-1000):
        Account.__init__(self, name, passport8, phone_number, start_balance)
        self.__negative_limit = negative_limit

    def _check_fee(self) -> None:
        """
        Проверяет размер комиссии
        :return: None
        """
        self._fee = self.NEGATIVE_FEE if self.balance < 0 else self.POSITIVE_FEE

    def _has_money(self, amount) -> bool:
        """
        Есть ли средства на счету
        :return: True если есть средства
        """
        self._check_fee()
        return (self.balance + abs(self.__negative_limit)) >= amount * (1 + self._fee)

    def __repr__(self) -> str:
        """"
        :return: данные клиента
        """
        return f'K-account: {self.name}. баланс: {self.balance} руб.'

    def to_archive(self):
        if self.balance < 0:
            raise ValueError('Невозможно отпавить в архив при отрицательном балансе')
        self.balance = 0
        self.in_archive = True

    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203"
        :return: данные клиента
        """
        return f"<К>-account: {self.name}, баланс: {self.balance} руб., паспорт: {self.passport8}, т. {self.phone_number}"
