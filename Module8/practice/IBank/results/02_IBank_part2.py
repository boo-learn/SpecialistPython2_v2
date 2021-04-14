# from generators import get_user_data
from abc import ABC, abstractmethod
from datetime import datetime


class AccountBase(ABC):
    def __init__(self, name, passport8, phone_number, start_balance=0, is_archive=False):
        self.name = name
        self.passport8 = passport8
        self.phone_number = phone_number
        self.balance = start_balance
        self.__is_archive = is_archive

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
    TRANSFER = "transfer"
    WITHDRAW = "withdraw"
    DEPOSIT = "deposit"

    def __init__(self, type, amount, target=None, fee=0):
        self.date = datetime.now()
        self.type = type
        self.amount = amount
        self.target = target
        self.fee = fee  # fee summ

    def __repr__(self):
        target = self.target.name if self.target else ""
        return f"({self.date}) {self.type}: sum: {self.amount} {target}"


class Account(AccountBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.history = []
        self.fee = 2  # 2%

    def transfer(self, target_account, amount):
        self.withdraw(amount, is_transfer=True)
        target_account.deposit(amount, is_transfer=True)
        op_transfer_to = Operation(Operation.TRANSFER, amount, target_account, amount * (self.fee / 100))
        op_transfer_from = Operation(Operation.TRANSFER, amount, self, amount * (self.fee / 100))
        self.history.append(op_transfer_to)
        target_account.history.append(op_transfer_from)

    def withdraw(self, amount, is_transfer=False):
        if amount * (1 + (self.fee / 100)) > self.balance:
            raise ValueError('Недостаточно средств на счете.')
        self.balance -= amount * (1 + (self.fee / 100))
        if not is_transfer:
            self.history.append(
                Operation(Operation.WITHDRAW, amount, fee=amount * (self.fee / 100))
            )

    def deposit(self, amount, is_transfer=False):
        self.balance += amount
        if not is_transfer:
            op_deposit = Operation(Operation.DEPOSIT, amount)
            self.history.append(op_deposit)

    def full_info(self):
        return f"{self.name} баланс: {self.balance}. Паспорт: {self.passport8}. тел.: {self.phone_number}"

    def __repr__(self):
        return f"{self.name} баланс: {self.balance}."

    def get_history(self):
        return "\n".join(map(str, self.history))

    def to_archive(self):
        self.__is_archive = True

    def restore(self):
        self.__is_archive = False

class CreditAccount(Account):
    def __init__(self, *args, negative_limit, **kwargs):
        super().__init__(*args, **kwargs)
        self.negative_limit = negative_limit


    def withdraw(self, amount, is_transfer=False):
        if self.balance < 0:
            self.fee = 5
        else: 
            self.fee = 2
        if amount * (1 + (self.fee / 100)) > self.balance + self.negative_limit:
            raise ValueError('Недостаточно средств на счете.')
        self.balance -= amount * (1 + (self.fee / 100))
        if not is_transfer:
            self.history.append(
                Operation(Operation.WITHDRAW, amount, fee=amount * (self.fee / 100))
            )

    def __repr__(self):
        return '<K> ' + super().__repr__()



ca = CreditAccount("Ivan", 12345678, "+79008001122", negative_limit=1000)

#
# account_ivan = Account("Ivan", 12345678, "+79008001122")
# account_petr = Account("Petr", 12345677, "+79008001133")
#
# account_ivan.deposit(500)
#
# try:
#     account_ivan.transfer(account_petr, 400)
# except ValueError as e:
#     print(e)
#
# print(account_ivan.get_history())
# print()
# print(account_petr.get_history())
#
# print(account_ivan)
# print(account_petr)
