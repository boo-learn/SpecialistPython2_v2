import re

class Account:

    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        passport_reg = r"\d{4} \d{6}"
        phone_number_reg = r"[+]7-\d{3}-\d{3}-\d{2}-\d{2}"
        if re.match(passport_reg, passport):
            self.passport = passport
        else:
            raise ValueError("Неверный формат телефона/паспорта")
        if re.match(phone_number_reg, phone_number):
            self.phone_number = phone_number
        else:
            raise ValueError("Неверный формат телефона/паспорта")
        self.name = name
        self.__balance = start_balance

    @property
    def balance(self) -> int:
        return self.__balance

    def full_info(self) -> str:
        return f"{self.name} баланс: {self.__balance} руб. паспорт: {self.passport} т.{self.phone_number}"

    def __repr__(self) -> str:
        return f"{self.name} баланс: {self.__balance} руб."

    def deposit(self, money: int) -> None:
        self.__balance += money

    def withdraw(self, money: int) -> int:
        if self.__balance >= money:
            self.__balance -= money
            return money
        else:
            raise ValueError

    def transfer(self, target_account: 'Account', money: int) -> None:
        to_transaction = self.withdraw(money)
        target_account.__balance += to_transaction
