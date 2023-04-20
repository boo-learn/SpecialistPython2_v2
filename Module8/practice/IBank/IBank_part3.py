import re


class Account:

    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        passport_reg = r"\d{4} \d{6}"
        phone_number_reg = r"[+]7-\d{3}-\d{3}-\d{2}-\d{2}"
        if re.match(passport_reg, passport):
            self.passport = passport
        else:
            raise ValueError("Неверный формат паспорта")
        if re.match(phone_number_reg, phone_number):
            self.phone_number = phone_number
        else:
            raise ValueError("Неверный формат телефона")
        self.name = name
        self.__balance = start_balance
        self.__history: list[Operation] = []

    @property
    def balance(self) -> int:
        return self.__balance

    def get_history(self) -> list['Operation']:
        return self.__history

    def full_info(self) -> str:
        return f"{self.name} баланс: {self.__balance} руб. паспорт: {self.passport} т.{self.phone_number}"

    def __repr__(self) -> str:
        return f"{self.name} баланс: {self.__balance} руб."

    def deposit(self, money: int, to_history: bool = True) -> None:
        self.__balance += money
        if to_history:
            operation = Operation(Operation.DEPOSIT, money)
            self.__history.append(operation)

    def withdraw(self, money: int, to_history: bool = True) -> None:
        money += int(money*(Operation.COMMISION/100))
        if not self.__balance >= money:
            raise ValueError("На счете недостаточно средств")
        self.__balance -= money
        if to_history:
            operation = Operation(Operation.WITHDRAW, money)
            self.__history.append(operation)

    def transfer(self, target_acc: 'Account', money: int, to_history: bool = True) -> None:
        self.withdraw(money, to_history=False)
        target_acc.deposit(money, to_history=False)
        if to_history:
            operation_out = Operation(
                Operation.TRANSFER_OUT, money, target_account=target_acc)
            self.__history.append(operation_out)
            operation_in = Operation(
                Operation.TRANSFER_IN, money, target_account=self)
            target_acc.__history.append(operation_in)


class Operation:

    DEPOSIT = 'Пополнение'
    WITHDRAW = 'Снятие'
    TRANSFER_OUT = 'Перевод'
    TRANSFER_IN = 'Поступление'
    COMMISION = 50  # 50%

    def __init__(self, type, amount, target_account=None):
        self.type = type
        self.amount = amount
        self.target_account = target_account
        self.commission_sum = int(amount*(Operation.COMMISION/100))

    def __repr__(self) -> str:
        str_out = f"{self.type} {self.amount} руб."
        if self.type == Operation.TRANSFER_OUT:
            str_out += f" на счет клиента: {self.target_account.name} (комиссия: {self.commission_sum} руб.)"
        if self.type == Operation.TRANSFER_IN:
            str_out += f" со счета клиента: {self.target_account.name}"
        if self.type == Operation.WITHDRAW:
            str_out += f"(комиссия: (комиссия: {self.commission_sum} руб.)"
        return str_out
