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
    FEE_PERC = 0.02

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

    def enough_money(self, amount, fee_perc=FEE_PERC):
        amount_with_fee = amount + int(amount * fee_perc)
        return amount_with_fee <= self.balance

    def withdraw(self, amount: int, to_history: bool = True, fee_perc=FEE_PERC) -> None:
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        withdraw_fee = int(amount * fee_perc)
        amount_with_fee = amount + withdraw_fee
        if self.enough_money(amount, fee_perc=fee_perc):
            self.__balance -= amount_with_fee
            if to_history:
                operation = Operation(amount=amount, type=Operation.WITHDRAW, fee=withdraw_fee)
                self.__history.append(operation)
        else:
            raise ValueError("Недостаточно средств")

    def transfer(self, target_account: 'Account', amount: int, to_history: bool = True, fee_perc=FEE_PERC) -> None:
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


# Создаем класс для кредитного аккаунта, наследуясь от аккаунта
class CreditAccount(Account):
    FEE_NEGATIVE_PERC = 0.05

    def __init__(self, name, passport, phone_number, start_balance=0, negative_limit=0):
        super().__init__(name, passport, phone_number, start_balance)
        if start_balance < 0 and abs(start_balance) > negative_limit:
            raise ValueError("Стартовый баланс меньше лимита")
        else:
            self.negative_limit = negative_limit

    def enough_money(self, amount, fee_perc=Account.FEE_PERC):
        amount_with_fee = amount + int(amount * fee_perc)
        return amount_with_fee <= self.balance + self.negative_limit

    def withdraw(self, amount: int, to_history: bool = True, fee_perc=Account.FEE_PERC) -> None:
        if self.balance < 0 and fee_perc != 0:
            super().withdraw(amount, to_history=to_history, fee_perc=CreditAccount.FEE_NEGATIVE_PERC)
        else:
            super().withdraw(amount, to_history=to_history, fee_perc=fee_perc)

    def transfer(self, target_account: 'Account', amount: int, to_history: bool = True, fee_perc=Account.FEE_PERC) -> None:
        if self.balance < 0:
            super().transfer(target_account, amount, to_history=to_history, fee_perc=CreditAccount.FEE_NEGATIVE_PERC)
        else:
            super().transfer(target_account, amount, to_history=to_history, fee_perc=fee_perc)

    def __repr__(self):
        return f"<К> {super().__repr__()}"

    def full_info(self) -> str:
        return f"<К> {super().full_info()}"
