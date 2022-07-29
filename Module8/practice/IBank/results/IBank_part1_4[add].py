import re


class Account:
    def check_passport(self, passport_num):
        pattern = r"\d{4} \d{6}"

        if re.match(pattern, passport_num):
            print(f"Passport number {passport_num} is correct")
        else:
            print(f"Passport number {passport_num} is not correct")

    def check_phone_number(self, phone_number):
        pattern = r"[+]7-\d{3}-\d{3}-\d{2}-\d{2}"

        if re.match(pattern, phone_number):
            print(f"Phone number {phone_number} is correct")
        else:
            print(f"Phone number {phone_number} is not correct")

    def __init__(self, name, passport, phone_number, start_balance=0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.__balance = start_balance
        self.check_passport(passport)
        self.check_phone_number(phone_number)

    def full_info(self):
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 3200 123456 т.+7-900-200-02-03"
        """
        return f"{self.name} баланс: {self.__balance} руб. паспорт: {self.passport} т. {self.phone_number}"

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иван баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.__balance} руб."

    def deposit(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        self.__balance += amount

    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if amount > self.__balance:
            raise ValueError(f"Сумма списания ({amount}) превышает остаток на счете {self.__balance}")
        self.__balance -= amount

    def transfer(self, target_account, amount):
        self.withdraw(amount)
        target_account.deposit(amount)


account1_1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 1000)  # аккаунт с корректными данными
account2_1 = Account("Алексей", "+7-901-744-22-99", "323 456124", 200)  # номер паспорта задан не верно
account3_1 = Account("Петр", "+7-904-745-47", "3232 456124", 200)  # номер телефона задан не верно

account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 1000)
account2 = Account("Алексей", "+7-901-744-22-99", "3232 456124", 200)

print(account1)
print(account2)

# Переводим деньги с первого аккаунт на второй:
account1.transfer(account2, 500)

# Проверяем изменения баланса:
print(account1)
print(account2)

# Переводим еще с первого аккаунт на второй:
try:
    account1.transfer(account2, 600)
finally:
    # Проверяем изменения баланса:
    print(account1)
    print(account2)
