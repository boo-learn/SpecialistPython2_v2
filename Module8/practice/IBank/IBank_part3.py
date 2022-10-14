from typing import List


class Operation:
    # Типы операций храним в свойствах класса
    DEPOSIT = 'Пополнение'
    WITHDRAW = 'Снятие'
    TRANSFER_OUT = 'Перевод'
    TRANSFER_IN = 'Поступление'

    def __init__(self, amount, type, target_account=None, commission=0):
        self.type = type
        self.amount = amount
        self.target_account = target_account
        self.commission = commission

    def __repr__(self) -> str:
        """
        :return: возвращает строковое представление операции. Формат указан в 02_IBank_part2.md
        """
        info = ""
        if self.type == Operation.TRANSFER_IN:
            info = f' со счета клиента: {self.target_account.name}'
        elif self.type == Operation.TRANSFER_OUT:
            info = f' на счет клиента: {self.target_account.name} (комиссия: {self.commission} руб.)'
        elif self.type == Operation.WITHDRAW:
            info = f' (комиссия: {self.commission} руб.)'
        return f'{self.type} {self.amount} руб.{info}'


class Account:
    COMMISSION = 2

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
        :param to_history: True - записывать операцию в историю, False - не записывать
        """
        commission = get_commission(amount)
        total_amount = amount + commission
        if total_amount <= self.__balance:
            self.__balance -= total_amount
            if to_history:
                self.__history.append(Operation(amount, Operation.WITHDRAW, commission=commission))
        else:
            raise ValueError("Not enough money")

    def transfer(self, target_account: 'Account', amount: int) -> None:
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        commission = get_commission(amount)
        self.withdraw(amount, False)
        op_out = Operation(amount, Operation.TRANSFER_OUT, target_account=target_account, commission=commission)
        self.__history.append(op_out)

        target_account.deposit(amount, False)
        op_in = Operation(amount, Operation.TRANSFER_IN, self)
        target_account.__history.append(op_in)

    def get_history(self) -> List[str]:
        """
        :return: возвращаем историю операций  виде списка строковых представлений
        """
        return [str(operation) for operation in self.__history]


def get_commission(amount):
    return (amount * Account.COMMISSION / 100) // 1


account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 1000)
account2 = Account("Алексей", "+7-901-744-22-99", "3232 456124", 200)

account1.transfer(account2, 600)
account2.withdraw(100)
account2.deposit(100)

print("Account1: ")
for op in account1.get_history():
    print(op)

print("Account2: ")
for op in account2.get_history():
    print(op)
