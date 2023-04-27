import re

class Account:
    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.__balance = start_balance
        self.__passport_check()
        self.__phone_check()

    def full_info(self) -> str:
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 3200 123456 т.+7-900-200-02-03"
        """
        return f"{self.name} баланс: {self.balance} руб. паспорт: {self.passport} т.{self.phone_number} "

    def __repr__(self) -> str:
        """
        :return: Информацию о счете в виде строки в формате "Иван баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.balance} руб."
        # TODO: реализуйте getter для просмотра баланса
        #  Подробнее тут: https://pythobyte.com/using-getters-and-setters-in-python-5205-840ed13f/

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
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("Not enough money in your amount")

    def transfer(self, target_account: 'Account', amount: int) -> None:
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        if amount <= self.__balance:
            self.__balance -= amount
            target_account.deposit(amount)
        else:
            raise ValueError("Not enough money in your amount")

    def __passport_check(self):
        pattern = r"\d{4} \d{6}"
        if not re.match(pattern, self.passport):
            raise ValueError(f"Неверный формат паспорта {self.passport}")

    def __phone_check(self):
        pattern = r"[+]7-\d{3}-\d{3}-\d{2}-\d{2}"
        if not re.match(pattern, self.phone_number):
            raise ValueError(f"Неверный формат телефона {self.phone_number}")


account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 1000)  # аккаунт с корректными данными
print(account1)
#account2 = Account("Алексей", "323 456124", "+7-901-744-22-99")  # номер паспорта задан неверно
#account3 = Account("Петр", "3232 456124", "+7-904-745-47", 400)  # номер телефона задан неверно
