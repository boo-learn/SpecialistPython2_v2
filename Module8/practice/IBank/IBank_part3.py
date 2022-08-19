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

    def __init__(self, amount, name, client = None, current_comission = 0):
        # TODO: Тут добавляем свойства для хранение информации об операции
        self.name = name
        self.amount = amount
        self.client = client
        self.comission = current_comission

    def __repr__(self) -> str:
        """
        :return: возвращает строковое представление операции. Формат указан в 02_IBank_part2.md

        Пополнение 600 руб.
        Снятие 400 руб.
        Пополнение 1000 руб.
        Перевод 750 руб. на счет клиента: Петр
        Поступление 300 руб. со счета клиента: Александр
        """

        if self.name == self.TRANSFER_IN:
            return f'{self.name} {self.amount} руб. со счета клиента: {self.client}'
        elif self.name == self.TRANSFER_OUT:
            return f'{self.name} {self.amount} руб. на счет клиента: {self.client} (Комиссия: {self.comission})'
        else:
            return f'{self.name} {self.amount} руб. (Комиссия: {self.comission})'

class Account:

    COMMISSION = 2

    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        # self.balance = start_balance
        self.__balance = start_balance
        self.__history = []

        try:
            self.check_passport()
        except ValueError:
            print(f'Некорректный формат паспорта, {name}')

        try:
            self.check_phone()
        except ValueError:
            print(f'Некорректный формат телефона, {name}')

    def check_passport(self):
        import re

        pattern = r"\d{4} \d{6}"

        if not re.match(pattern, self.passport):
            raise ValueError("Неверный формат телефона/паспорта")

    def check_phone(self):
        import re

        pattern = r"[+]7-\d{3}-\d{3}-\d{2}-\d{2}"

        if not re.match(pattern, self.phone_number):
            raise ValueError("Неверный формат телефона/паспорта")

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

    def get_history(self) -> List[str]:
        """
        :return: возвращаем историю операций  виде списка строковых представлений
        """
        return [str(operation) for operation in self.__history]

    def withdraw(self, amount: int, to_history: bool = True) -> None:
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """

        current_comission = int((amount*self.COMMISSION/100))
        amount += current_comission

        if self.__balance < amount:
            raise ValueError("У Вас не достаточно средств...")

        self.__balance -= amount
        if to_history:
            self.__history.append(Operation(amount, Operation.WITHDRAW, current_comission))

    def transfer(self, target_account: 'Account', amount: int, to_history: bool = True) -> None:
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """

        self.withdraw(amount, False)

        target_account.deposit(amount, False)

        if to_history:
            target_account.__history.append(Operation(amount, Operation.TRANSFER_IN, self.name))
            self.__history.append(Operation(amount, Operation.TRANSFER_OUT, target_account.name))

if __name__ == '__main__':
    # Создаем тестовый аккаунт:
    account1 = Account("Алексей", "3232 456124", "+7-901-744-22-99", start_balance=2000)
    account2 = Account("Вася", "3232 456124", "+7-901-744-22-99", start_balance=2000)
    # print(account1.balance)
    # Смотрим баланс:
    # print(account1)
    # print(account1)
    # print(account2)
    # Вносим сумму на счет:
    account1.deposit(600)
    # print(account1)
    # print(account1.get_history())
    # print(account2.get_history())
    # print(account1)
    # print(account2)
    # # Снимаем деньги со счета:
    try:
        account1.withdraw(1000.14)
    except ValueError as e:
        print(e)
    # print(account1)
    # print(account2)
    account1.withdraw(1000)
    account1.transfer(account2, 500)
    for item in account1.get_history():
        print(f'{account1.name},{item}')
    for item in account2.get_history():
        print(f'{account2.name},{item}')

    print(account1)
    print(account2)
    #
