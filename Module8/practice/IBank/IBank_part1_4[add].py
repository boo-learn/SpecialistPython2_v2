import re

class Account:
    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        self.name = name
        if self.validate_passport(passport):
            self.passport = passport
        else:
            raise ValueError("Неверный формат паспорта")
        if self.validate_phone(phone_number):
            self.phone_number = phone_number
        else:
            raise ValueError("Неверный формат телефона")

        self.__balance = start_balance  # TODO: Закрываем прямой доступ к балансу

    def full_info(self) -> str:
        return f"{self.name} баланс: {self.balance} руб. паспорт: {self.passport} т.{self.phone_number}"

    def __repr__(self) -> str:
        return f"{self.name} баланс: {self.balance} руб."

    @property
    def balance(self) -> int:
        return self.__balance

    def deposit(self, amount: int) -> None:
        self.__balance += amount

    def withdraw(self, amount: int) -> None:
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("no money!")

    def transfer(self, target_account: 'Account', amount: int) -> None:
        if amount <= self.__balance:
            self.__balance -= amount
            target_account.deposit(amount)
        else:
            raise ValueError("no money!")

    def validate_passport(self, passport: str):
        pattern = r"\d{4} \d{6}"
        if re.match(pattern, passport):
            return True
        else:
            return False

    def validate_phone(self, phone_number: str):
        pattern = r"[+]7-\d{3}-\d{3}-\d{2}-\d{2}"
        if re.match(pattern, phone_number):
            return True
        else:
            return False

try:
    account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 1000)  # аккаунт с корректными данными
except ValueError as e:
    print(e)

try:
    account2 = Account("Алексей", "323 456124", "+7-901-744-22-99")  # номер паспорта задан неверно
except ValueError as e:
    print(e)

try:
    account3 = Account("Петр", "3232 456124", "+7-904-745-47", 400)  # номер телефона задан неверно
except ValueError as e:
    print(e)
