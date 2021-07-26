# from generators import get_user_data
from abc import ABC, abstractmethod


class AccountBase(ABC):
    def __init__(self, name, passport8, phone_number, start_balance=0):
        self.name = name
        self.passport8 = passport8
        self.phone_number = phone_number
        self.balance = start_balance

    @abstractmethod
    def transfer(self, target_account, amount, is_record=True):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        pass

    @abstractmethod
    def deposit(self, amount, is_record=True):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        pass

    @abstractmethod
    def withdraw(self, amount, is_record=True):
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


class Operation:
    DEPOSIT = 'пополнение'
    WITHDRAW = 'списание'
    TRANSFER = 'перевод'

    def __init__(self, type, amount, fee=0., target=None):
        self.type = type
        self.amount = amount
        self.fee = fee
        self.target = target

    def __str__(self):
        if self.target is not None:
            target_name = self.target.name
        else:
            target_name = ''
        if self.fee == 0:
            return f'Операция {self.type} на сумму {self.amount} {target_name}'
        return f'Операция {self.type} на сумму {self.amount} {target_name} с комиссией {self.fee * self.amount:.2f}'


class Account(AccountBase):
    FEE = 0.02

    def __init__(self, name, passport8, phone_number, start_balance=0):
        AccountBase.__init__(self, name, passport8, phone_number, start_balance=0)
        self.history = []
        self.is_archived = False

    def account_close(self):
        self._account_check_status()
        self.is_archived = True

    def account_reopen(self):
        self.is_archived = False

    def _account_check_status(self):
        if self.is_archived:
            raise ValueError(f'Аккаунт {self.name} закрыт и отправлен в архив')

    def transfer(self, target_account, amount, is_record=True):
        """
        Перевод денег на счет другого клиента
        :param is_record:
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        self._account_check_status()
        target_account._account_check_status()
        self.withdraw(amount, is_record=False)
        target_account.deposit(amount, is_record=False)
        if is_record:
            op = Operation(Operation.TRANSFER, amount, target=target_account, fee=self.FEE)
            self.history.append(op)

    def deposit(self, amount, is_record=True):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        self._account_check_status()
        self.balance += amount
        if is_record:
            op = Operation(Operation.DEPOSIT, amount)
            self.history.append(op)

    def _has_money(self, amount):
        return self.balance < amount * (1 + self.FEE)

    def withdraw(self, amount, is_record=True):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        self._account_check_status()
        if self._has_money(amount):
            raise ValueError("На счёту недостаточно средств")
        fee = self.FEE * amount
        self.balance = self.balance - amount - fee
        if is_record:
            op = Operation(Operation.WITHDRAW, amount, fee=self.FEE)
            self.history.append(op)

    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        self._account_check_status()
        return f"{self.name} баланс: {self.balance} руб. паспорт: {self.passport8} т. {self.phone_number}"

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        self._account_check_status()
        return f"{self.name} баланс: {self.balance} руб."

    def show_history(self):
        self._account_check_status()
        h_str = ''
        for op in self.history:
            h_str += str(op) + '\n'
        return h_str[:-1]


class CreditAccount(Account):
    FEE = 0
    NEGATIVE_BALANCE_FEE = 0.05

    def __init__(self, name, passport8, phone_number, start_balance=0, negative_limit=-1000):
        Account.__init__(self, name, passport8, phone_number, start_balance)
        self.__negative_limit = negative_limit

    def __repr__(self):
        self._account_check_status()
        return f"{self.name} K-account баланс: {self.balance} руб."

    def full_info(self):
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        self._account_check_status()
        return f"{self.name} K-account баланс: {self.balance} руб. лимит {self.__negative_limit} руб. паспорт: {self.passport8} т. {self.phone_number}"

    def _has_money(self, amount):
        self.FEE = self.NEGATIVE_BALANCE_FEE
        if self.balance > 0:
            self.FEE = Account.FEE
        return (self.balance + abs(self.__negative_limit)) < amount * (1 + self.FEE)


account1 = Account("Иван", 1234, "...")
account2 = Account("Пётр", 5678, "...", start_balance=300)
account1.deposit(100)
account1.transfer(account2, 90)
account2.withdraw(80)
print(account1.show_history())
print(account2.show_history())
print(account1.full_info())
print(account2.full_info())

account3 = CreditAccount("Сергей", 4444, "...")
account3.deposit(500)
print(account3.full_info())
account3.withdraw(900)
account3.transfer(account1, 200)
print(account3.show_history())
print(account1.full_info())
account3.account_close()
account1.transfer(account3, 100)
