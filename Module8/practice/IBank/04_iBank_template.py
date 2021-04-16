# from generators import get_user_data
from abc import ABC, abstractmethod
from datetime import datetime
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
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"

    def __init__(self, type, amount, target=None, fee=0):
        self.date = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        self.type = type
        self.amount = amount
        self.target = target
        self.fee = fee  # fee summa

    def __repr__(self):
        return f"{self.date} " \
               f"Тип операции: {self.type} " \
               f"Сумма: {self.amount} " \
               f"Перевод: {self.target.name if self.target else 'None'} " \
               f"Комиссия: {self.fee if self.fee else '0'}"


class Account(AccountBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.history = []
        self.__fee = 2
        self.in_archive = False
        self.passport8 = self._validate_passport(self.passport8)
        self.phone_number = self._validate_phone_number(self.phone_number)

    def _validate_passport(self, passport_raw):
        try:
            passport = int(passport_raw)
        except ValueError:
            raise ValueError("Номер паспорта должен быть целым числом")
        if not 10000000 <= passport <= 99999999:
            raise ValueError("Паспорт должен быть восьмизначным")
        return passport

    def _validate_phone_number(self, phone_number_raw):
        pattern = re.compile(r"^\+7[0-9]{3}\-[0-9]{3}\-[0-9]{2}\-[0-9]{2}$")
        match = pattern.match(phone_number_raw)
        if not match:
            raise ValueError("Телефонный номер должен соответствовать формату +7xxx-xxx-xx-xx")

        return match.string


    @property
    def fee(self):
        return self.__fee


    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        if self.in_archive:
            raise ValueError("Операция перевода недоступна")

        self.withdraw(amount, is_transfer=True)
        target_account.deposit(amount, is_transfer=True)
        target_account.history.append(
            Operation(Operation.TRANSFER, amount, target=self)
        )
        self.history.append(
            Operation(Operation.TRANSFER, amount, target=target_account, fee=self.fee / 100 * amount)
        )


    def deposit(self, amount, is_transfer=False):
        """
         Внесение суммы на текущий счет
         :param amount: сумма
         """

        if self.in_archive:
            raise ValueError("Операция пополнения недоступна")

        self.balance += amount
        if not is_transfer:
            self.history.append(Operation(Operation.DEPOSIT, amount))


    def _check_balance(self, amount):
        deduce = round(amount * (1 + (self.fee / 100)), 2)
        return self.balance < deduce


    def withdraw(self, amount, is_transfer=False):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """

        if self.in_archive:
            raise ValueError("Операция списания недоступна")

        deduce = round(amount * (1 + (self.fee / 100)), 2)

        if self._check_balance(amount):
            raise ValueError("Недостаточно средств на счете")

        self.balance -= deduce
        if not is_transfer:
            self.history.append(
                Operation(Operation.WITHDRAW, amount, fee=self.fee / 100 * amount)
            )


    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        return f"{self.name} " \
               f"баланс: {self.balance} руб. " \
               f"Паспорт: {self.passport8} " \
               f"т.{self.phone_number}" \
            if not self.in_archive else " Счет находится в архиве"


    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"{self.name} баланс: " \
               f"{self.balance} руб." \
            if not self.in_archive else " Счет находится в архиве"


    def show_history(self):
        return "\n".join(map(str, self.history))


    def to_archive(self):
        self.in_archive = True


    def restore(self):
        self.in_archive = False


class CreditAccount(Account):
    def __init__(self, *args, **kwargs):
        self.negative_limit = kwargs.pop('negative_limit')
        super().__init__(*args, **kwargs)
        self.base_transfer_fee = 2
        self.negative_balance_transfer_fee = 5

    @property
    def fee(self):
        if self.balance < 0:
            return self.negative_balance_transfer_fee
        return self.base_transfer_fee

    def __repr__(self):
        return '<K>' + super().__repr__()

    def full_info(self):
        return '<K>' + super().full_info()

    def _check_balance(self, amount):
        deduce = round(amount * (1 + (self.fee / 100)), 2)
        return self.balance - self.negative_limit < deduce

    def to_archive(self):
        if self.balance < 0:
            raise ValueError('Нельзя убрать счет с отрицательным балансом в архив')
        return super().to_archive()


class Accounts(list):
    def append(self, object):
        iteration = self.__iter__()
        while True:
            try:
                object_in_list = iteration.__next__()
                if object_in_list.passport8 == object.passport8:
                    raise ValueError("Аккаунт с таким номером паспорта уже существует")
                if object_in_list.phone_number == object.phone_number:
                    raise ValueError("Аккаунт с таким номером телефона уже существует")
            except StopIteration:
                break
        return super().append(object)


accounts = Accounts()
account_ivan = Account('Ivan', '12349978', '+7951-879-65-08', 1000)
account_andrey = Account('Andrey', '12346978', '+7951-879-65-58')
accounts.append(account_andrey)
accounts.append(account_ivan)
# account_vasil = CreditAccount('Vasil', 548392, '+77338990000', negative_limit = 1000)
#
# print(account_ivan)
# print(account_andrey)
#
# # account_ivan.deposit(1000)
# # print(account_ivan)
# # print(account_andrey)
#
# try:
#     account_ivan.transfer(account_andrey, 100)
# except ValueError as exp:
#     print(exp)
# print(account_ivan)
# print(account_andrey)
#
# # account_ivan.withdraw(300)
# # account_andrey.withdraw(50)
#
# print(account_ivan)
# print(account_andrey)
#
# try:
#     account_ivan.transfer(account_andrey, 200)
# except ValueError as exp:
#     print(exp)
# print(account_ivan)
# print(account_andrey)
#
# print(account_ivan.show_history())
#
# print("")
# print(account_andrey.show_history())
