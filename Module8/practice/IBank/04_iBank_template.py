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
    def deposite(self, amount):
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
        AccountBase.__init__(self, name, passport8, phone_number, start_balance)
    
    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        self.balance -= amount
        target_account.balance += amount

    def deposite(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        self.balance -= amount

    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        return f"{self.name}, баланс: {self.balance} руб., паспорт: {self.passport8}, т. {self.phone_number}"

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        fio = self.name.split()
        return f"{fio[0]} {fio[1][0]}. {fio[2][0]}. баланс: {self.balance} руб."


acc_1 = Account('Иванов Иван Петрович', 'xxxx xxxxxx', '89000000000', start_balance=200)
print(acc_1.balance)
print(acc_1)

acc_2 = Account('Сидоров Евгений Александрович', 'xxxx xxxxxx', '89000000000', start_balance=300)
print(acc_2.balance)
print(acc_2)

acc_1.deposite(400)
print(acc_1)

acc_1.withdraw(50)
print(acc_1)

acc_2.transfer(acc_1, 60)

print(acc_1, acc_2)
print(acc_1.full_info())
