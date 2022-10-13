import re

class Account:
    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        
        self.phone_number = self.validation(phone_number)
        self.passport = self.validation(passport)
        # self.balance = start_balance
        self.__balance = start_balance  # TODO: Закрываем прямой доступ к балансу

    def full_info(self) -> str:

        return f"{self.__repr__()} паспорт: {self.passport} т.{self.phone_number}"

    def __repr__(self) -> str:

        return f"{self.name} {self.balance}"

    @property
    def balance(self) -> int:
        return f"баланс {self.__balance} руб."

    def deposit(self, amount: int) -> None:
        self.__balance += amount

    def withdraw(self, amount: int) -> None:
        if self.__balance < amount:
            raise ValueError("Недостаточно средств")
        self.__balance = self.__balance-amount

    def transfer(self, target_account: 'Account', amount: int) -> None:
        self.withdraw(amount)
        target_account.deposit(amount)
        
    def validation(self, data):
        if re.match(r"[+]7-\d{3}-\d{3}-\d{2}-\d{2}", data):
            return data
        elif re.match(r"\d{4} \d{6}", data):
            return data
        else:
            raise ValueError("Неверный формат телефона/паспорта")
    
account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 1000)  # аккаунт с корректными данными
account2 = Account("Алексей", "+7-901-744-22-99", "323 456124", 200)  # номер паспорта задан не верно
account3 = Account("Петр", "+7-904-745-47", "3232 456124", 200)  # номер телефона задан не верно
