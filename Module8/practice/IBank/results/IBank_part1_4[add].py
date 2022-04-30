import re


def validate_passport(passport):
    pattern = r"\d{4} \d{6}"
    return re.match(pattern, passport)


def validate_phone_number(phone_number):
    pattern = r"[+]7-\d{3}-\d{3}-\d{2}-\d{2}"
    return re.match(pattern, phone_number)


class Account:

    def __init__(self, name, passport, phone_number, start_balance=0):
        self.name = name
        if validate_passport(passport):
            self.passport = passport
        else:
            raise ValueError('Некорректный номер паспорта')
        if validate_phone_number(phone_number):
            self.phone_number = phone_number
        else:
            raise ValueError('Некорректный номер телефона')
        self.__balance = start_balance

    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        self.withdraw(amount)
        target_account.deposit(amount)

    @property
    def balance(self):
        return self.__balance

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
        if self.__balance - amount < 0:
            raise ValueError('Недостаточно средств на счету')
        self.__balance -= amount

    def full_info(self):
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 3200 123456 т.+7-900-200-02-03"
        """
        return f'{self.name} баланс: {self.__balance} руб. паспорт: {self.passport} т.{self.phone_number}'

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иван баланс: 100 руб."
        """
        return f'{self.name} баланс: {self.__balance} руб.'


account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 1000)  # аккаунт с корректными данными
account2 = Account("Алексей", "323 456124", "+7-901-744-22-99", 200)  # номер паспорта задан не верно
account3 = Account("Петр", "3232 456124", "+7-904-745-47", 200)  # номер телефона задан не верно
