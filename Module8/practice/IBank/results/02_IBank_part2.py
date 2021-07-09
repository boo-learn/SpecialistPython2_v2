
class Account(AccountBase):
    def __init__(self, name, passport8, phone_number, start_balance=0):
        super().__init__(name, passport8, phone_number, start_balance)
        self.flag = False
        self.history = []

    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        self.flag = True
        self.withdraw(amount)
        self.history.append(f'Перевод  {amount} руб.  на счет {target_account.name}.')
        self.flag = True
        target_account.deposit(amount)
        target_account.history.append(f'Перевод  {amount} руб.  со счёта  {self.name}.')

    def deposit(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        if amount < 0:
            raise ValueError("Сумма должна быть положительная")
        self.balance += amount
        if not self.flag:
            self.history.append(f'Пополнение счета на {amount} руб.')
        else:
            self.flag = False

    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        commission = 0.02
        if self.balance < amount:
            raise ValueError("Суммы на счёте недостаточно")
        amount = amount * (1 + commission)
        self.balance -= amount
        if not self.flag:
            self.history.append(f'Снятие со счета {amount} руб.')
        else:
            self.flag = False

    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        return f"{self.name}  баланс: {self.balance} руб. паспорт: {self.passport8} т.{self.phone_number}"

    def show_history(self):
        return self.history

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """

        return f"{self.name} баланс: {self.balance} руб."


if __name__ == "__main__":

    account1 = Account("Lol", 2314234, "+79181234558")
    account1.deposit(600)
    account2 = Account("Lol2", 2314234, "+79181598734")
    try:
        account1.transfer(account2, 100)
    except ValueError as e:
        print(e)

    account1.deposit(600)
    account2.withdraw(0)

    print(account1.show_history())
    print(account2.show_history())
