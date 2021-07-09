# from generators import get_user_data
from abc import ABC, abstractmethod


class AccountBase(ABC):
    def __init__(self, name, passport8, phone_number, start_balance=0):
        self._name = name
        self._passport8 = passport8
        self._phone_number = phone_number
        self._balance = start_balance

    # An example of a virtual getter/setter.
    @property
    @abstractmethod
    def name(self):
        pass


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
    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        """

        balance_left = self._balance - amount
        if balance_left >= 0:
            self._balance -= amount
            target_account.deposit(amount)
        else:
            raise ValueError("Недостаточно средств для перевода.")

    @property
    def name(self):
        return self._name

    def deposit(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Сумма пополнения должна быть положительной.")

    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета, если средств достаточно.
        :param amount: сумма
        """
        balance_left = self._balance - amount
        if balance_left >= 0:
            self._balance -= amount
        else:
            raise ValueError("Недостаточно средств для снятия.")

    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        return f"{self._name} баланс: {self._balance} руб. паспорт: {self._passport8} т. {self._phone_number}"

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"{self._name} баланс: {self._balance} руб."


def main():
    ac1 = Account("L. Torvalds", 11111111, 9998887766, 998)
    ac2 = Account("R. Stallman", 22222222, 9998887755, 1)
    print(ac1)
    print(ac1.full_info())
    print(ac2)
    print(ac2.full_info())
    ac2.deposit(1)
    ac2.transfer(ac1, 2)
    print(ac1)
    print(ac2)



if __name__ == "__main__":
    main()

