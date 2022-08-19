from typing import List


# Сюда отправляем готовое решение IBank часть-2

# класс для хранение информации об операциях
class Operation:
    # Типы операций храним в свойствах класса
    DEPOSIT = 'Пополнение'
    WITHDRAW = 'Снятие'
    TRANSFER_OUT = 'Перевод'
    TRANSFER_IN = 'Поступление'

    # Напоминаю: обращение к этим переменным происходит через имя класса, пример: Operation.WITHDRAW

    def __init__(self, amount, type, related_account=None):
        self.amount = amount
        self.type = type
        self.related_account = related_account

    def __repr__(self) -> str:
        """
        :return: возвращает строковое представление операции. Формат указан в 02_IBank_part2.md
        """
        if self.type == Operation.DEPOSIT or self.type == Operation.WITHDRAW:
            return f"{self.type} {self.amount} руб."
        elif self.type == Operation.TRANSFER_OUT:
            return f"{self.type} {self.amount} руб. на счет клиента: {self.related_account.name}"
        elif self.type == Operation.TRANSFER_IN:
            return f"{self.type} {self.amount} руб. со счета клиента: {self.related_account.name}"


class Account:

    FEE = 0.02

    def __init__(self, name, passport, phone_number, start_balance = 0, fee=None):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.__balance = start_balance
        self.__history = []
        self.fee = fee

    def full_info(self) -> str:
        return f"{self.name} баланс: {self.balance} руб. паспорт: {self.passport} т.{self.phone_number}"

    def __repr__(self) -> str:
        return f"{self.name} баланс: {self.balance} руб."

    @property
    def balance(self) -> int:
        return self.__balance

    def deposit(self, amount: int, to_history: bool = True) -> None:
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        :param to_history: True - записывать операцию в историю, False - не записывать
        """
        self.__balance += amount
        if to_history:
            self.__history.append(Operation(amount, Operation.DEPOSIT))

    def get_history(self) -> List[str]:
        """
        :return: возвращаем историю операций  виде списка строковых представлений
        """
        return [str(operation) for operation in self.__history]

    def withdraw(self, amount: int, to_history: bool = True) -> None:
        if self.__balance * (1 + Account.FEE) < amount:
            raise ValueError("У Вас не достаточно средств...")

        self.__balance -= (amount + self.balance * Account.FEE)
        if to_history:
            self.__history.append(Operation(amount, Operation.WITHDRAW))

    def transfer(self, target_account: 'Account', amount: int) -> None:
        self.withdraw(amount, to_history=False)
        target_account.deposit(amount, to_history=False)

        transfer_in = Operation(amount, Operation.TRANSFER_IN, self)
        transfer_out = Operation(amount, Operation.TRANSFER_OUT, target_account)

        self.__history.append(transfer_out)
        target_account.__history.append(transfer_in)
