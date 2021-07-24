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

    def __init__(self, *args, **kwargs):
        AccountBase.__init__(self, *args, **kwargs)
        self.history = []

    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        self.withdraw(amount, record=False)
        target_account.deposit(amount)
        self.history.append({'event': 'transfer', 'amount': amount, 'fee': 0.02 * amount})

    def deposit(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        self.balance += amount
        self.history.append({'event': 'deposit', 'amount': amount, 'fee': 0})


    def withdraw(self, amount, record=True):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.balance < (amount * 1.02):
            raise ValueError('Недостаточно средств')
        self.balance -= (amount * 1.02)
        if record:
            self.history.append({'event': 'withdraw', 'amount': amount, 'fee': 0.02 * amount})

    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        if input('Введите номер паспорта: ') == self.passport8:
            return f"{self.name}, баланс: {self.balance} руб., паспорт: {self.passport8}, т. {self.phone_number}"
        else:
            return 'Неверные паспортные данные'

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        fio = self.name.split()
        return f"{fio[0]} {fio[1][0]}. {fio[2][0]}. баланс: {self.balance} руб."

    def show_history(self):
        return '\n'.join([f'{x["event"]}: {x["amount"]}, fee: {x["fee"]}' for x in self.history])


class CreditAccount(Account): #черновик

    def __init__(self, negative_limit, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.negative_limit = negative_limit


acc_1 = Account('Иванов Иван Петрович', 'xxxx xxxxxx', '89000000000', start_balance=200)
print(acc_1.balance)
print(acc_1)

acc_2 = Account('Сидоров Евгений Александрович', 'xxxx xxxxxx', '89000000000', start_balance=300)
print(acc_2.balance)
print(acc_2)

acc_1.deposit(400)
print(acc_1)

acc_1.withdraw(50)
print(acc_1)

acc_2.transfer(acc_1, 60)
acc_1.transfer(acc_2, 90)

print(acc_1, acc_2)
print(acc_1.show_history())
