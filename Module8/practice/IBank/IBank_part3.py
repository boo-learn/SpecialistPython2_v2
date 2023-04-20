import re
from typing import List


class Operation:
    # Типы операций храним в свойствах класса
    DEPOSIT = 'Пополнение'
    WITHDRAW = 'Снятие'
    TRANSFER_OUT = 'Перевод'
    TRANSFER_IN = 'Поступление'

    # Напоминаю: обращение к этим переменным происходит через имя класса, пример: Operation.WITHDRAW

    def __init__(self, type, amount, target_account=None):
        self.type = type
        self.amount = amount
        self.target_account = target_account

    def __repr__(self) -> str:
        """
        :return: возвращает строковое представление операции. Формат указан в 02_IBank_part2.md
        """
        str_out = f"{self.type} {self.amount} руб."
        if self.type == Operation.TRANSFER_OUT:
            str_out += f" на счет клиента: {self.target_account.name}"
        if self.type == Operation.TRANSFER_IN:
            str_out += f" со счета клиента: {self.target_account.name}"
        return str_out

class Account:
    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        def is_correct_passport_number(passport):
            pattern = r"\d{4} \d{6}"
            if re.match(pattern, passport):
                print(f"Passport number {passport} is correct")
            else:
                print(f"Passport number {passport} is not correct")
            
        def is_correct_phone_number(phone_number):
            pattern = r"[+]7-\d{3}-\d{3}-\d{2}-\d{2}"
            if re.match(pattern, phone_number):
                print(f"Phone number {phone_number} is correct")
            else:
                print(f"Phone number {phone_number} is not correct")
            
        self.name = name
        
        self.passport = passport
        is_correct_passport_number(self.passport)
        
        self.phone_number = phone_number
        is_correct_phone_number(self.phone_number)
        
        self.__balance = start_balance
        self.__history: List[Operation] = []
                     

    def full_info(self) -> str:
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 3200 123456 т.+7-900-200-02-03"
        """
        return f"{self.name} баланс: {self.__balance} руб. паспорт: {self.passport} т. {self.phone_number}"

    def __repr__(self) -> str:
        """
        :return: Информацию о счете в виде строки в формате "Иван баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.__balance} руб."

    @property
    def balance(self) -> int:
        return self.__balance

    def deposit(self, amount: int) -> None:
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        self.__balance += amount

    def withdraw(self, amount: int) -> None:
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.__balance - amount >= 0:
            self.__balance -= amount
        else:
            raise Exception("Недостаточно средств на счёте!")
            
    def transfer(self, target_account: 'Account', amount: int) -> None:
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        self.withdraw(amount)
        target_account.deposit(amount)
        

    # Данный метод дан в готовом виде. Изучите его и используйте как пример, для доработки других
    def deposit(self, amount: int, to_history: bool = True) -> None:
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        :param to_history: True - записывать операцию в историю, False - не записывать
        """
        self.__balance += amount
        if to_history:
            operation = Operation(amount, Operation.DEPOSIT)
            self.__history.append(operation)

    def get_history(self) -> List[Operation]:
        """
        :return: возвращаем историю операций в виде списка операций
        """
        self.__history.append()
        return self.__history



account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 1000)  # аккаунт с корректными данными
account2 = Account("Алексей", "323 456124", "+7-901-744-22-99")  # номер паспорта задан неверно
account3 = Account("Петр", "3232 456124", "+7-904-745-47", 400)  # номер телефона задан неверно
