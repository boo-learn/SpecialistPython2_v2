
from typing import List

class Operation:
    # Типы операций храним в свойствах класса
    DEPOSIT = 'Пополнение'
    WITHDRAW = 'Снятие'
    TRANSFER_OUT = 'Перевод'
    TRANSFER_IN = 'Поступление'


    # Напоминаю: обращение к этим переменным происходит через имя класса, пример: Operation.WITHDRAW

    def __init__(self, amount, type, target_account=None):
        self.type = type
        self.amount = amount
        self.target_account = target_account

    def __repr__(self) -> str:
        """
        :return: возвращает строковое представление операции. Формат указан в 02_IBank_part2.md
        """
        info = ""
        if self.type == Operation.TRANSFER_IN:
            info = f' со счета клиента: {self.target_account.name}'
        elif self.type == Operation.TRANSFER_OUT:
            info = f' на счет клиента: {self.target_account.name}'
        return f'{self.type} {self.amount} руб.{info}'


class Account:
    COMISSION = 0.02
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
        return f"{self.name} баланс: {self.balance} руб. паcпорт: {self.passport} т.{self.phone_number}"

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
            self.__history.append(Operation(amount, Operation.DEPOSIT))

    def withdraw(self, amount: int,  to_history: bool = True) -> None:
        global COMISSION
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.balance < amount + int(amount*COMISSION):
            raise ValueError("Недостаточно средств")

        self.__balance -= (amount+amount*COMISSION)
        if to_history:
            self.__history.append(Operation(amount, Operation.WITHDRAW))

    def transfer(self, target_account: 'Account', amount: int) -> None:
        global COMISSION
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        self.withdraw(amount, to_history=False)
        target_account.deposit(amount, to_history=False)

        oper_out = Operation(amount, Operation.TRANSFER_OUT, target_account=target_account)
        oper_in = Operation(amount, Operation.TRANSFER_IN, target_account=self)
        self.__history.append(oper_out)
        target_account.__history.append(oper_in)

    def get_history(self) -> List[str]:
        """
        :return: возвращаем историю операций в виде списка строковых представлений
        """
        return [str(operation) for operation in self.__history]


account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 1000)
account2 = Account("Алексей", "+7-901-744-22-99", "3232 456124", 200)

account1.transfer(account2, 600)

print("Account1: ")
for op in account1.get_history():
    print(op)

print("Account2: ")
for op in account2.get_history():
    print(op)
