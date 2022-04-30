# Сюда отправляем готовое решение IBank часть-4
import re


def validate_passport(passport):
    pattern = r"\d{4} \d{6}"
    return re.match(pattern, passport)


def validate_phone_number(phone_number):
    pattern = r"[+]7-\d{3}-\d{3}-\d{2}-\d{2}"
    return re.match(pattern, phone_number)


class Operation:
    DEPOSIT = "Пополнение"
    WITHDRAW = "Снятие"
    TRANSFER = "Перевод"
    RECEIPT = "Поступление"

    def __init__(self, operation, amount, commision=0.0, account=None):
        self.operation = operation
        self.amount = amount
        self.account = account
        self.commision = round(self.amount * commision * 0.01)

    def __repr__(self):
        add_str = ''
        if self.operation == self.WITHDRAW:
            add_str = f' (комиссия: {self.commision} руб.)'
        if self.operation == self.TRANSFER:
            add_str = f' (комиссия: {self.commision} руб.) на счет клиента: {self.account.name}'
        if self.operation == self.RECEIPT:
            add_str = f' со счета клиента: {self.account.name}'
        return f'{self.operation} {self.amount} руб.' + add_str


class Account:

    commision = 2

    def __init__(self, name, passport, phone_number, start_balance=0):
        self.name = name
        if validate_passport(passport):
            self.passport = passport
        else:
            raise ValueError('Некорректный номер паспорта')
        if validate_phone_number(phone_number):
            self.phone_number = phone_number
        else:
            raise ValueError('Некорректный номер телефона')
        self.__balance = start_balance
        self.__history = []

    def transfer(self, target_account, amount):
        self.withdraw(amount, False)
        target_account.deposit(amount, False)
        self.__history.append(Operation(Operation.TRANSFER, amount, CreditAccount.commision, account=target_account))
        target_account.__history.append(Operation(Operation.RECEIPT, amount, account=self))

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount, record_to_history=True):
        self.__balance += amount
        if record_to_history:
            self.__history.append(Operation(Operation.DEPOSIT, amount))

    def withdraw(self, amount, record_to_history=True):
        if self.__balance - amount * (1 + Account.commision / 100) < 0:
            raise ValueError('Недостаточно средств на счету')
        self.__balance -= amount * (1 + Account.commision / 100)
        if record_to_history:
            self.__history.append(Operation(Operation.WITHDRAW, amount, Account.commision))

    def full_info(self):
        return f'{self.name} баланс: {self.__balance} руб. паспорт: {self.passport} т.{self.phone_number}'

    def __repr__(self):
        return f'{self.name} баланс: {self.__balance} руб.'

    def show_history(self):
        for operation in self.__history:
            print(operation)


class CreditAccount(Account):

    commision = Account.commision

    def __init__(self, name, passport, phone_number, start_balance=0, negative_limit=0):
        Account.__init__(self, name, passport, phone_number)
        self.__balance = start_balance
        self.__history = []
        self.negative_limit = negative_limit*-1

    def withdraw(self, amount, record_to_history=True):
        if self.__balance < 0:
            CreditAccount.commision = 5
        else:
            CreditAccount.commision = Account.commision
        if self.__balance - amount * (1 + CreditAccount.commision / 100) < self.negative_limit:
            raise ValueError('Недостаточно средств на счету')
        self.__balance -= amount * (1 + CreditAccount.commision / 100)
        if record_to_history:
            self.__history.append(Operation(Operation.WITHDRAW, amount, commision=CreditAccount.commision))

    def full_info(self):
        return f'<K> {self.name} баланс: {self.__balance} руб. паспорт: {self.passport} т.{self.phone_number}'

    def __repr__(self):
        return f'<K> {self.name} баланс: {self.__balance} руб.'


account1 = CreditAccount("Иван", "3230 634563", "+7-900-765-12-34", 1000, negative_limit=20000)
account2 = Account("Алексей", "3232 456124", "+7-901-744-22-99", 200)
account1.transfer(account2, 1500)
print(account1)
account1.transfer(account2, 1500)
print(account1)
account1.show_history()
account2.show_history()
