from typing import List
import re
# Сюда отправляем готовое решение IBank часть-2

# класс для хранение информации об операциях
class Operation:
    # Типы операций храним в свойствах класса
    DEPOSIT = 'Пополнение'
    WITHDRAW = 'Снятие'
    TRANSFER_OUT = 'Перевод'
    TRANSFER_IN = 'Поступление'

    # Напоминаю: обращение к этим переменным происходит через имя класса, пример: Operation.WITHDRAW

    def __init__(self, amount, operation, related_acc=None):
        # TODO: Тут добавляем свойства для хранение информации об операции
        self.amount = amount
        self.operation = operation
        self.related_acc = related_acc

    def __repr__(self) -> str:
        """
        :return: возвращает строковое представление операции. Формат указан в 02_IBank_part2.md
        """
        if self.operation == Operation.DEPOSIT or self.operation == Operation.WITHDRAW:
            return f"{self.operation} {self.amount} руб."
        elif self.operation == Operation.TRANSFER_OUT:
            return f"{self.operation} {self.amount} руб. на счет клиента: {self.related_acc.name}"
        elif self.operation == Operation.TRANSFER_IN:
            return f"{self.operation} {self.amount} руб. со счета клиента: {self.related_acc.name}"


class Account:
    pattern_phone = r"[+]7-\d{3}-\d{3}-\d{2}-\d{2}"
    pattern_pasport = r"\d{4} \d{6}"

    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.__balance = start_balance
        self.__history = []
        self.__validator_phone()

    def __validator_phone(self):
        if not re.match(Account.pattern_phone, self.phone_number):
            raise ValueError(f"Phone number {self.phone_number} is not correct")
        if not re.match(Account.pattern_pasport, self.passport):
            raise ValueError(f"Passport number {self.passport} is not correct")

    def full_info(self) -> str:
        return f"{self.name} баланс: {self.balance} руб. паспорт: {self.passport} т.{self.phone_number}"

    def __repr__(self) -> str:
        return f"{self.name} баланс: {self.balance} руб."

    @property
    def balance(self) -> int:
        return self.__balance

    def deposit(self, amount: int) -> None:
        self.__balance += amount

    def withdraw(self, amount: int, to_history: bool = True) -> None:
        if self.__balance < amount:
            raise ValueError("У Вас не достаточно средств...")

        self.__balance -= amount
        if to_history:
            self.__history.append(Operation(amount, Operation.DEPOSIT))

    def transfer(self, target_account: 'Account', amount: int) -> None:
        self.withdraw(amount, to_history=False)
        target_account.deposit(amount, to_history=False)

        transfer_in = Operation(amount, Operation.TRANSFER_IN, self)
        transfer_out = Operation(amount, Operation.TRANSFER_OUT, target_account)

        self.__history.append(transfer_out)
        target_account.__history.append(transfer_in)

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

    def get_history(self) -> List[str]:
        """
        :return: возвращаем историю операций  виде списка строковых представлений
        """
        return [str(operation) for operation in self.__history]

if __name__ == '__main__':
    account1 = Account("Иван", "3002 123477", "+7-900-600-10-22", start_balance=1500)
    account2 = Account("Петр", "3002 123456", "+7-900-600-10-20", start_balance=300)

    # account1.deposit(600)
    # account1.withdraw(600)
    # account1.withdraw(400)
    account1.transfer(account2, 100)

    for hist in account1.get_history():
        print(hist)

    for hist in account2.get_history():
        print(hist)
