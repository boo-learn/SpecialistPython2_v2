import re


def validate_passport(passport):

    pattern = r"\d{4} \d{6}"

    try:
        if not re.match(pattern, passport):
            raise ValueError(f"Неверный формат паспорта '{passport}'")
    except ValueError as e:
        print(e)


def validate_phone_number(phone_number):

    pattern = r"[+]7-\d{3}-\d{3}-\d{2}-\d{2}"

    try:
        if not re.match(pattern, phone_number):
            raise ValueError(f"Неверный формат телефона '{phone_number}'")
    except ValueError as e:
        print(e)


class Account:
    def __init__(self, name: str, phone_number: str, passport: str, start_balance: int = 0):
        self.name = name
        self.passport = validate_passport(passport)
        self.phone_number = validate_phone_number(phone_number)
        self.__balance = start_balance

    def full_info(self) -> str:
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 3200 123456 т.+7-900-200-02-03"
        """
        return f"{self.name} баланс: {self.balance} руб. паспорт: {self.passport} т.{self.phone_number}"

    def __repr__(self) -> str:
        """
        :return: Информацию о счете в виде строки в формате "Иван баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.balance} руб."

    @property
    def balance(self) -> int:
        return self.__balance

    def deposit(self, amount: int) -> None:
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        self.__balance += amount

    def withdraw(self, amount: int) -> None:
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.__balance - amount < 0:
            raise ValueError("Недостаточно средств на счете. Операция отклонена")

        self.__balance -= amount

    def transfer(self, target_account: 'Account', amount: int) -> None:
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        self.withdraw(amount)
        target_account.deposit(amount)


account1 = Account("Иван", "+7-900-765-12-34", "3230 634563", 1000)  # аккаунт с корректными данными
account2 = Account("Алексей", "+7-901-744-22-99", "323 456124", 200)  # номер паспорта задан не верно
account3 = Account("Петр", "+7-904-745-47", "3232 456124", 200)  # номер телефона задан не верно
