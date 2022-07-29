class Operation:
    DEPOSIT = 'Пополнение'
    WITHDRAW = 'Снятие'
    TRANSFER_OUT = 'Перевод'
    TRANSFER_IN = 'Поступление'

    def __init__(self, operation_type, amount, corr_acc=None):
        self.operation_type = operation_type
        self.amount = amount
        self.corr_acc = corr_acc

    def __repr__(self):
        if self.corr_acc is None:
            return f'{self.operation_type} на сумму {self.amount} руб.'
        else:
            if self.operation_type == Operation.TRANSFER_OUT or self.operation_type == Operation.TRANSFER_IN:
                return f'{self.operation_type} на сумму {self.amount} руб. на счет клиента: {self.corr_acc}'
            else:
                return f'{self.operation_type} на сумму {self.amount} руб. со счета клиента: {self.corr_acc}'


class Account:
    def __init__(self, name, passport, phone_number, start_balance=0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.__balance = start_balance
        self.__history = []

    @property
    def balance(self):
        return self.__balance

    @property
    def history(self):
        return self.__history

    def deposit(self, amount, is_transfer=False, corr_acc=None):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        if is_transfer:
            self.__balance += amount
            depo_hist = Operation(Operation.TRANSFER_IN, amount, corr_acc)
            self.__history.append(depo_hist)
        else:
            self.__balance += amount
            depo_hist = Operation(Operation.DEPOSIT, amount)
            self.__history.append(depo_hist)

    def withdraw(self, amount, is_transfer=False, corr_acc=None):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.__balance >= amount:
            if is_transfer:
                self.__balance -= amount
                with_hist = Operation(Operation.TRANSFER_OUT, amount, corr_acc)
                self.__history.append(with_hist)
            else:
                self.__balance -= amount
                with_hist = Operation(Operation.WITHDRAW, amount)
                self.__history.append(with_hist)
        else:
            raise ValueError("Недостаточно средств на балансе")

    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        self.withdraw(amount, True, target_account.name)
        target_account.deposit(amount, True, self.name)

    def full_info(self):
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 3200 123456 т.+7-900-200-02-03"
        """
        return f"{self.name} баланс: {self.__balance} руб. паспорт: {self.passport} т.{self.phone_number}"

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иван баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.__balance} руб."

    # TODO-1: добавьте проверку паспорта и телефона(в конструкторе) на соответствие заданным форматам
    #  В случае несоответствия выбрасываем исключение ValueError("Неверный формат телефона/паспорта")
    #  Проверка информации на корректность - валидация
    #  Готовые валидаторы можете взять в директории helpers


if __name__ == '__main__':
    account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 1000)  # аккаунт с корректными данными
    account2 = Account("Алексей", "+7-901-744-22-99", "323 456124", 200)  # номер паспорта задан не верно
    account3 = Account("Петр", "+7-904-745-47", "3232 456124", 200)  # номер телефона задан не верно

    account1.deposit(100)
    account1.transfer(account2, 1000)
    print(account1.history)
    print(account2.history)
