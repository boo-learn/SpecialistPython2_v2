from typing import List

# класс для хранение информации об операциях
class Operation:
    # Типы операций храним в свойствах класса
    DEPOSIT = 'Пополнение'
    WITHDRAW = 'Снятие'
    TRANSFER_OUT = 'Перевод'
    TRANSFER_IN = 'Поступление'

    # Напоминаю: обращение к этим переменным происходит через имя класса, пример: Operation.WITHDRAW

    def __init__(self, amount: int, oper_type: str, target_account = None):
        self.type = oper_type
        self.amount = amount
        self.target_account = target_account

    def __repr__(self) -> None:
        """
        :return: возвращает строковое представление операции. Формат указан в 02_IBank_part2.md
        """
        if self.type == Operation.DEPOSIT or self.type == Operation.WITHDRAW:
            return f'{self.type} {self.amount} руб.'
        elif self.type == Operation.TRANSFER_IN:
            return f'{self.type} {self.amount} руб. со счета клиента: {self.target_account.name}'
        else:
            return f'{self.type} {self.amount} руб. на счет клиента: {self.target_account.name}'


class Account:
    # TODO: сюда копируем реализацию класса Account из предыдущей задачи
    # TODO: историю храним как список объектов класса Operation, добавив свойство в конструктор:
    #   self.__history = []

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

    def withdraw(self, amount: int, to_history: bool = True) -> None:
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.__balance < amount:
            raise ValueError("Недостаточно средств на счете. Операция отклонена")
        self.__balance -= amount
        if to_history:
            self.__history.append(Operation(amount, Operation.WITHDRAW))

    def transfer(self, target_account: 'Account', amount: int, to_history: bool = True) -> None:
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        self.withdraw(amount)
        target_account.deposit(amount)
        if to_history:
            self.__history.append(Operation(amount, Operation.TRANSFER_OUT, target_account))
            self.__history.append(Operation(amount, Operation.TRANSFER_IN, target_account))

    def get_history(self) -> List[str]:
        """
        :return: возвращаем историю операций  виде списка строковых представлений
        """
        return [str(operation) for operation in self.__history]
