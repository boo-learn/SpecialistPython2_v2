from typing import List


class Operation:
    # Типы операций храним в свойствах класса
    DEPOSIT = 'Пополнение'
    WITHDRAW = 'Снятие'
    TRANSFER_OUT = 'Перевод'
    TRANSFER_IN = 'Поступление'

    # Напоминаю: обращение к этим переменным происходит через имя класса, пример: Operation.WITHDRAW

    def __init__(self, type, amount, target_account=None, fee=None):
        self.type = type
        self.amount = amount
        self.target_account = target_account
        self.fee = fee

    def __repr__(self) -> str:
        """
        :return: возвращает строковое представление операции. Формат указан в 02_IBank_part2.md
        """
        str_out = f"{self.type} {self.amount} руб."
        if self.type == Operation.TRANSFER_OUT:
            str_out += f" на счет клиента: {self.target_account.name}"
        if self.type == Operation.TRANSFER_IN:
            str_out += f" со счета клиента: {self.target_account.name}"
        if self.fee is not None:
            str_out += f" (комиссия: {self.fee} руб.)"
        return str_out


class Account:
    TRANSFER_FEE_PERC = 0.02
    WITHDRAW_FEE_PERC = 0.02

    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.__balance = start_balance
        # историю храним как список объектов класса Operation, добавив свойство в конструктор:
        self.__history: List[Operation] = []

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

    def deposit(self, amount: int, to_history: bool = True) -> None:
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        self.__balance += amount
        if to_history:
            operation = Operation(amount=amount, type=Operation.DEPOSIT)
            self.__history.append(operation)

    def withdraw(self, amount: int, to_history: bool = True, fee_perc=WITHDRAW_FEE_PERC) -> None:
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        withdraw_fee = int(amount * fee_perc)
        amount_with_fee = amount + withdraw_fee
        if amount_with_fee <= self.balance:
            self.__balance -= amount_with_fee
            if to_history:
                operation = Operation(amount=amount, type=Operation.WITHDRAW, fee=withdraw_fee)
                self.__history.append(operation)
        else:
            raise ValueError("Недостаточно средств")

    def transfer(self, target_account: 'Account', amount: int, to_history: bool = True, fee_perc=TRANSFER_FEE_PERC) -> None:
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        transer_fee = int(amount * fee_perc)
        amount_with_fee = amount + transer_fee
        self.withdraw(amount_with_fee, to_history=False, fee_perc=0)
        target_account.deposit(amount, to_history=False)
        if to_history:
            operation_out = Operation(amount=amount, type=Operation.TRANSFER_OUT, target_account=target_account, fee=transer_fee)
            operation_in = Operation(amount=amount, type=Operation.TRANSFER_IN, target_account=self)
            self.__history.append(operation_out)
            target_account.__history.append(operation_in)

    def get_history(self) -> List[Operation]:

        """
        :return: возвращаем историю операций в виде списка операций
        """
        return self.__history
