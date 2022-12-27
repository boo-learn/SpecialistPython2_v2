import re


class Account:
    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        self.name = name

        if self._validate_passport(passport):
            self.passport = passport
        else:
            raise ValueError("Неверный формат паспорта")

        if self._validate_phone_number(phone_number):
            self.phone_number = phone_number
        else:
            raise ValueError("Неверный формат телефона")

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
        if amount <= self.balance:
            self.__balance -= amount
        else:
            raise ValueError("Недостаточно средств")

    def transfer(self, target_account: 'Account', amount: int) -> None:
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        self.withdraw(amount)
        target_account.deposit(amount)

    def _validate_passport(self, passport):
        pattern = r"\d{4} \d{6}$"  # добавил конец строки, чтобы не проходили паспорта вида 1234 1234567890
        return bool(re.match(pattern, passport))

    def _validate_phone_number(self, phone_number):
        pattern = r"[+]7-9\d{2}-\d{3}-\d{2}-\d{2}$"  # Номер телефона клиента, строка в формате: "+7-9xx-xxx-xx-xx" - из задания
        return bool(re.match(pattern, phone_number))


account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 1000)  # аккаунт с корректными данными
print(account1)

try:
    account2 = Account("Алексей", "3233 456123242344", "+7-901-744-22-99")  # номер паспорта задан неверно
except ValueError as e:
    print(e)

try:
    account3 = Account("Петр", "3232 456124", "+7-804-745-47-22", 400)  # номер телефона задан неверно
except ValueError as e:
    print(e)
