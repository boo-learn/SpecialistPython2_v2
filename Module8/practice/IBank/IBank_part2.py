from typing import List
import re


class Operation:
    DEPOSIT = 'Пополнение'
    WITHDRAW = 'Снятие'
    TRANSFER_OUT = 'Перевод'
    TRANSFER_IN = 'Поступление'

    def __init__(self, type, amount, target_account=None):
        self.type = type
        self.amount = amount
        self.target_account = target_account

    def __repr__(self) -> str:
        str_out = f"{self.type} {self.amount} руб."
        if self.type == Operation.TRANSFER_OUT:
            str_out += f" на счет клиента: {self.target_account.name}"
        if self.type == Operation.TRANSFER_IN:
            str_out += f" со счета клиента: {self.target_account.name}"
        return str_out


class Account:
    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        self.name = name
        self.passport = None
        self.phone_number = None
        self.__check_passport(passport)
        self.__check_phone(phone_number)
        self.__balance = start_balance
        self.info = self.full_info()
        self.__history: List[Operation] = []

    def __check_passport(self, passport):
        passport_pattern = r"\d{4} \d{6}"
        if re.match(passport_pattern, passport):
            self.passport = passport
        else:
            raise ValueError('Неверный формат паспортных данных')

    def __check_phone(self, phone):
        phone_pattern = r"[+]7-\d{3}-\d{3}-\d{2}-\d{2}"
        if re.match(phone_pattern, phone):
            self.phone_number = phone
        else:
            raise ValueError('Неверный формат номера телефона')

    def full_info(self) -> str:
        return f"{self.name} баланс: {self.__balance} руб. паспорт: {self.passport} т.{self.phone_number}"

    def __repr__(self) -> str:
        return self.info

    def get_history(self) -> List[Operation]:
        return self.__history

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount: int, to_history: bool = True):
        self.__balance += amount
        if to_history:
            self.__history.append(Operation('Пополнение', amount))

    def withdraw(self, amount: int, to_history: bool = True):
        if self.__balance - amount >= 0:
            self.__balance -= amount
            if to_history:
                self.__history.append(Operation('Снятие', amount))
        else:
            raise ValueError('Недостаточно средств')

    def transfer(self, target_account: 'Account', amount: int) -> None:
        try:
            self.withdraw(amount, to_history=False)
            target_account.deposit(amount, to_history=False)
            self.__history.append(Operation('Перевод', amount, target_account))
            target_account.__history.append(Operation('Поступление', amount, self))
        except ValueError:
            raise ValueError('Недостаточно средств')
