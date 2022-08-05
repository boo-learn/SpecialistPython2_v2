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

    def __init__(self, amount, type, target_account=None, commission=0.0):
        self.amount = amount
        self.type = type
        self.target_account = target_account
        self.commission = commission

    def calculate_commission(self):
        return int(self.amount * self.commission)

    def __repr__(self) -> str:
        """
        :return: возвращает строковое представление операции. Формат указан в 02_IBank_part2.md
        """
        if self.type ==  self.type == Operation.WITHDRAW:
            return f"{self.type} {self.amount} руб. (комиссия: {self.calculate_commission()} руб.)"
        if self.type == Operation.DEPOSIT:
            return f"{self.type} {self.amount} руб."

        if self.type == Operation.TRANSFER_IN:
            return f"{Operation.TRANSFER_IN} {self.amount} руб. со счета клиента: {self.target_account.name}"

        if self.type == Operation.TRANSFER_OUT:
            return f"{Operation.TRANSFER_OUT} {self.amount} руб.(комиссия: {self.calculate_commission()} руб.) на счет клиента: {self.target_account.name}"


class Account:
    COMMISION = 0.02

    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.__balance = start_balance
        self.__history = []

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

    # Данный метод дан в готовом виде. Изучите его и используйте как пример, для доработки других
    def deposit(self, amount: int, to_history: bool = True) -> None:
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        :param to_history: True - записывать операцию в историю, False - не записывать
        """
        self.__balance += amount
        if to_history:
            self.__history.append(Operation(amount, Operation.DEPOSIT))

    @staticmethod
    def amount_with_commission(amount):
        return amount + int(amount * Account.COMMISION)

    def withdraw(self, amount: int, to_history: bool = True) -> None:
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.__balance < self.amount_with_commission(amount):
            raise ValueError("Недостаточно средств на счете. Операция отклонена")

        self.__balance -= self.amount_with_commission(amount)
        if to_history:
            self.__history.append(Operation(amount, Operation.WITHDRAW, commission=Account.COMMISION))

    def transfer(self, target_account: 'Account', amount: int) -> None:
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        self.withdraw(amount, to_history=False)
        target_account.deposit(amount, to_history=False)

        self.__history.append(Operation(amount, Operation.TRANSFER_OUT, target_account))
        target_account.__history.append(Operation(amount, Operation.TRANSFER_IN, self))

    def get_history(self) -> List[str]:
        """
        :return: возвращаем историю операций  виде списка строковых представлений
        """
        return [str(operation) for operation in self.__history]
    

# TODO-1: Создаем класс для кредитного аккаунта, наследуясь от аккаунта
class CreditAccount(Account):
    def __init__(self, name, passport, phone_number, start_balance=0, negative_limit=0):
        # TODO-1: Пока реализуем ТОЛЬКО первый пункт задания "возможность уходить в отрицательный баланс"
        Account.__init__(self,name, passport, phone_number, start_balance)
        self.negative_limit = negative_limit
        #   Договоримся, что negative_limit будет положительным числом.
        #   Например, negative_limit = 500 означает, что мы можем уйти в минус на 500 рублей, self.__balance = -500
        
