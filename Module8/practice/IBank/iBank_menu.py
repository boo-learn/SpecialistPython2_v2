# from generators import get_user_data
import pickle
from abc import ABC, abstractmethod
from datetime import datetime


EMPLOYEE_PASSWORD = "123"
ARCHIVE = []
ACCOUNTS = []


class Transaction:
    DEPOSIT = 'deposit'
    WITHDRAW = 'withdraw'
    TRANSFER = 'transfer'
    def __init__(self, category, amount, fee, timestamp=datetime.now().timestamp(), sender=None, receiver=None):
        self.type = category
        self.timestamp = timestamp
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.fee = fee

    def __str__(self):
        fee = ''
        sender = ''
        receiver = ''
        if self.fee:
            fee = f' с комиссией {self.fee}р.'
        if self.sender:
            sender = f'отправитель {self.sender.__repr__()} '
        if self.receiver:
            receiver = f'получатель {self.receiver.__repr__()}'
        return f'Transaction: время-{self.timestamp} {self.type} {sender}{receiver} сумма операции {self.amount}р.{fee}'

    def __repr__(self):
        return f'Transaction: {self.timestamp} {self.type} {self.amount} {self.fee}'


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
        super().__init__(*args, **kwargs)
        self.history = []
        self.transfer_fee = 0.02

    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        fee = amount * self.transfer_fee
        self.withdraw(amount + fee)
        target_account.deposit(amount, sender=self)
        self.add_to_history(timestamp=datetime.now().timestamp(),
                            operation=Transaction.TRANSFER,
                            sender=self,
                            receiver=target_account,
                            amount=amount,
                            fee=fee)

    def deposit(self, amount, sender=None):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        if amount < 0:
            raise ValueError('введено отрицательное число')
        self.balance += amount
        self.add_to_history(timestamp=datetime.now().timestamp(),
                            operation=Transaction.DEPOSIT,
                            sender=sender,
                            receiver=self,
                            amount=amount,
                            fee=0.0)
        return self.balance

    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.balance < amount:
            raise ValueError('Недостаточно средств')
        self.balance -= amount
        self.add_to_history(timestamp=datetime.now().timestamp(),
                            operation=Transaction.WITHDRAW,
                            sender=self,
                            amount=amount,
                            fee=0.0)
        return amount

    def add_to_history(self, timestamp: datetime.timestamp, operation: str, amount: int, sender=None, receiver=None, fee=0.0):
        self.history.append(Transaction(category=operation,
                                        amount=amount,
                                        fee=fee,
                                        timestamp=timestamp,
                                        sender=sender,
                                        receiver=receiver))

    def show_history(self):
        return ' | '.join(map(str, self.history))

    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        return f"{self.name} баланс: {self.balance} руб. паспорт: {self.passport8} т.{self.phone_number}"

    def __str__(self):
        return f"{self.name} баланс: {self.balance} руб."

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"{self.name}"

    def close(self):
        ARCHIVE.append(self.__deepcopy__())
        ACCOUNTS.remove(self)

    def __deepcopy__(self, memodict={}):
        new_obj = Account(self.name, self.passport8, self.phone_number, start_balance=self.balance)
        new_obj.history = self.history
        return new_obj


class CreditAccount(Account):
    def __init__(self, limit=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.limit = limit
        self.base_transfer_fee = 0.02
        self.negative_balance_transfer_fee = 0.05

    def calculate_fee(self, amount=0):
        if self.balance - amount <= 0:
            self.transfer_fee = self.negative_balance_transfer_fee
        else:
            self.transfer_fee = self.base_transfer_fee

    def transfer(self, target_account, amount):
        self.calculate_fee(amount)
        super(CreditAccount, self).transfer(target_account, amount)

    def withdraw(self, amount):
        if self.balance + self.limit < amount:
            raise ValueError('Недостаточно средств')
        self.balance -= amount
        self.add_to_history(timestamp=datetime.now().timestamp(),
                            operation=Transaction.WITHDRAW,
                            sender=self,
                            amount=amount,
                            fee=0.0)

    def full_info(self):
        return f"{self.name} баланс: {self.balance} руб. лимит: {self.limit} руб. паспорт: {self.passport8} " \
               f"т.{self.phone_number}"

    def __str__(self):
        return '<K>' + super().__str__() + f' лимит {self.limit}руб.'

    def __repr__(self):
        return '<K>' + super().__repr__()

    def __deepcopy__(self, memodict={}):
        new_obj = CreditAccount(limit=self.limit, name=self.name, passport8=self.passport8,
                                phone_number=self.phone_number, start_balance=self.balance)
        new_obj.history = self.history
        return new_obj


def save_session(accounts: list, archive: list):
    with open('session.pickle', 'wb') as f:
        pickle.dump({'accounts': accounts, 'archive': archive}, f)


def load_session() -> (list, list):
    with open('session.pickle', 'rb') as f:
        data = pickle.load(f)
    return data['accounts'], data['archive']


def get_amount():
    while True:
        try:
            amount = int(input('Введите сумму: '))
            break
        except ValueError:
            print('Необходимо ввести ЦЕЛОЕ ЧИСЛО')
    return amount


def close_account(account):
    """
    Закрыть счет клиента.
    Считаем, что оставшиеся на счету деньги были выданы клиенту наличными, при закрытии счета
    """
    account.close()
    print('счёт отправлен в архив')


def view_accounts_list():
    """Отображение всех клиентов банка в виде нумерованного списка"""
    print('*' * 30)
    print('Список счетов:')
    for i, account, in enumerate(ACCOUNTS):
        print(f'{i + 1}: {account.full_info()}')
        print(f'\t{account.show_history()}')
    print('*' * 30)
    print('Архив:')
    for i, account, in enumerate(ARCHIVE):
        print(f'{i + 1}: {account.full_info()}')
        print(f'\t{account.show_history()}')
    print('*' * 30)


def view_account_by_passport():
    while True:
        passport = input('Введите номер паспорта: ')
        for account in ACCOUNTS:
            if account.passport8 == passport:
                return account
        print('Такого пользователя не существует, либо введён неверный номер паспорта')
        print('1. Повторить')
        print('2. Выход')
        while True:
            choice = input(': ')
            if choice == '1':
                break
            elif choice == '2':
                raise InterruptedError


def view_client_account(account):
    """Узнать состояние своего счета"""
    print(account.full_info())
    print(account.show_history())


def put_account(account):
    """
    Пополнить счет на указанную сумму.
    Считаем, что клиент занес наличные через банкомат
    """
    amount = get_amount()
    account.deposit(amount)


def withdraw(account):
    """
    Снять со счета.
    Считаем, что клиент снял наличные через банкомат
    """
    amount = get_amount()
    account.withdraw(amount)


def transfer(account):
    """
    Перевести на счет другого клиента по номеру телефона
    """
    amount = get_amount()
    try:
        receiver = view_account_by_passport()
        account.transfer(receiver, amount)
    except InterruptedError:
        print('Операция перевода отменена')


def create_new_account():
    print("Укажите данные клиента")
    name = input("Имя:")
    passport = input("Номер паспорта: ")
    phone_number = input("Номер телефона: ")
    while True:
        print('1. Дебетовый')
        print('2. Кредитный')
        account_type = input(':')
        if account_type == '1' or account_type == '2':
            break
    balance = int(input('Начальный баланс: '))
    if account_type == '1':
        ACCOUNTS.append(Account(name=name, passport8=passport, phone_number=phone_number, start_balance=balance))
    else:
        limit = int(input('Кредитный лимит: '))
        ACCOUNTS.append(CreditAccount(name=name, passport8=passport, phone_number=phone_number, start_balance=balance,
                                      limit=limit))


def client_menu(account):
    while True:
        print(f"***********Меню клиента <{account.name}>*************")
        print("1. Состояние счета")
        print("2. Пополнить счет")
        print("3. Снять со счета")
        print("4. Перевести деньги другому клиенту банка")
        print("5. Exit")
        choice = input(":")
        if choice == "1":
            view_client_account(account)
        elif choice == "2":
            put_account(account)
        elif choice == "3":
            withdraw(account)
        elif choice == "4":
            transfer(account)
        elif choice == "5":
            return
    # input("Press Enter")


def employee_menu():
    while True:
        print("***********Меню сотрудника*************")
        print("1. Создать новый счет")
        print("2. Закрыть счет")
        print("3. Посмотреть список счетов")
        print("4. Посмотреть счет по номеру паспорта")
        print("5. Exit")
        choice = input(":")
        if choice == "1":
            create_new_account()
        elif choice == "2":
            account = view_account_by_passport()
            close_account(account)
        elif choice == "3":
            view_accounts_list()
        elif choice == "4":
            try:
                print(view_account_by_passport())
            except InterruptedError:
                pass
        elif choice == "5":
            return


def employee_access():
    """
    Проверяет доступ сотрудника банка, запрашивая пароль
    """
    password = input("Пароль: ")
    if password == EMPLOYEE_PASSWORD:
        return True
    return False


def client_access(accounts):
    """
    Находит аккаунт с введеным номером паспорта
    Или возвращает False, если аккаунт не найден
    """
    try:
        passport = int(input("Номер паспорта: "))
    except ValueError:
        return False
    for account in accounts:
        if str(passport).strip() == str(account.passport8).strip():
            return account
    return False


def start_menu():
    while True:
        print("Укажите вашу роль:")
        print("1. Сотрудник банка")
        print("2. Клиент")
        print("3. Завершить работу")

        choice = input(":")
        if choice == "3":
            save_session(ACCOUNTS, ARCHIVE)
            break
        elif choice == "1":
            if employee_access():
                employee_menu()
            else:
                print("Указан неверный пароль, укажите роль и повторите попытку...")
        elif choice == "2":
            account = client_access(ACCOUNTS)
            if account:
                client_menu(account)
            else:
                print("Указан несуществующий пасспорт, укажите роль и повторите попытку...")
        else:
            print("Указан некорректный пункт меню, повторите выбор...")


if __name__ == "__main__":
    ACCOUNTS, ARCHIVE = load_session()
    start_menu()
    save_session(ACCOUNTS, ARCHIVE)
