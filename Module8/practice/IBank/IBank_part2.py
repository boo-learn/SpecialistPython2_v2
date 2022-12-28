from typing import List
import re

# класс для хранения информации об операциях
class Operation:
    # Типы операций храним в свойствах класса
    DEPOSIT = 'Пополнение'
    WITHDRAW = 'Снятие'
    TRANSFER_OUT = 'Перевод'
    TRANSFER_IN = 'Поступление'

    # Напоминаю: обращение к этим переменным происходит через имя класса, пример: Operation.WITHDRAW

    def __init__(self, type, amount, target_account=None):
        self.type = type
        self.amount = amount
        self.target_account = target_account

    def __repr__(self) -> str:
        """
        :return: возвращает строковое представление операции. Формат указан в 02_IBank_part2.md
        """
        str_out = f"{self.type} {self.amount} руб."
        if self.type == Operation.TRANSFER_OUT:
            str_out += f" на счет клиента: {self.target_account.name}"
        if self.type == Operation.TRANSFER_IN:
            str_out += f" со счета клиента: {self.target_account.name}"
        return str_out


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
        self.__balance = start_balance
        # историю храним как список объектов класса Operation, добавив свойство в конструктор:
        self.__history: List[Operation] = []

    def full_info(self) -> str:
        return f"{self.name} баланс: {self.balance} руб. паспорт: {self.passport} т.{self.phone_number}"

    def __repr__(self) -> str:
        return f"{self.name} баланс: {self.balance} руб."

    @property
    def balance(self) -> int:
        return self.__balance

    # Данный метод дан в готовом виде. Изучите его и используйте как пример, для доработки других
    def deposit(self, amount: int, to_history: bool = True, source : 'Account' = None) -> None:
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        :param to_history: True - записывать операцию в историю, False - не записывать
        """
        if source is None:
            operation = Operation.DEPOSIT
        else:
            operation = Operation.TRANSFER_IN
        self.__balance += amount
        if to_history:
            self.__history.append(Operation(operation, amount, source))

    def withdraw(self, amount: int, to_history: bool = True, source : 'Account' = None) -> None:
        if source is None:
            operation = Operation.WITHDRAW
        else:
            operation = Operation.TRANSFER_OUT
        if amount <= self.__balance:
            self.__balance -= amount
        if to_history:
            self.__history.append(Operation(operation, amount, source))
        else:
            raise ValueError("no money!")

    def transfer(self, target_account: 'Account', amount: int, to_history: bool = True) -> None:
        self.withdraw(amount = amount, to_history = True, source = target_account )
        target_account.deposit(amount = amount, to_history = True, source = target_account)

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

    def get_history(self) -> List[Operation]:
        """
        :return: возвращаем историю операций в виде списка операций
        """
        return self.__history


# Создаем тестовый аккаунт:
account1 = Account("Алексей", "3232 456124", "+7-901-744-22-99", start_balance=500)
account2 = Account("Andy", "3232 456124", "+7-901-744-22-99", start_balance=500)

# Выполняем пару операций пополнения:
account1.deposit(200)
account1.deposit(500)
account1.transfer(account2, 100)

# Выводим историю операций:
for operation in account1.get_history():
    print(operation)

for operation in account2.get_history():
    print(operation)
