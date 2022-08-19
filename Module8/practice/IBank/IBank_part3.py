from typing import List
import math

# Сюда отправляем готовое решение IBank часть-2

# класс для хранение информации об операциях


class Operation:
    # Типы операций храним в свойствах класса
    DEPOSIT = 'Пополнение'
    WITHDRAW = 'Снятие'
    TRANSFER_OUT = 'Перевод'
    TRANSFER_IN = 'Поступление'
    comission = 0.02

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
            return f"{self.type} {self.amount} руб. (комиссия: {self.amount*Operation.comission } руб.)"
        elif self.type == Operation.TRANSFER_OUT:
            return f"{self.type} {self.amount} руб. на счет клиента: {self.related_account.name} (комиссия: {self.amount*Operation.comission } руб.)"
        elif self.type == Operation.TRANSFER_IN:
            return f"{self.type} {self.amount} руб. со счета клиента: {self.related_account.name}"


class Account:
    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.__balance = start_balance
        self.__history = []
        

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

        if self.__balance + self.__balance * self.comission < amount:
            raise ValueError("У Вас не достаточно средств...")

        self.__balance -= (math.floor(amount + amount * self.comission))
        if to_history:
            self.__history.append(Operation(amount, Operation.WITHDRAW))

    def transfer(self, target_account: 'Account', amount: int) -> None:
        self.withdraw(amount, to_history=False)
        target_account.deposit(amount, to_history=False)

        transfer_in = Operation(amount, Operation.TRANSFER_IN, self)
        transfer_out = Operation(amount, Operation.TRANSFER_OUT, target_account)

        self.__history.append(transfer_out)
        target_account.__history.append(transfer_in)


if __name__ == "__main__":
    account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 1000)
    account2 = Account("Алексей", "+7-901-744-22-99", "3232 456124", 200)

    # account1.deposit(600)
    # account1.withdraw(600)
    # account1.withdraw(400)
    try:
        account1.transfer(account2, 500)
    except ValueError as e:
        print(e)

    print("History-1: ")
    for hist in account1.get_history():
        print(hist)

    print("History-2: ")
    for hist in account2.get_history():
        print(hist)


account1.deposit(600)
print(account1)

        # Снимаем деньги со счета:

print('снятие денег со счета')
try:
    account1.withdraw(1000)
except ValueError as e:
    print(e)
print(account1)

        # Пробуем снять еще:
try:
    account1.withdraw(1000)
except ValueError as e:
    print(e)

print('еще попытка снятия денег со счета')
print(account1)


print("History-1: ")
for hist in account1.get_history():
    print(hist)
