from typing import List
import re


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

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance - amount >= 0:
            self.__balance -= amount
        else:
            raise ValueError('Недостаточно средств')

    def transfer(self, target_account: 'Account', amount: int) -> None:
        self.withdraw(amount)
        target_account.deposit(amount)
