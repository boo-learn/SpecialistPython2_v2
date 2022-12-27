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

    def __init__(self, type, amount, target_account= None):
        self.type = type
        self.amount = amount
        self.target_account = target_account


    def __repr__(self) -> None:
        if self.type == Operation.DEPOSIT:
            return f"{self.type} {self.amount} руб."
        if self.type == Operation.TRANSFER_IN:
            return f"{Operation.TRANSFER_IN} {self.amount} руб. со счета клиента: {self.target_account.name}"

class Account:

    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.__balance = start_balance  # TODO: Закрываем прямой доступ к балансу
        self.__history = []

    def full_info(self) -> str:
        return f"{self.name} баланс: {self.__balance} руб. паспорт: {self.passport} т.{self.phone_number}"

    def __repr__(self) -> str:
        return f"{self.name} баланс: {self.__balance} руб."

    def balance(self) -> int:
        return self.__balance

    def get_history(self) -> List[str]:
        return [str(operation) for operation in self.__history]

    def withdraw(self, amount: int, to_history: bool = True) -> None:
        if self.__balance < amount:
            raise ValueError("Недостаточно средств на счете")
        self.__balance -= amount
        if to_history:
            self.__history.append(Operation(amount, Operation.WITHDRAW))

    def transfer(self, target_account: 'Account', amount: int, to_history: bool = True) -> None:
        self.withdraw(amount)
        target_account.deposit(amount)
        if to_history:
            self.__history.append(Operation(amount, Operation.TRANSFER_OUT))

    def deposit(self, amount: int, to_history: bool = True) -> None:
        self.__balance += amount
        if to_history:
            self.__history.append(Operation(amount, Operation.DEPOSIT))

    def get_history(self) -> List[str]:
        return [str(operation) for operation in self.__history]

account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 1000)
account2 = Account("Алексей", "+7-901-744-22-99", "3232 456124", 200)

print(account1)
print(account2)

account2.deposit(200)

print (account2.get_history())
