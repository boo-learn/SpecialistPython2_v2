# Сюда отправляем готовое решение IBank часть-2
# from generators import get_user_data
from abc import ABC, abstractmethod


class AccountBase(ABC):
    def __init__(self, name, passport8, phone_number, start_balance=0):
        self.name = name
        self.passport8 = passport8
        self.phone_number = phone_number
        self.balance = start_balance

    @abstractmethod
    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        pass

    @abstractmethod
    def deposit(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        pass

    @abstractmethod
    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        pass

    @abstractmethod
    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        return f"..."

    @abstractmethod
    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"..."


class Account(AccountBase):
    def __init__(self, name, passport8, phone_number, start_balance=0):
        super().__init__(name, passport8, phone_number, start_balance)
        self.history = []

    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """

        self.withdraw(amount)
        target_account.deposit(amount)

    def deposit(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        if amount >= 0:
            self.balance += amount
            self.history.append(f"Пополнение счёта на: {amount} руб.")
        else:
            raise ValueError("Сумма не может быть меньше 0")

    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        prcnt = 2
        com = amount - amount * (1 - prcnt / 100)

        if amount > self.balance:
            raise ValueError("Не достаточно денег на счёте")
        self.balance -= amount + com
        self.history.append(f"Списание со счёта: -{amount} руб. Комиссия {prcnt}% = {com} руб.")

    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        return f"{self.name} баланс: {self.balance} руб. " \
               f"паспорт: {self.passport8} тел. {self.phone_number}"

    def history(self):
        if

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.balance} руб."


if __name__ == "__main__":
    obj = Account("Иванов И.П.", 12345678, "8(910)123-45-67", 500)
    obj2 = Account("Сидоров П.И.", 87654321, "8(916)765-43-21", 1000)
    # print(f"Первый аккаунт: {obj}")
    # print(f"Полная информация аккаунт 1: {obj.full_info()}")
    # print(f"Второй аккаунт: {obj2}")
    # print(f"Полная информация аккаунт 2: {obj2.full_info()}")
    # obj.deposit(100)
    # obj.deposit(100)
    # obj.deposit(100)
    # print(obj)
    # try:
    #     obj.withdraw(200)
    # except ValueError as e:
    #     print(e)
    try:
        obj.transfer(obj2, 200)
    except ValueError as e:
        print(e)

    print(obj.history)
    print(f"Первый аккаунт: {obj}")
    print(f"Второй аккаунт: {obj2}")
