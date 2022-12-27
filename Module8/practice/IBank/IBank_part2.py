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

    def __init__(self, type, amount, target_account=None):
        # TODO: Тут добавляем свойства для хранение информации об операции
        self.type = type
        self.amount = amount
        self.target_account = target_account

    def __repr__(self) -> str:
        """
        :return: возвращает строковое представление операции. Формат указан в 02_IBank_part2.md
        """
        str_out = f"{self.type} {str(self.amount)} rub."
        if self.type == Operation.TRANSFER_OUT:
            str_out += f" to client {self.target_account}"
        if self.type == Operation.TRANSFER_IN:
            str_out += f" from client {self.target_account}"
        return str_out


class Account:
    # TODO-0: скопируйте реализацию из предыдущего решения
    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        # self.balance = start_balance
        self.__balance = start_balance  # TODO: Закрываем прямой доступ к балансу
        self.__history = []

    def full_info(self) -> str:
        return f"{self.name}. Balance: {self.balance}. Passport: {self.passport}. tel: {self.phone_number}"

    def __repr__(self) -> str:
        return f"{self.name}. Balance: {self.__balance}."

    @property
    def balance(self) -> int:
        return self.__balance

    def deposit(self, amount: int, to_history: bool = True) -> None:
        self.__balance += amount
        if to_history:
            self.__history.append(Operation(Operation.DEPOSIT, amount))

    def withdraw(self, amount: int, to_history: bool = True) -> None:
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            raise ValueError
        if to_history:
            self.__history.append(Operation(Operation.WITHDRAW, amount))

    def transfer(self, target_account: 'Account', amount: int, to_history: bool = True) -> None:
        self.withdraw(amount, False)
        target_account.deposit(amount, False)
        if to_history:
            self.__history.append(Operation(Operation.TRANSFER_OUT, amount, target_account.name))
            target_account.__history.append(Operation(Operation.TRANSFER_IN, amount, self.name))

    def get_history(self) -> List[str]:
        """
        :return: возвращаем историю операций  виде списка строковых представлений
        """
        return [str(operation) for operation in self.__history]

