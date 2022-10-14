from typing import List


class Operation:
    DEPOSIT = 'Пополнение'
    WITHDRAW = 'Снятие'
    TRANSFER_OUT = 'Перевод'
    TRANSFER_IN = 'Поступление'

    def __init__(self, type, amount, target_account=None, commission=0):
        self.type = type
        self.amount = amount
        self.target_account = target_account
        self.commission = commission

    def __repr__(self) -> str:

        if self.type == Operation.DEPOSIT:
            return f'{self.type} {self.amount} руб.'
        if self.type == Operation.WITHDRAW:
            return f'{self.type} {self.amount} руб. (комиссия: {self.commission} руб.)'
        if self.type == Operation.TRANSFER_OUT:
            return f'{self.type} {self.amount} руб. на счет клиента {self.target_account.name} (комиссия: {self.commission} руб.) '
        if self.type == Operation.TRANSFER_IN:
            return f'{self.type} {self.amount} руб. со счёта клиента {self.target_account.name}'


class Account:
    COMMISSION = 2

    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.balance = start_balance
        self.history = []

    def full_info(self) -> str:
        return f'{self.name} баланс: {self.balance} руб. паспорт: {self.passport} т.{self.phone_number}'

    def __repr__(self) -> str:
        return f'{self.name} баланс: {self.balance} руб.'

    @property
    def account_balance(self) -> int:
        return f'{self.balance} руб.'

    def deposit(self, amount: int, to_history: bool = True) -> None:
        self.balance += amount
        if to_history:
            self.history.append(Operation(Operation.DEPOSIT, amount))

    def get_history(self) -> List[str]:
        return [str(operation) for operation in self.history]

    def withdraw(self, amount: int, to_history: bool = True) -> None:
        if self.balance - amount < 0:
            raise ValueError('Недостаточно средств')
        else:
            self.balance -= amount + (amount * Account.COMMISSION / 100)
        if to_history:
            commission = amount * Account.COMMISSION / 100
            self.history.append(Operation(Operation.WITHDRAW, amount, commission=amount * Account.COMMISSION / 100))

    def transfer(self, target_account: 'Account', amount: int, to_history: bool = True) -> None:
        self.withdraw(amount, to_history=False)
        target_account.deposit(amount, to_history=False)
        if to_history:
            self.history.append(Operation(Operation.TRANSFER_OUT, amount, target_account=target_account, commission=amount * Account.COMMISSION / 100))
            target_account.history.append(Operation(Operation.TRANSFER_IN, amount, target_account=self))
