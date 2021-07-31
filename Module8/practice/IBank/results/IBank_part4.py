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


class Operation:
    OPEN = 'Открытие счета '
    DEPOSIT = 'Пополнение '
    WITHDRAW = 'Списание '
    TRANSFER = 'Перевод '
    CLOSE = 'Закрытие счета '
    RESTORE = 'Восстановление счета '
    INCOME = 'Поступление '

    def __init__(self, type, amount, fee=0, target=None, sender=None):
        self.type = type
        self.amount = amount
        self.fee = fee
        self.target = target
        self.sender = sender

    def __str__(self):
        if self.target is not None:
            target_name = ' на счет клиента: ' + self.target.name
        elif self.sender is not None:
            target_name = ' со счета клиента: ' + self.sender.name
        else:
            target_name = ''
        return f'{self.type}{self.amount:+.2f}{target_name}' + (f' (комиссия {self.fee:.2f})' if self.fee > 0 else '')


class Account(AccountBase):
    FEE = 2
    FEE_NEG = 5

    def __init__(self, name, passport8, phone_number, start_balance=0, in_archive=False):
        AccountBase.__init__(self, name, passport8, phone_number, start_balance)
        self.history = []
        self.in_archive = in_archive
        operation = Operation(Operation.OPEN, self.balance)
        self.history.append(operation)

    def fee_size_calc(self, amount):
        """
        Возвращает размер комиссии в руб. из расчета FEE в пределах положительного баланса
        и FEE_NEG в пределах кредитного лимита
        :param amount: сумма снятия со счета в руб
        :return: сумма комиссии в руб
        """
        if self.balance > 0 and self.balance - amount > 0:
            return amount * Account.FEE / 100
        elif self.balance > 0:
            return self.balance * Account.FEE / 100 + (amount - self.balance) * Account.FEE_NEG / 100
        return amount * Account.FEE_NEG / 100

    def transfer(self, target_account, amount, record=True):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        fee_size = Account.fee_size_calc(self, amount)
        self.withdraw(amount, record=False)
        target_account.deposit(amount)
        if record:
            operation = Operation(Operation.TRANSFER, -amount, target=target_account, fee=fee_size)
            self.history.append(operation)
            operation = Operation(Operation.TRANSFER, amount, sender=self)
            target_account.history.append(operation)

    def deposit(self, amount, record=True):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        if self.in_archive:
            raise ValueError('Операция не может быть выполнена, т.к. целевой счет закрыт')
        self.balance += amount
        if record:
            operation = Operation(Operation.DEPOSIT, amount)
            self.history.append(operation)

    def has_money(self, amount):
        return amount + Account.fee_size_calc(self, amount) > self.balance

    def withdraw(self, amount, record=True):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.in_archive:
            raise ValueError('Операция не может быть выполнена, т.к. счет закрыт')
        fee_size = Account.fee_size_calc(self, amount)
        if self.has_money(amount):
            raise ValueError('Недостаточно средств на счете')
        self.balance -= (amount + Account.fee_size_calc(self, amount))
        if record:
            operation = Operation(Operation.WITHDRAW, amount, fee=fee_size)
            self.history.append(operation)

    def to_archive(self):
        if self.balance < 0:
            raise ValueError('Нельзя закрыть счет с отрицательным балансом')
        amount = self.balance / (1 + Account.FEE / 100)
        fee_size = Account.fee_size_calc(self, amount)
        self.withdraw(amount, record=False)
        self.in_archive = True
        operation = Operation(Operation.CLOSE, -amount, fee=fee_size)
        self.history.append(operation)

    def restore(self):
        self.in_archive = False
        operation = Operation(Operation.RESTORE, self.balance)
        self.history.append(operation)

    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        if self.in_archive:
            status = ' счет закрыт'
        else:
            status = ''
        return f'Имя: {self.name}; баланс {self.balance:.2f}{status}; ' \
               f'Номер паспорта: {self.passport8}; тел.{self.phone_number}'

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.balance:.2f}"

    def show_history(self):
        hist_str = ''
        for operation in self.history:
            hist_str += str(operation) + '\n'
        return hist_str


class CreditAccount(Account):
    def __init__(self, name, passport8, phone_number, start_balance=0, negative_limit=0):
        Account.__init__(self, name, passport8, phone_number, start_balance)
        self.negative_limit = negative_limit

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"{self.name} <K> баланс: {self.balance:.2f} лимит: {self.negative_limit}"

    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        if self.in_archive:
            status = ' счет закрыт'
        else:
            status = ''
        return f'Имя: {self.name}; <К> баланс {self.balance:.2f}{status}; кредитный лимит {self.negative_limit}; ' \
               f'Номер паспорта: {self.passport8}; тел.{self.phone_number}'

    def has_money(self, amount):
        return (amount + Account.fee_size_calc(self, amount)) > (self.balance + abs(self.negative_limit))

"""
Нужно поменять тесты с отрицательным балансом, т.к. в моем варианте комиссия
при переходе при исчерпании положительного баланса считается в пределах 
положительного и кредитного лимита отдельно, а за тем суммируется. 

    def test_withdraw_inc_commission_on_negative_balance(self):
        self.account1.withdraw(400)  # уходим в -баланс. Комиссия 2%, т.к. до снятия был положительный баланс
        self.assertEqual(self.account1.balance, -111)
        self.account1.withdraw(200)  # снимает при -балансе. Комиссия 5%
        self.assertEqual(self.account1.balance, -321)
        
    def test_to_archive_negative_balance(self):
        self.account1.withdraw(500)
        self.assertEqual(self.account1.balance, -216)
        with self.assertRaises(ValueError) as error:
            self.account1.to_archive()
        # Можно так, если нужно проверить определенный текст ошибки (как правило так не делают):
        # self.assertTrue('Нельзя убрать счет с отрицательным балансом в архив' in str(error.exception))
"""

if __name__ == "__main__":
    account1 = CreditAccount('Иван', '1234 565678', '+7-999-556-18-54', 300, negative_limit=500)
    account2 = Account('Петр', '2345 746781', '+7-999-985-17-45', 500)
    account3 = Account('Василий', '3456 587812', '+7-989-915-77-45', 1000)
    account4 = Account('Алексей', '4567 728123', '+7-989-915-77-45', 5000)

    try:

        account1.withdraw(400)
        print(account1)
        account1.withdraw(200)
        print(account1)



    except ValueError as e:
        print(e)
