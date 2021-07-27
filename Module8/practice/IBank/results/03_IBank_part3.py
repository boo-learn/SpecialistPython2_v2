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
    DEPOSIT = 'deposit'
    WITHDRAW = 'withdraw'
    TRANSFER = 'transfer'

    def __init__(self, type, amount, interest=0, target=None):
        self.type = type
        self.amount = amount
        self.interest = interest
        self.target = target

    def __str__(self):
        if self.target is not None:
            target_name = self.target
        else:
            target_name = ''
        return f'Operation: {self.type}, amount: {self.amount}, target: {target_name}, interest: {self.amount*(self.interest/100)}'


class Account(AccountBase):
    INTEREST = 2

    def __init__(self, name, passport8, phone_number, start_balance=0):
        AccountBase.__init__(self, name, passport8, phone_number, start_balance)
        self.history = []
        self.active = True
        if len(str(self.passport8)) != 8:
            raise ValueError("Incorrect length of the passport number")
          #"+7xxx-xxx-xx-xx"
        area1 = self.phone_number[2:5]
        area2 = self.phone_number[6:9]
        area3 = self.phone_number[10:12]
        area4 = self.phone_number[-2:]
        if self.phone_number != f'+7{area1}-{area2}-{area3}-{area4}':
            raise ValueError("Please insert your phone number in format: +7xxx-xxx-xx-xx")

    def transfer(self, target_account, amount, record=True):
        if self.active:
            self.withdraw(amount, record=False)
            target_account.deposit(amount, record=False)
            if record:
                op = Operation(Operation.TRANSFER, amount, target=target_account, interest=Account.INTEREST)
                self.history.append(op)

    def deposit(self, amount, record=True):
        if self.active:
            self.balance += amount
            if record:
                op = Operation(Operation.DEPOSIT, amount)
                self.history.append(op)

    def __enough_money(self, amount):
        return self.balance < amount * (1 + Account.INTEREST/100)

    def withdraw(self, amount, record=True):
        if self.active:
            if self.__enough_money(amount):
                raise ValueError("Isn't enough money")

            self.balance -= amount * (1 + Account.INTEREST/100)
            if record:
                op = Operation(Operation.WITHDRAW, amount, interest=Account.INTEREST)
                self.history.append(op)

    def full_info(self):
        return f"{self.name} баланс: {self.balance} руб. паспорт: {self.passport8} т.{self.phone_number}"

    def __repr__(self):
        return f"{self.name} баланс: {self.balance} руб."

    def show_history(self):
        hist_str = ''
        for operation in self.history:
            hist_str += str(operation) + '\n'
        return hist_str

    def closing(self):
        self.active = False


class CreditAcc(Account):
    def __init__(self, name, passport8, phone_number, start_balance=0, negative_limit=-1000):
        Account.__init__(self, name, passport8, phone_number, start_balance)
        self.__negative_limit = negative_limit
        self.history = []

    def __repr__(self):
        return f"{self.name} K-account баланс: {self.balance} руб."

    def __enough_money(self, amount):
        if self.balance < 0:
            Account.INTEREST = 5
        return (self.balance + abs(self.__negative_limit)) < amount * (1 + Account.INTEREST / 100)

    def withdraw(self, amount, record=True):
        if self.__enough_money(amount):
            raise ValueError("Isn't enough money")

        self.balance -= amount * (1 + Account.INTEREST / 100)
        if record:
            op = Operation(Operation.WITHDRAW, amount, interest=Account.INTEREST)
            self.history.append(op)

    def transfer(self, target_account, amount, record=True):
        self.withdraw(amount, record=False)
        target_account.deposit(amount, record=False)
        if record:
            op = Operation(Operation.TRANSFER, amount, interest=Account.INTEREST)
            self.history.append(op)


try:
    account1 = Account('Ivan', 24655387, '+7987-321-87-43')
except ValueError as e:
    print(e)
# try:
#     account2 = Account('Olga', 23424385, '59300')
# except ValueError as e:
#     print(e)
try:
    account2 = Account('Olga', 234385, '+7977-321-34-65')
except ValueError as e:
    print(e)

account1.deposit(612)
account1.withdraw(100)

# #account1.transfer(account2, 250)
#
# print(account1.show_history())
#
# account1.closing()
# account1.deposit(1000)
# print(account1)
