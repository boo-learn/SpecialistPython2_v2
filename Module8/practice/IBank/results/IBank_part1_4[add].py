import re

class Account:
    pattern_pass = r"\d{4} \d{6}"
    pattern_ph = r"[+]7-\d{3}-\d{3}-\d{2}-\d{2}"

    def __init__(self, name, passport, phone_number, start_balance=0):
        self.name = name

        if re.match(Account.pattern_pass, passport):
            self.passport = passport
        else:
            print(f"Passport number {passport} is not correct")
            raise ValueError(f"Passport number {passport} is not correct")

        if re.match(Account.pattern_ph, phone_number):
            self.phone_number = phone_number
        else:
            print(f"Phone number {phone_number} is not correct")
            raise ValueError(f"Phone number {phone_number} is not correct")
        self.balance = start_balance

    def full_info(self):
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 3200 123456 т.+7-900-200-02-03"
        """
        return f"{self.name} balance: {self.balance} rub. passport:{self.passport } ph.:{self.phone_number}"

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иван баланс: 100 руб."
        """
        return f"{self.name} balance: {self.balance} rub"

    def deposit(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Недостаточно средств")

    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        if self.balance >= amount:
            self.balance -= amount
            target_account.balance += amount
        else:
            raise ValueError("Недостаточно средств")

account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 1000)  # аккаунт с корректными данными
#account2 = Account("Алексей", "+7-901-744-22-99", "323 456124", 200)  # номер паспорта задан не верно
account3 = Account("Петр", "3230 634563", "3232 456124", 200)  # номер телефона задан не верно
