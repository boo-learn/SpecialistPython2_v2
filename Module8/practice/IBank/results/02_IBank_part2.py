# from generators import get_user_data
from abc import ABC, abstractmethod
from datetime import datetime

EMPLOYEE_PASSWORD = "123"
ARCHIVE = []
ACCOUNTS = []

class Transaction:
    DEPOSIT = 'deposit'
    WITHDRAW = 'withdraw'
    TRANSFER = 'transfer'
    def __init__(self, category, amount, fee, timestamp=datetime.now().timestamp(), sender=None, receiver=None):
        self.type = category
        self.timestamp = timestamp
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.fee = fee

    def __str__(self):
        fee = ''
        sender = ''
        receiver = ''
        if self.fee:
            fee = f' с комиссией {self.fee}р.'
        if self.sender:
            sender = f'отправитель {self.sender.__repr__()} '
        if self.receiver:
            receiver = f'получатель {self.receiver.__repr__()}'
        return f'Transaction: время-{self.timestamp} {self.type} {sender}{receiver} сумма операции {self.amount}р.{fee}'

    def __repr__(self):
        return f'Transaction: {self.timestamp} {self.type} {self.amount} {self.fee}'


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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.history = []
        self.transfer_fee = 0.02

    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        fee = amount * self.transfer_fee
        self.withdraw(amount + fee)
        target_account.deposit(amount, sender=self)
        self.add_to_history(timestamp=datetime.now().timestamp(),
                            operation=Transaction.TRANSFER,
                            sender=self,
                            receiver=target_account,
                            amount=amount,
                            fee=fee)

    def deposit(self, amount, sender=None):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        if amount < 0:
            raise ValueError('введено отрицательное число')
        self.balance += amount
        self.add_to_history(timestamp=datetime.now().timestamp(),
                            operation=Transaction.DEPOSIT,
                            sender=sender,
                            receiver=self,
                            amount=amount,
                            fee=0.0)
        return self.balance

    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.balance < amount:
            raise ValueError('Недостаточно средств')
        self.balance -= amount
        self.add_to_history(timestamp=datetime.now().timestamp(),
                            operation=Transaction.WITHDRAW,
                            sender=self,
                            amount=amount,
                            fee=0.0)
        return amount

    def add_to_history(self, timestamp: datetime.timestamp, operation: str, amount: int, sender=None, receiver=None, fee=0.0):
        self.history.append(Transaction(category=operation,
                                        amount=amount,
                                        fee=fee,
                                        timestamp=timestamp,
                                        sender=sender,
                                        receiver=receiver))

    def show_history(self):
        return ' | '.join(map(str, self.history))

    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        return f"{self.name} баланс: {self.balance} руб. паспорт: {self.passport8} т.{self.phone_number}"

    def __str__(self):
        return f"{self.name} баланс: {self.balance} руб."

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"{self.name}"

    def close(self):
        ARCHIVE.append(self.__deepcopy__())
        ACCOUNTS.remove(self)

    def __deepcopy__(self, memodict={}):
        new_obj = Account(self.name, self.passport8, self.phone_number, start_balance=self.balance)
        new_obj.history = self.history
        return new_obj


class CreditAccount(Account):
    def __init__(self, limit=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.limit = limit
        self.base_transfer_fee = 0.02
        self.negative_balance_transfer_fee = 0.05

    def calculate_fee(self, amount=0):
        if self.balance - amount <= 0:
            self.transfer_fee = self.negative_balance_transfer_fee
        else:
            self.transfer_fee = self.base_transfer_fee

    def transfer(self, target_account, amount):
        self.calculate_fee(amount)
        super(CreditAccount, self).transfer(target_account, amount)

    def withdraw(self, amount):
        if self.balance + self.limit < amount:
            raise ValueError('Недостаточно средств')
        self.balance -= amount
        self.add_to_history(timestamp=datetime.now().timestamp(),
                            operation=Transaction.WITHDRAW,
                            sender=self,
                            amount=amount,
                            fee=0.0)

    def __str__(self):
        return '<K>' + super().__str__() + f' лимит {self.limit}руб.'

    def __repr__(self):
        return '<K>' + super().__repr__()

    def __deepcopy__(self, memodict={}):
        new_obj = CreditAccount(limit=self.limit, name=self.name, passport8=self.passport8,
                                phone_number=self.phone_number, start_balance=self.balance)
        new_obj.history = self.history
        return new_obj


if __name__ == '__main__':
    ivan = Account('Иван', '12345678', 90000000000, start_balance=1000)
    ACCOUNTS.append(ivan)
    oleg = Account('Олег', '23456789', 90000000001, start_balance=10000)
    ACCOUNTS.append(oleg)
    print(ivan)
    print(oleg)
    print(ACCOUNTS)
    ivan.deposit(100)
    print(ivan)
    try:
        ivan.withdraw(1000000)
    except ValueError as e:
        print(e)
    print(ivan)
    try:
        ivan.transfer(oleg, 1000000)
    except ValueError as e:
        print(e)
    print(ivan)
    print(oleg)
    ivan.transfer(oleg, 500)
    print(ivan)
    print(oleg)
    print('История транзакций:')
    print(f'{ivan} {ivan.show_history()}')
    print(f'{oleg} {oleg.show_history()}')
    print('История транзакций, если добираться через список ACCOUNTS')
    for account in ACCOUNTS:
        print(f'{account} {account.show_history()}')
    print(ACCOUNTS)
    print('Закрываем счёт Ивана')
    ivan.close()
    print('Список открытых счетов')
    print(ACCOUNTS)
    print('Архив')
    print(ARCHIVE)
    print('Создаём кредитный аккаунт Сергей')
    sergo = CreditAccount(limit=1000, name='Сергей', passport8='12345678', phone_number=90000000000, start_balance=10)
    ACCOUNTS.append(sergo)
    print(sergo)
    print(ACCOUNTS)
    try:
        sergo.withdraw(10000)
    except ValueError as e:
        print(e)
    sergo.withdraw(100)
    print(sergo)
    sergo.deposit(1)
    print(sergo)
    try:
        sergo.transfer(oleg, 1000)
    except ValueError as e:
        print(e)
    sergo.transfer(oleg, 200)
    for account in ACCOUNTS:
        print(f'{account} {account.show_history()}')
    print('Проверяем перевод с положительным балансом')
    sergo.deposit(10000)
    sergo.transfer(oleg, 500)
    print(sergo.history[-1])
    print('Проверяем перевод когда баланс при переводе должен стать отрицательным')
    sergo.transfer(oleg, 9700)
    print(sergo)
    print(sergo.history[-1])
    print('Закрываем счет Сергея')
    sergo.close()
    print('Список открытых счетов')
    print(ACCOUNTS)
    print('Архив')
    print(ARCHIVE)

