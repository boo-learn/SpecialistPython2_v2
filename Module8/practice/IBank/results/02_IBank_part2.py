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
        self.activeaccount = 1
        self.COMMISSION = 0.02
        self.history = ['Создан счет с начальным балансом ' + str(start_balance)]


    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        fee = round(amount * (1 + self.COMMISSION), 2)
        self.withdraw(amount + fee)
        target_account.deposit(amount)
        self.history.append('Осуществлен перевод на счет ' + str(target_account) + 'в сумме ' + str(amount))
        self.history.append('Списана комисия в сумме ' + str(fee))


    def deposit(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        if amount <= 0:
            raise ValueError('Сумма должна быть положительной')
        self.balance += amount
        self.history.append('Пополнен счет на сумму ' + str(amount))


    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if amount > self.balance:
            raise ValueError('Запрашиваемая сумма не может быть больше баланса')
        self.balance -= amount
        self.history.append('Снятие со счета суммы ' + str(amount))

    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        return f"{self.name} баланс: {self.balance} руб. паспорт:{self.passport8} тел. {self.phone_number}"

    def print_history(self):
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        return f'История операций по счету {self.passport8}:\n {" ".join(self.history)}'

    def close_account():
        """
        Закрыть счет клиента.
        Считаем, что оставшиеся на счету деньги были выданы клиенту наличными, при закрытии счета
        """
        self.withdraw(self.balance)
        self.ativeaccount = 0
        self.history.append('Закрытие счета. Выдача остатка в сумме ' + str(self.balance))

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.balance} руб."


if __name__ == "__main__":
    account1 = Account("Иванов Иван Петрович", 12345678, "+79161234567", 0)
    account2 = Account("Петров Сергей Иванович", 22345678, "+79261234567", 0)

    print(account1)
    account1.deposit(500)
    print(account1)

    try:
        account1.withdraw(300)
    except ValueError as e:
        print(e)
    print(account1)

    try:
        account1.withdraw(300)
    except ValueError as e:
        print(e)
    print(account1)

    print(account1.print_history())


